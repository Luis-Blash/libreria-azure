from . import connBase

conn = connBase()
cursor = conn.cursor(as_dict=True)

class EjemplarModels:
    
    def getTodosEjemplares(self):

        q = """SELECT ID_Ejemplar, ISBN 
        FROM Ejemplar
        """
        cursor.execute(q)
        datos = []
        for d in cursor:
            datos.append(d)

        return datos