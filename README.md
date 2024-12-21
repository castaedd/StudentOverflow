# Proyecto Flask con PostgreSQL y JWT

Este es un proyecto básico de una aplicación web utilizando Flask, PostgreSQL, y JWT (JSON Web Tokens) para autenticación. El proyecto permite a los usuarios registrarse, iniciar sesión, y publicar preguntas de manera similar a un foro.

## Requisitos

- **Python 3.x**
- **PostgreSQL** (con `pg8000` como driver para Python)
- **pip** para gestionar las dependencias de Python

## Estructura del Proyecto
project/ │ ├── app/ │ ├── init.py # Inicializa la aplicación y las extensiones (db, JWT, etc.) │ ├── models.py # Define los modelos de base de datos │ ├── routes.py # Define las rutas y la lógica │ └── templates/ │ ├── index.html # Página de inicio │ ├── ask_question.html │ └── login.html ├── config.py # Configuración global del proyecto (base de datos, JWT, etc.) └── run.py # Archivo para ejecutar la aplicación


## Instalación y Configuración

Sigue estos pasos para configurar el entorno de desarrollo y ejecutar la aplicación:

### 1. Clonar el Repositorio

Si aún no tienes el proyecto, clónalo a tu máquina:

```bash
git clone <https://github.com/castaedd/StudentOverflow>
cd <StudentOverflow>

