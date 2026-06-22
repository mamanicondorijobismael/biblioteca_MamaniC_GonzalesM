# 📚 Biblioteca Digital

[![Django](https://img.shields.io/badge/Django-5.0.10-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completado-brightgreen)]()

> Sistema de gestión de biblioteca desarrollado con **Django** como proyecto final de Programación Web.  
> Incluye control de libros, autores, préstamos, autenticación de usuarios y autorización por roles.

---

## ✨ Características principales

- ✅ **CRUD completo** para Libros, Autores y Préstamos.
- ✅ **Autenticación nativa de Django** (login/logout).
- ✅ **Roles y permisos**:
  - 👤 Anónimo → solo visualización.
  - 👥 Usuario registrado → crear y editar.
  - 🛡️ Administrador (`is_staff`) → eliminar registros.
- ✅ **URLs amigables** con slugs generados automáticamente.
- ✅ **Diseño moderno** con Bootstrap 5 y estilo oscuro personalizado.
- ✅ **Mensajes flash** para retroalimentación al usuario.

---

## 🖥️ Capturas de pantalla

<p align="center">
  <img src="screenshots/libro_list.png" alt="Lista de libros" width="70%">
  <br><em>Lista de libros con botones dinámicos según rol</em>
</p>

<p align="center">
  <img src="screenshots/libro_form.png" alt="Formulario de creación" width="70%">
  <br><em>Formulario para crear/editar libros</em>
</p>

<p align="center">
  <img src="screenshots/admin.png" alt="Panel de administración" width="70%">
  <br><em>Panel de administración de Django</em>
</p>

<p align="center">
  <img src="screenshots/login.png" alt="Pantalla de login" width="70%">
  <br><em>Pantalla de inicio de sesión</em>
</p>

> 📸 *Nota: Agrega tus propias capturas en la carpeta `screenshots/`.*

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Versión |
|------------|---------|
| Python     | 3.13    |
| Django     | 5.0.10  |
| Bootstrap  | 5.3     |
| SQLite     | 3       |
| HTML/CSS   | -       |

---

## 📦 Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/biblioteca-django.git
cd biblioteca-django
  
2. Crear y activar un entorno virtual
bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS / Linux:
source venv/bin/activate
3. Instalar dependencias
Si tienes el archivo requirements.txt:

bash
pip install -r requirements.txt
Si no, instala Django directamente:

bash
pip install django
4. Aplicar migraciones
bash
python manage.py makemigrations
python manage.py migrate
5. Crear un superusuario (administrador)
bash
python manage.py createsuperuser
Sigue las instrucciones en pantalla. Por ejemplo:

Usuario: admin

Correo: (puedes dejarlo en blanco)

Contraseña: admin123

6. Crear un usuario normal (para probar roles)
Puedes hacerlo desde el panel de administración (/admin) o desde la terminal:

bash
python manage.py shell
python
from django.contrib.auth.models import User
User.objects.create_user('usuario', 'usuario@mail.com', 'password123')
exit()
7. Ejecutar el servidor de desarrollo
bash
python manage.py runserver
Abre tu navegador y visita http://127.0.0.1:8000/.

🔐 Roles y permisos (detalle)
Rol	Acciones permitidas	¿Cómo se controla?
Anónimo (sin sesión)	Ver listados y detalles.	No se aplica ningún mixin.
Usuario autenticado	Crear y editar registros de libros, autores y préstamos.	LoginRequiredMixin en las vistas CreateView y UpdateView.
Administrador (is_staff)	Eliminar registros (además de crear y editar).	UserPassesTestMixin con test_func() que retorna self.request.user.is_staff.
En las plantillas: los botones de acción se ocultan/muestran con:

django
{% if user.is_authenticated %} ... {% endif %}
{% if user.is_staff %} ... {% endif %}
📁 Estructura del proyecto
text
biblioteca-django/
├── config/                         # Configuración del proyecto Django
│   ├── __init__.py
│   ├── settings.py                 # Configuración global
│   ├── urls.py                     # URLs principales (incluye las de la app)
│   └── wsgi.py
├── biblioteca/                     # Aplicación principal
│   ├── migrations/                 # Migraciones de base de datos
│   ├── templates/
│   │   ├── base.html               # Plantilla base con navbar y estilos
│   │   ├── biblioteca/             # Plantillas para cada modelo
│   │   │   ├── autor_list.html
│   │   │   ├── autor_detail.html
│   │   │   ├── autor_form.html
│   │   │   ├── autor_confirm_delete.html
│   │   │   ├── libro_list.html
│   │   │   ├── libro_detail.html
│   │   │   ├── libro_form.html
│   │   │   ├── libro_confirm_delete.html
│   │   │   ├── prestamo_list.html
│   │   │   ├── prestamo_detail.html
│   │   │   ├── prestamo_form.html
│   │   │   └── prestamo_confirm_delete.html
│   │   └── registration/
│   │       └── login.html          # Plantilla de inicio de sesión
│   ├── __init__.py
│   ├── admin.py                    # Registro de modelos en el admin
│   ├── apps.py
│   ├── forms.py                    # ModelForms con estilos Bootstrap
│   ├── models.py                   # Modelos: Autor, Libro, Prestamo
│   ├── urls.py                     # Rutas específicas de la app
│   └── views.py                    # Vistas con mixins de autorización
├── manage.py
├── requirements.txt                # Dependencias del proyecto
├── .gitignore                      # Archivos ignorados por Git
├── LICENSE                         # Licencia MIT (opcional)
└── README.md                       # Este archivo
🧪 Datos de prueba (opcional)
Puedes cargar datos de prueba directamente desde el panel de administración (/admin). Inicia sesión con tu superusuario y añade autores, libros y préstamos para tener contenido con el que mostrar.


