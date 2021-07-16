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
        LibroModels('',titulo,genero,ejemplar).inserLibro()
        return redirect(url_for('libro_bp.todolosLibros'))
        
    return render_template('libros/subirLibro.html',ejemplar=datos)

def actualizar_bibloteca(id):
    datos = LibroModels(id).getUnLibro()

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        genero = request.form.get('genero')
        LibroModels(id,titulo,genero).updateLibro()
        return redirect(url_for('libro_bp.todolosLibros'))
        
    return render_template('libros/updateLibro.html',datos=datos)

def deleteLibro(id):
    datos = LibroModels(id).getUnLibro()
    if request.method == 'POST':
        LibroModels(id).deleteLibro()
        return redirect(url_for('libro_bp.todolosLibros'))
    return render_template('libros/deleteLibro.html', datos=datos)