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

    def insert_text(self,coleccion,documento,contenido):
        self.operacion = "insert_text"
        self.coleccion = coleccion
        self.documento = documento
        self.contenido = contenido
        comando = '"C:\\Users\\salva\\Documents\\GitHub2\\salvaHdb\\salvaHdb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+' "'+self.contenido+'"'
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

        if resultado.returncode == 0:
            return("OK")
        else:
            return("KO")

    def remove_file(self,coleccion,documento):
        self.operacion = "remove_file"
        self.coleccion = coleccion
        self.documento = documento
        comando = '"C:\\Users\\salva\\Documents\\GitHub2\\salvaHdb\\salvaHdb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+''
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

        if resultado.returncode == 0:
            return("OK")
        else:
            return("KO")

    def create_collection(self,coleccion):
        self.operacion = "create_collection"
        self.coleccion = coleccion
        comando = '"C:\\Users\\salva\\Documents\\GitHub2\\salvaHdb\\salvaHdb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+''
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

        if resultado.returncode == 0:
            return("OK")
        else:
            return("KO")

    def remove_collection(self,coleccion):
        self.operacion = "remove_collection"
        self.coleccion = coleccion
        comando = '"C:\\Users\\salva\\Documents\\GitHub2\\salvaHdb\\salvaHdb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+''
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

        if resultado.returncode == 0:
            return("OK")
        else:
            return("KO")

    def select(self,coleccion,documento):
        self.operacion = "select"
        self.coleccion = coleccion
        self.documento = documento
        comando = '"C:\\Users\\salva\\Documents\\GitHub2\\salvaHdb\\salvaHdb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+''
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

        if resultado.returncode == 0:
            print("OK")
            archivo = open((documento+".json"),"r")
            print(archivo.read())
        else:
            return("KO")


##select
