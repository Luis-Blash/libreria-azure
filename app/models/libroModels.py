from . import connBase

conn = connBase()
cursor = conn.cursor(as_dict=True)

class LibroModels:
    __id_libro = ''
    __genero = ''
    __id_ejemplar=''

    def __getIdlibros(self):
        cursor.execute('SELECT ID_Libro FROM Libro')
        id = 0
        for da in cursor:
            id = int(da['ID_Libro']) + 1
        return id

    def getTodosLibros(self):

        q = """SELECT Libro.ID_Libro, Libro.Titulo, Libro.Genero, Ejemplar.Autor,
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
    
    def getUnLibro(self, id):
        cursor.execute(f'select Genero,Titulo FROM Libro WHERE ID_Libro={id};')
        datos = []
        for d in cursor:
            datos.append(d)
        return datos

    def inserLibro(self,titulo,genero,id_ejemplar): 
        id = self.__getIdlibros()
        sql = "INSERT INTO Libro (ID_Libro, Genero, Titulo, ID_Ejemplar) VALUES (%d,%s, %s,%d)"
        val = (id,titulo, genero,id_ejemplar)
        cursor.execute(sql, val)
        conn.commit()
        return "Listo"

    def updateLibro(self,titulo,genero,id):
        sql = "UPDATE Libro SET Titulo = %s ,Genero = %s WHERE ID_Libro = %d"
        val = (titulo,genero,id)
        cursor.execute(sql,val)
        conn.commit()
        return "Listo"

    def deleteLibro(self,id):
        sql = "DELETE FROM Libro WHERE ID_Libro = %d"
        val = (id,)
        cursor.execute(sql,val)
        conn.commit()
        return "listo"
