from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Inicialización de la base de datos y migraciones
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()  # Inicializa el objeto JWTManager

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+pg8000://postgres:Soyenergia93@localhost/studentoverflow'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Debes definir esta clave en tu configuración
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)  # Asocia JWTManager con la aplicación

    # Importar las rutas
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

