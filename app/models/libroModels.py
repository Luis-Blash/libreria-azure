from . import connBase

conn = connBase()
cursor = conn.cursor(as_dict=True)

class LibroModels:
    __id_libro = ''
    __genero = ''
    __id_ejemplar=''

    def inserLibro(self):
        pass
    
    def getTodosLibros(self):

        q = """SELECT Libro.Titulo, Libro.Genero, Ejemplar.Autor,
        Ejemplar.Editorial, Ejemplar.Edicion 
        FROM Libro
        INNER JOIN Ejemplar
        ON Libro.ID_Ejemplar=Ejemplar.ID_Ejemplar;
        """
        cursor.execute(q)
        datos = []
        for d in cursor:
            datos.append(d)

        return datos

