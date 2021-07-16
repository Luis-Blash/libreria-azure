from flask import render_template, request
# models
from app.models import LibroModels, EjemplarModels

def todolosLibros():
    datos = LibroModels().getTodosLibros()
    return render_template('libros/todosloslibros.html', libros=datos)

def subir_bibloteca():
    datos = EjemplarModels().getTodosEjemplares()
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        genero = request.form.get('genero')
        ejemplar = request.form.get('ejemplar')
        insertar = LibroModels().inserLibro(titulo, genero, ejemplar)
        
    return render_template('libros/subirLibro.html',ejemplar=datos)