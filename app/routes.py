from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .models import db, User, Question
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

main_bp = Blueprint('main', __name__)

# Página principal
@main_bp.route('/')
def home():
    return render_template('index.html')

# Registro de usuarios
@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        new_user = User(username=data['username'], email=data['email'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html')

# Inicio de sesión
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(email=data['email']).first()
        if user and user.password == data['password']:
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token)
        return jsonify({'message': 'Invalid credentials'}), 401
    return render_template('login.html')

# Preguntas
@main_bp.route('/question', methods=['GET', 'POST'])
@jwt_required()
def ask_question():
    if request.method == 'POST':
        current_user_id = get_jwt_identity()  # Obtener el ID del usuario actual
        data = request.form  # Obtener los datos del formulario

        # Crear una nueva pregunta
        new_question = Question(
            title=data['title'], 
            content=data['content'], 
            user_id=current_user_id
        )
        db.session.add(new_question)
        db.session.commit()

        # Redirigir al home o alguna otra página después de crear la pregunta
        return redirect(url_for('main.home'))

    # Si es un GET, simplemente renderiza el formulario
    return render_template('ask_question.html')

