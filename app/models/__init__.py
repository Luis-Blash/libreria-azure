import pymssql

def connBase():
    server='ashanty.southcentralus.cloudapp.azure.com'
    user='sa'
    password='TeseEq01'
    try:
        conn = pymssql.connect(server, user, password, "biblioteca")
    except:
        print("Fallo")
    return conn

from .libroModels import LibroModels
from .ejemplarModels import EjemplarModels
