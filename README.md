<!--
  README.md para Biblioteca Digital - Django
  Incluye badges, capturas de pantalla, instrucciones detalladas.
-->

# 📚 Biblioteca Digital

[![Django](https://img.shields.io/badge/Django-5.0.10-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completado-brightgreen)]()

Sistema de gestión de biblioteca desarrollado con **Django** como proyecto final de Programación Web. Incluye control de libros, autores, préstamos, autenticación de usuarios y autorización por roles.

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
