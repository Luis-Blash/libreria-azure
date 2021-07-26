from flask import render_template, request, redirect, url_for

from app.models import connBase
conn = connBase()
cursor = conn.cursor(as_dict=True)

def busquedaLibros():

    q = request.args.get('consulta')
    datos = []
    cursor.execute(f"""
    SELECT li.Titulo, li.Genero, ej.Autor, ej.Editorial, ej.Edicion
    FROM Libro li, Ejemplar ej
    WHERE li.ID_Ejemplar = ej.ID_Ejemplar AND li.Titulo LIKE '%{q}%'
    UNION ALL
    SELECT li.Titulo, li.Genero, ej.Autor, ej.Editorial, ej.Edicion
    FROM 
    [issac.southcentralus.cloudapp.azure.com].[biblioteca].[dbo].[Libro] li,
    [issac.southcentralus.cloudapp.azure.com].[biblioteca].[dbo].[Ejemplar] ej
    WHERE li.ID_Ejemplar = ej.ID_Ejemplar AND li.Titulo LIKE '%{q}%'
    """)
    for d in cursor:
        datos.append(d)
    return render_template('busqueda.html', libros=datos)