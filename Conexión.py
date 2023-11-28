##Práctica 5:
##Creación de un conector a nuestra base de datos usando Python como lenguaje.
##Ampliar las funcionalidades del conector con respecto a lo que hago en la práctica.
from salvaHdb_conector import SalvaHdb


Conexion1 = SalvaHdb("pruebas")
Conexion1.insert_file("libros","prueba","primera prueba")
Conexion1.insert_text("libros","prueba","segunda prueba")
