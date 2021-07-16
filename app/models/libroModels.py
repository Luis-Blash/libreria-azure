from . import connBase

conn = connBase()
cursor = conn.cursor(as_dict=True)

class LibroModels:
    __id_libro = ''
    __genero = ''
    __id_ejemplar=''

    def __getIdlibros(self):
        cursor.execute('SELECT Genero FROM Libro')
        id = 1
        for da in cursor:
            id = id + 1
        return id

    def inserLibro(self,titulo,genero,id_ejemplar): 
        id = self.__getIdlibros()
        sql = "INSERT INTO Libro (ID_Libro, Genero, Titulo, ID_Ejemplar) VALUES (%d,%s, %s,%d)"
        val = (id,titulo, genero,id_ejemplar)
        cursor.execute(sql, val)
        conn.commit()
        return "Listo"
    
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

