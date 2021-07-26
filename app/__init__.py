from flask import Flask
from flask.templating import render_template

def create_app():
    app = Flask(__name__)

    from .routes.libros_bp import libro_bp
    from .routes.busqueda_bp import busqueda_bp


    @app.route('/')
    def index():
        return render_template('index.html')

    app.register_blueprint(libro_bp, url_prefix='/')
    app.register_blueprint(busqueda_bp, url_prefix='/')

    
    return app