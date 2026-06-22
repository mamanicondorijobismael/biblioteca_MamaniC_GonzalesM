# 📚 Biblioteca Digital – Sistema de Gestión con Django

[![Django](https://img.shields.io/badge/Django-5.0.10-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completado-brightgreen)]()
[![GitHub last commit](https://img.shields.io/github/last-commit/tu-usuario/biblioteca-django)]()

Sistema web completo para la gestión de una biblioteca, desarrollado con **Django** como proyecto final de la asignatura **Programación Web**. Permite administrar libros, autores y préstamos, con un sistema de autenticación y autorización basado en roles.

---

## ✨ Características principales

- ✅ **CRUD completo** para Libros, Autores y Préstamos.
- ✅ **Autenticación nativa de Django** (login/logout).
- ✅ **Roles y permisos diferenciados**:
  - 👤 **Usuario anónimo** → solo visualización (listados y detalles).
  - 👥 **Usuario autenticado** → puede crear y editar registros.
  - 🛡️ **Administrador (is_staff)** → puede eliminar registros (además de crear/editar).
- ✅ **URLs amigables** con slugs generados automáticamente a partir del título o nombre.
- ✅ **Interfaz moderna y responsiva** con Bootstrap 5 y tema oscuro personalizado.
- ✅ **Mensajes flash** para retroalimentar las acciones del usuario.
- ✅ **Panel de administración** de Django para gestión rápida de datos.

---

## 🖥️ Capturas de pantalla

> ⚠️ **Nota:** Agrega tus propias imágenes en la carpeta `screenshots/` y reemplaza las rutas si es necesario.

### 📋 Lista de libros
![Lista de libros](screenshots/libro_list.png)
*Vista principal con tabla de libros y botones dinámicos según el rol del usuario.*

### ➕ Crear / Editar libro
![Formulario de libro](screenshots/libro_form.png)
*Formulario con estilos Bootstrap y validación integrada.*

### 👑 Panel de administración
![Panel de administración](screenshots/admin.png)
*Panel de Django para gestionar autores, libros y préstamos.*

### 🔐 Inicio de sesión
![Login](screenshots/login.png)
*Página de inicio de sesión con diseño coherentemente integrado.*

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Versión | Uso |
| :--- | :--- | :--- |
| **Python** | 3.13 | Lenguaje de programación |
| **Django** | 5.0.10 | Framework web |
| **Bootstrap** | 5.3 | Diseño y maquetación |
| **SQLite** | 3 | Base de datos (por defecto) |
| **HTML5 / CSS3** | - | Estructura y estilos personalizados |
| **Bootstrap Icons** | 1.11 | Iconos vectoriales |

---

## 📦 Instalación y configuración (paso a paso)

Sigue estas instrucciones para ejecutar el proyecto en tu máquina local.

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/biblioteca-django.git
cd biblioteca-django
---

2. Crear y activar un entorno virtual

python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS / Linux:
source venv/bin/activate
