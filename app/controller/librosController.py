from flask import render_template, request, redirect, url_for
from werkzeug.utils import redirect
# models
from app.models import LibroModels, EjemplarModels


# Controllador

def todolosLibros():
    datos = LibroModels().getTodosLibros()
    return render_template('libros/todosloslibros.html', libros=datos)

def subir_bibloteca():
    datos = EjemplarModels().getTodosEjemplares()
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        genero = request.form.get('genero')
        ejemplar = request.form.get('ejemplar')
        LibroModels().inserLibro(titulo, genero, ejemplar)
        return redirect(url_for('libro_bp.todolosLibros'))
        
    return render_template('libros/subirLibro.html',ejemplar=datos)

def actualizar_bibloteca(id):
    datos = LibroModels().getUnLibro(id)

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        genero = request.form.get('genero')
        LibroModels().updateLibro(titulo,genero,id)
        return redirect(url_for('libro_bp.todolosLibros'))
        
    return render_template('libros/updateLibro.html',datos=datos)

def deleteLibro(id):
    if request.method == 'POST':
        LibroModels().deleteLibro(id)
        return redirect(url_for('libro_bp.todolosLibros'))
    return render_template('libros/deleteLibro.html')