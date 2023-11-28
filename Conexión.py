##Práctica 5:
##Creación de un conector a nuestra base de datos usando Python como lenguaje.
##Ampliar las funcionalidades del conector con respecto a lo que hago en la práctica.
import subprocess

class SalvaHdb:
    def __init__(self,basededatos):
        self.basededatos = basededatos
    def insert_file(self,coleccion,documento,contenido):
        self.operacion = "insert_file"
        self.coleccion = coleccion
        self.documento = documento
        self.contenido = contenido
        comando = '"C:\\Users\\salva\\Documents\\GitHub2\\salvaHdb\\salvaHdb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+' "'+self.contenido+'"'
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

        if resultado.returncode == 0:
            return("OK")
        else:
            return("KO")

Conexion1 = SalvaHdb("pruebas")
Conexion1.insert_file("libros","comedia","monólogo1")
