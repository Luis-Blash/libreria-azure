import pymssql

def connBase():
    server='ashanty.southcentralus.cloudapp.azure.com'
    user='sa'
    password='TeseEq01'
    try:
        conn = pymssql.connect(server, user, password, "biblioteca")
    except UnboundLocalError:
        return "Not found connection"
    return conn

from .libroModels import LibroModels
from .ejemplarModels import EjemplarModels
