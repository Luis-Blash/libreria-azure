from flask import Blueprint
# controlador
from app.controller.librosController import subir_bibloteca, todolosLibros

# el controlador de ruta
libro_bp = Blueprint('libro_bp', __name__,static_folder='static', template_folder='templates')

libro_bp.route('/bibloteca', methods=['GET'])(todolosLibros)

libro_bp.route('/subir-libro', methods=['GET','POST'])(subir_bibloteca)