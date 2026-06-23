from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Autor, Libro, Prestamo
from .forms import Autorform, Libroform, Prestamoform


class SuperuserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Solo permite acceso a superusuarios. Retorna 403 si no es superusuario."""
    def test_func(self):
        return self.request.user.is_superuser


class AutorListView(ListView):
    model = Autor
    template_name = 'biblioteca/autor_list.html'
    context_object_name = 'autores'
    
class AutorDetailView(DetailView):
    model = Autor
    template_name = 'biblioteca/autor_detail.html'
    context_object_name = 'autor'
    
class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    form_class = Autorform
    template_name = 'biblioteca/autor_form.html'
    success_url = reverse_lazy('biblioteca:autor_list')
    
class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    form_class = Autorform
    template_name = 'biblioteca/autor_form.html'
    success_url = reverse_lazy('biblioteca:autor_list')
    
class AutorDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Autor
    template_name = 'biblioteca/autor_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:autor_list')
    
class LibroListView(ListView):
    model = Libro
    template_name = 'biblioteca/libro_list.html'
    context_object_name = 'libros'

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'biblioteca/libro_detail.html'
    context_object_name = 'libro'

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = Libroform
    template_name = 'biblioteca/libro_form.html'
    success_url = reverse_lazy('biblioteca:libro_list')
    
class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = Libroform
    template_name = 'biblioteca/libro_form.html'
    success_url = reverse_lazy('biblioteca:libro_list')
    
class LibroDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Libro
    template_name = 'biblioteca/libro_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:libro_list')
    
class PrestamoListView(ListView):
    model = Prestamo
    template_name = 'biblioteca/prestamo_list.html'
    context_object_name = 'prestamos'
    
class PrestamoDetailView(DetailView):
    model = Prestamo
    template_name = 'biblioteca/prestamo_detail.html'
    context_object_name = 'prestamo'

class PrestamoCreateView(LoginRequiredMixin, CreateView):
    model = Prestamo
    form_class = Prestamoform
    template_name = 'biblioteca/prestamo_form.html'
    success_url = reverse_lazy('biblioteca:prestamo_list')
    
class PrestamoUpdateView(LoginRequiredMixin, UpdateView):
    model = Prestamo
    form_class = Prestamoform
    template_name = 'biblioteca/prestamo_form.html'
    success_url = reverse_lazy('biblioteca:prestamo_list')
    
class PrestamoDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Prestamo
    template_name = 'biblioteca/prestamo_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:prestamo_list')