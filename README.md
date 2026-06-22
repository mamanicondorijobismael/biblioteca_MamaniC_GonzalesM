Gonzales Moscoso Roberto Carlos

Mamani Condori Job Ismael


📚 Biblioteca Digital - Sistema de Gestión de Biblioteca
Proyecto desarrollado con Django como parte de la asignatura de Programación Web. Implementa un sistema completo de gestión de biblioteca con control de libros, autores y préstamos, aplicando autenticación y autorización nativa de Django.

🚀 Características
Modelos: Autor, Libro, Préstamo (relacionados con ForeignKey).

CRUD completo: Crear, leer, actualizar y eliminar registros.

Autenticación: Login/Logout con el sistema nativo de Django.

Autorización:

Usuarios anónimos: solo pueden ver listados y detalles.

Usuarios autenticados: pueden crear y editar registros.

Administradores (is_staff): pueden eliminar registros.

Interfaz dinámica: Bootstrap 5 con diseño moderno y responsivo.

Slug automático: generado con slugify para URLs amigables.

🛠️ Tecnologías utilizadas
Python 3.13+

Django 5.0.10

Bootstrap 5.3

SQLite (base de datos por defecto)

📦 Instalación y configuración
Sigue estos pasos para ejecutar el proyecto en tu máquina local.

1. Clonar el repositorio
bash
git clone https://github.com/tu-usuario/biblioteca-django.git
cd biblioteca-django
2. Crear y activar un entorno virtual
bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
3. Instalar dependencias
bash
pip install django
Si deseas generar un archivo requirements.txt, ejecuta:

bash
pip freeze > requirements.txt
Luego, para instalar desde ese archivo: pip install -r requirements.txt

4. Aplicar migraciones
bash
python manage.py makemigrations
python manage.py migrate
5. Crear un superusuario (administrador)
bash
python manage.py createsuperuser
Sigue las instrucciones para crear el usuario admin (ej: admin, contraseña: admin123).

6. Crear un usuario normal (para probar roles)
Desde el panel de administración o mediante el shell:

bash
python manage.py shell
python
from django.contrib.auth.models import User
User.objects.create_user('usuario', 'usuario@mail.com', 'pass123')
exit()
7. Ejecutar el servidor
bash
python manage.py runserver
Abre tu navegador en http://127.0.0.1:8000/.

🔐 Roles y permisos
Rol	Acciones permitidas
Anónimo	Ver listados y detalles de libros, autores y préstamos.
Usuario autenticado	Crear y editar cualquier registro.
Administrador (is_staff)	Eliminar registros (además de crear y editar).
Los botones de acción se muestran/ocultan dinámicamente en las plantillas según el rol del usuario.

📁 Estructura del proyecto
text
biblioteca_django/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── biblioteca/               # Aplicación principal
│   ├── models.py             # Modelos: Autor, Libro, Prestamo
│   ├── views.py              # Vistas con mixins de autorización
│   ├── forms.py              # ModelForms con estilos Bootstrap
│   ├── urls.py               # Rutas de la app
│   ├── templates/
│   │   ├── base.html         # Plantilla base con navbar y estilos
│   │   ├── biblioteca/       # Plantillas CRUD
│   │   └── registration/     # Plantilla de login
│   └── admin.py              # Registro de modelos en admin
├── manage.py
└── README.md
🧪 Datos de prueba (opcional)
Puedes cargar datos de prueba desde el panel de administración (/admin). Inicia sesión con el superusuario y agrega autores, libros y préstamos.

📝 Notas para la defensa
Demostración de roles:

Anónimo: navega sin iniciar sesión.
Usuario normal: inicia sesión y prueba crear/editar.
Administrador: inicia sesión con superusuario y prueba eliminar.
Explicación técnica:

Uso de LoginRequiredMixin y UserPassesTestMixin para proteger vistas.

Condicionales en plantillas con {% if user.is_authenticated %} y {% if user.is_staff %}.

Generación de slugs con slugify en el método save() de los modelos.
