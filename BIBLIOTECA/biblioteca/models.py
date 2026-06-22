from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.nombre} {self.apellido}")
            slug = base_slug
            counter = 1
            while Autor.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_absolute_url(self):
        return reverse('biblioteca:autor_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name_plural = 'Autores'


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    disponible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            counter = 1
            while Libro.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('biblioteca:libro_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['titulo']
        verbose_name_plural = 'Libros'


class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prestamos')
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} - {self.libro.titulo}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Actualizar la disponibilidad del libro automáticamente
        # Un libro está disponible solo si no tiene préstamos activos (no devueltos)
        tiene_prestamos_activos = self.libro.prestamos.filter(devuelto=False).exists()
        self.libro.disponible = not tiene_prestamos_activos
        self.libro.save()

    def delete(self, *args, **kwargs):
        libro = self.libro
        super().delete(*args, **kwargs)
        # Al eliminar el préstamo, verificar si el libro vuelve a estar disponible
        tiene_prestamos_activos = libro.prestamos.filter(devuelto=False).exists()
        libro.disponible = not tiene_prestamos_activos
        libro.save()

    class Meta:
        ordering = ['-fecha_prestamo']
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'