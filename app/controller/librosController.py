from flask import render_template, request
# models
from app.models import LibroModels, EjemplarModels

def todolosLibros():
    datos = LibroModels().getTodosLibros()
    return render_template('libros/todosloslibros.html', libros=datos)

def subir_bibloteca():
    datos = EjemplarModels().getTodosEjemplares()
    titulo = request.form.get('titulo')
    ejemplar = request.form.get('ejemplar')
    print(ejemplar)
    return render_template('libros/subirLibro.html',ejemplar=datos)