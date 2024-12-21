# StudentOverflow - Proyecto Flask con PostgreSQL y JWT

StudentOverflow es una aplicación web inspirada en StackOverflow, donde los usuarios pueden registrarse, iniciar sesión y publicar preguntas sobre diferentes materias. La autenticación está implementada utilizando JSON Web Tokens (JWT). El proyecto está desarrollado con **Flask** como el framework web, **PostgreSQL** como base de datos, y **JWT** para gestionar la autenticación.

## Requisitos

- **Python 3.x**
- **PostgreSQL** (con `pg8000` como driver para Python)
- **pip** para gestionar las dependencias de Python

## Estructura del Proyecto

```
project/
│
├── app/
│   ├── __init__.py           # Inicializa la aplicación y las extensiones (db, JWT, etc.)
│   ├── models.py            # Define los modelos de base de datos
│   ├── routes.py            # Define las rutas y la lógica
│   └── templates/
│       ├── index.html       # Página de inicio
│       ├── ask_question.html # Página para hacer preguntas
│       └── login.html       # Página de inicio de sesión
│
├── config.py                # Configuración global del proyecto (base de datos, JWT, etc.)
└── run.py                   # Archivo para ejecutar la aplicación
```

## Instalación y Configuración

Sigue estos pasos para configurar el entorno de desarrollo y ejecutar la aplicación:

### 1. Clonar el Repositorio

Clona el repositorio del proyecto:

```bash
git clone <https://github.com/castaedd/StudentOverflow>
cd StudentOverflow
```

### 2. Crear un Entorno Virtual

Es recomendable usar un entorno virtual para aislar las dependencias del proyecto:

```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate     # En Windows
```

### 3. Instalar Dependencias

Instala las dependencias necesarias para el proyecto:

```bash
pip install -r requirements.txt
```

Crea el archivo `requirements.txt` con las siguientes dependencias:

```txt
Flask
Flask-SQLAlchemy
Flask-JWT-Extended
pg8000
```

### 4. Configurar PostgreSQL

Asegúrate de tener PostgreSQL instalado y en ejecución en tu máquina. Si no lo tienes, sigue la documentación oficial de [PostgreSQL](https://www.postgresql.org/docs/).

1. Crea una base de datos para el proyecto:

```bash
psql -U postgres
CREATE DATABASE dbname;  # Cambia 'dbname' por el nombre que des a tu base de datos
```

2. Actualiza la configuración en `app/__init__.py` con los datos correctos de tu base de datos:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+pg8000://usuario:contraseña@localhost/dbname'
```

- **usuario**: El nombre de usuario de PostgreSQL.
- **contraseña**: La contraseña del usuario.
- **dbname**: El nombre de la base de datos que creaste.

### 5. Crear las Tablas en la Base de Datos

Antes de iniciar la aplicación, crea las tablas en la base de datos. Para ello, abre una consola interactiva de Python con el siguiente comando:

```bash
python
```

Dentro de la consola de Python, ejecuta:

```python
from app import db
db.create_all()
```

Esto creará las tablas `user` y `question` en la base de datos PostgreSQL.

### 6. Configurar el Secreto JWT

Abre el archivo `app/__init__.py` y cambia la clave secreta para JWT:

```python
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Cambia esto por una clave secreta segura
```

### 7. Ejecutar la Aplicación

Para iniciar la aplicación, ejecuta el siguiente comando:

```bash
python run.py
```

La aplicación se ejecutará en `http://127.0.0.1:5000/`.

## Rutas de la Aplicación

1. **Página de Inicio** `/`
   - Muestra la página principal del proyecto.

2. **Página para Hacer una Pregunta** `/question`
   - **Método**: GET, POST
   - Si el usuario está autenticado con un token JWT, puede enviar una nueva pregunta.
   - Se requiere que el token JWT se pase en los encabezados como `Authorization: Bearer <token>`.

3. **Registro de Usuario** `/register`
   - **Método**: GET, POST
   - Los usuarios pueden registrarse proporcionando un nombre de usuario, correo electrónico y contraseña. La contraseña se guarda de forma segura con un hash.

4. **Autenticación y JWT**
   - Se utiliza el módulo **Flask-JWT-Extended** para manejar el inicio de sesión y la validación del token JWT.

## Funcionalidades

- **Registro de Usuario**: Los usuarios pueden registrarse proporcionando un nombre de usuario, correo electrónico y una contraseña segura.
- **Inicio de Sesión**: Los usuarios pueden iniciar sesión proporcionando sus credenciales para obtener un token JWT.
- **Publicar Preguntas**: Los usuarios pueden publicar preguntas solo si están autenticados mediante JWT.
- **Autenticación de Usuario**: Se utiliza JWT para gestionar la autenticación y protección de rutas.

## Contribución

Si deseas contribuir al proyecto, haz un fork del repositorio y envía un pull request con las mejoras que hayas realizado.
