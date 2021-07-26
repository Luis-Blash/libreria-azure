from flask import Blueprint
# el controlador de ruta
from app.controller.busquedaController import busquedaLibros

busqueda_bp = Blueprint('busqueda_bp', __name__,static_folder='static', template_folder='templates')

busqueda_bp.route('/busqueda', methods=['GET'])(busquedaLibros)