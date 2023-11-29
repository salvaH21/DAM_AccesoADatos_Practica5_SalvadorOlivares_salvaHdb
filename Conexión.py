##Práctica 5:
##Creación de un conector a nuestra base de datos usando Python como lenguaje.
##Ampliar las funcionalidades del conector con respecto a lo que hago en la práctica.
from salvaHdb_conector import SalvaHdb


Conexion1 = SalvaHdb("pruebas")
#Conexion1.insert_file("carpeta","prueba1","hola salva")
#Conexion1.insert_text("carpeta","prueba1","tercera prueba")
#Conexion1.remove_file("pelis","prueba1")
#Conexion1.create_collection("carpeta")
#Conexion1.remove_collection("pelis")
Conexion1.select("carpeta","prueba2")
