##Práctica 5:
##Creación de un conector a nuestra base de datos usando Python como lenguaje.
##Ampliar las funcionalidades del conector con respecto a lo que hago en la práctica.
import subprocess

comando = '"C:\\Users\\salva\\Documents\\GitHub2\\salvaHdb\\salvaHdb.exe" insert_file pruebas libros aventuras "la isla del tesoro"'
resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

if resultado.returncode == 0:
    print("OK")
else:
    print("KO")
