markdown<div align="center">
  
  # 📚 Biblioteca Digital
  ### *Sistema de Gestión con Django para la asignatura de Programación Web*

  [![Django](https://shields.io)](https://djangoproject.com)
  [![Python](https://shields.io)](https://python.org)
  [![Bootstrap](https://shields.io)](https://getbootstrap.com)
  [![License](https://shields.io)](https://opensource.org)
  [![Status](https://shields.io)](https://github.com/)

  Análisis y desarrollo de un sistema web completo para la gestión bibliotecaria. La plataforma integra la administración de catálogos y flujos de préstamos mediante un control estricto de accesos basado en perfiles de usuario.

  [🌐 Reportar un Error](https://github.com) • [📖 Solicitar Mejora](https://github.com)
</div>

---

## 🗺️ Menú de Navegación rápida
* [✨ Características Principales](#-características-principales)
* [🖥️ Vista Previa del Sistema](#️-vista-previa-del-sistema)
* [🛠️ Ficha Técnica](#️-ficha-técnica)
* [📦 Guía de Instalación](#-guía-de-instalación-y-configuración)
* [🔐 Matriz de Seguridad](#-matriz-de-seguridad-y-permisos)
* [📁 Arquitectura del Directorio](#-arquitectura-del-directorio)
* [📝 Fundamentación Técnica](#-fundamentación-técnica-defensa-de-proyecto)

---

## ✨ Características Principales

* 🔄 **Módulos CRUD Completos:** Gestión autónoma y relacional de Libros, Autores y Préstamos.
* 🔑 **Autenticación Centralizada:** Control de sesiones nativo de Django (Login/Logout).
* 🛡️ **Seguridad por Capas (Roles):**
    * `Anónimo:` Permisos exclusivos de lectura y navegación libre.
    * `Autenticado:` Capacidad operativa para registrar y modificar registros.
    * `Administrador (is_staff):` Control total del sistema, incluyendo la eliminación de datos.
* 🔍 **Optimización SEO & UX:** Enrutamiento semántico mediante la generación automática de *slugs*.
* 🎨 **Diseño Vanguardista:** Interfaz responsiva basada en Bootstrap 5 con la implementación de un tema oscuro personalizado.

---

## 🖥️ Vista Previa del Sistema

> 💡 **Nota para el despliegue:** Asegúrate de almacenar tus capturas dentro del directorio `screenshots/` local para asegurar su correcta vinculación. Puedes usar un GIF animado en esta sección para simular el uso en tiempo real.

| 📋 Lista de Libros | ➕ Formulario Operativo |
|:---:|:---:|
| ![Lista de libros](screenshots/libro_list.png) | ![Formulario de libro](screenshots/libro_form.png) |
| *Botonera dinámica adaptada al rol* | *Validación de campos en tiempo real* |

| 👑 Panel de Administración | 🔐 Control de Acceso |
|:---:|:---:|
| ![Panel de administración](screenshots/admin.png) | ![Login](screenshots/login.png) |
| *Backoffice nativo para la gestión de datos* | *Diseño minimalista y seguro* |

---

## 🛠️ Ficha Técnica

| Componente | Versión | Propósito del Sistema |
| :--- | :--- | :--- |
| **Python** | `3.13` | Entorno de ejecución y lógica de programación |
| **Django** | `5.0.10` | Framework de arquitectura MVC (MVT) |
| **Bootstrap** | `5.3` | Maquetación responsiva y diseño de interfaz |
| **SQLite** | `3` | Motor de persistencia de datos local |
| **Bootstrap Icons** | `1.11` | Iconografía vectorial del aplicativo |

---

## 📦 Guía de Instalación y Configuración

<details>
<summary><b>🛠️ Haz clic aquí para desplegar los pasos de instalación paso a paso</b></summary>
<br>

Sigue atentamente este flujo secuencial para clonar y ejecutar el ecosistema en tu entorno de desarrollo local.

### Paso 1: Obtención del código fuente
Clona el repositorio oficial en tu máquina e ingresa al directorio raíz del proyecto:
```bash
git clone https://github.com/tu-usuario/biblioteca-django.git
cd biblioteca-django
```

### Paso 2: Configuración del entorno virtual
Instancia un entorno aislado para mitigar conflictos de dependencias y procede a su activación automática:

* **En Windows (PowerShell / CMD):**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **En macOS / Linux (Terminal):**
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

### Paso 3: Aprovisionamiento de paquetes
Garantiza la instalación del framework y sus componentes asociados. Si dispones del manifiesto ejecútalo, de lo contrario instala directamente:
```bash
pip install -r requirements.txt
# Alternativa directa si no posees el archivo: pip install django
```

### Paso 4: Migración de la Base de Datos
Estructura el esquema relacional en el motor SQLite ejecutando las preparaciones de modelos:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Paso 5: Gestión de Cuentas Administrativas
Genera la credencial maestra para acceder al panel de control de administración principal:
```bash
python manage.py createsuperuser
```
*Sigue las instrucciones en consola (Ej: Usuario: `admin` / Contraseña: `admin123`).*

### Paso 6: Generación de Usuarios de Prueba
Para validar la correcta segregación de roles (Permisos estándar vs Staff), crea un perfil alternativo abriendo la consola interactiva:
```bash
python manage.py shell
```
Una vez dentro del prompt de Python, introduce el siguiente bloque y presiona Enter:
```python
from django.contrib.auth.models import User
User.objects.create_user('usuario', 'usuario@mail.com', 'password123')
exit()
```

### Paso 7: Inicialización del Servidor
Despliega el servidor HTTP local para verificar la funcionalidad completa de la aplicación:
```bash
python manage.py runserver
```
Acceso web inmediato en tu explorador: **http://127.0.0.1:8000/**

</details>

---

## 🔐 Matriz de Seguridad y Permisos

| Nivel de Perfil | Operaciones Permitidas | Mecanismo de Control Técnico |
| :--- | :--- | :--- |
| **Anónimo** | Lectura de listados generales y consultas detalladas. | Rutas públicas sin restricciones de Mixins. |
| **Autenticado** | Mutación selectiva: Alta y Edición de entidades del catálogo. | `LoginRequiredMixin` inyectado en `CreateView` y `UpdateView`. |
| **Administrador** | Destrucción de datos: Eliminación física de registros. | `UserPassesTestMixin` evaluando el flag estricto de `is_staff`. |

### Abstracción de lógica en Capa de Presentación (Templates HTML):
```html
{% if user.is_authenticated %}
    <a href="#" class="btn btn-warning">Modificar Registro</a>
{% endif %}

{% if user.is_staff %}
    <a href="#" class="btn btn-danger">Eliminar Registro Permanente</a>
{% endif %}
```

---

## 📁 Arquitectura del Directorio

<details>
<summary><b>📂 Haz clic aquí para explorar el árbol de archivos estructurado</b></summary>
<br>

```plaintext
biblioteca-django/
├── config/                         # Core - Configuración global del proyecto
│   ├── __init__.py
│   ├── settings.py                 # Variables de entorno y utilidades
│   ├── urls.py                     # Enrutador principal de la aplicación
│   └── wsgi.py
├── biblioteca/                     # Aplicación modular de negocio
│   ├── migrations/                 # Historial de cambios en base de datos
│   ├── templates/
│   │   ├── base.html               # Layout maestro (Navbar, Footer, Estilos)
│   │   ├── biblioteca/             # Vistas de entidades específicas
│   │   │   ├── autor_list.html
│   │   │   ├── autor_detail.html
│   │   │   ├── autor_form.html
│   │   │   ├── autor_confirm_delete.html
│   │   │   ├── libro_list.html
│   │   │   └── (demás sub-plantillas del CRUD)...
│   │   └── registration/
│   │       └── login.html          # Interfaz de acceso al sistema
│   ├── admin.py                    # Reglas de visualización del Backoffice
│   ├── forms.py                    # Formularios enlazados a modelos (Bootstrap 5)
│   ├── models.py                   # Esquemas de datos (Autor, Libro, Préstamo)
│   ├── urls.py                     # Rutas internas de la app
│   └── views.py                    # Controladores basados en clases (CBV)
├── manage.py                       # Utilidad de administración en consola
├── requirements.txt                # Manifiesto de dependencias
└── README.md                       # Documento técnico actual
```
</details>

---

## 📝 Fundamentación Técnica (Defensa de Proyecto)

* **Persistencia y Abstracción:** El modelo cuenta con tres entidades correlacionadas (`Autor`, `Libro`, `Prestamo`). Se anula la exposición de ID numéricos secuenciales sobreescribiendo el ciclo de vida en el método `save()` mediante la generación de slugs amigables para las URLs.
* **Controladores Avanzados:** La lógica de negocio fue desarrollada mediante Vistas Basadas en Clases (`CBV`), optimizando la reutilización de código y acelerando el tiempo de desarrollo del CRUD.

---
<div align="center">
  Desarrollado con ❤️ para la materia de Programación Web.
</div>
