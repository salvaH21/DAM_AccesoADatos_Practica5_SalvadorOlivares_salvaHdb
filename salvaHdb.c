#include <stdio.h>
#include <string.h>

int main(int argc,char *argv[]){
    FILE *archivo;
    char *operacion = argv[1];
    char *basededatos = argv[2];
    char *coleccion = argv[3];
    /*
        Uso:
        jvdb.exe [operacion] [basededatos] [coleccion] [documento] [contenido]
    */
    if(strcmp(operacion,"select") == 0){
        char *documento = argv[4];
        char ruta[100];
        strcpy(ruta,"db/");
        strcat(ruta,basededatos);
        strcat(ruta,"/");
        strcat(ruta,coleccion);
        strcat(ruta,"/");
        strcat(ruta,documento);
        strcat(ruta,".json");
        archivo = fopen(ruta,"r");
        printf("te doy datos:\n");
        char linea[1024];
        while(fgets(linea,sizeof(linea),archivo) != NULL){
            printf("Linea: %s",linea);
        }
        fclose(archivo);
        
    }else if(strcmp(operacion,"insert_file") == 0){
        char *documento = argv[4];
        char ruta[100];
        strcpy(ruta,"db/");
        strcat(ruta,basededatos);
        strcat(ruta,"/");
        strcat(ruta,coleccion);
        strcat(ruta,"/");
        strcat(ruta,documento);
        strcat(ruta,".json");
        archivo = fopen(ruta,"w");
        char *texto = argv[5];
        fputs(strcat(texto,"\n"),archivo);
        fclose(archivo);
    }else if(strcmp(operacion,"insert_text") == 0){
        char *documento = argv[4];
        char ruta[100];
        strcpy(ruta,"db/");
        strcat(ruta,basededatos);
        strcat(ruta,"/");
        strcat(ruta,coleccion);
        strcat(ruta,"/");
        strcat(ruta,documento);
        strcat(ruta,".json");
        archivo = fopen(ruta,"a");
        char *texto = argv[5];
        fputs(strcat(texto,"\n"),archivo);
        fclose(archivo);
    }else if(strcmp(operacion,"remove_file") == 0){
        char *documento = argv[4];
        char ruta[100];
        strcpy(ruta,"db/");
        strcat(ruta,basededatos);
        strcat(ruta,"/");
        strcat(ruta,coleccion);
        strcat(ruta,"/");
        strcat(ruta,documento);
        strcat(ruta,".json");
        archivo = remove(ruta);
    }else if(strcmp(operacion,"create_collection") == 0){
        char rutacoleccion[100];
        strcpy(rutacoleccion,"db/");
        strcat(rutacoleccion,basededatos);
        strcat(rutacoleccion,"/");
        strcat(rutacoleccion,coleccion);
        printf(rutacoleccion);
        if(mkdir(rutacoleccion,0777) == 0){
            printf("Coleccion creada correctamente");
        }else{
            printf("No se ha podido crear");
        }
    }else if(strcmp(operacion,"remove_collection") == 0){
        char rutacoleccion[100];
        strcpy(rutacoleccion,"db/");
        strcat(rutacoleccion,basededatos);
        strcat(rutacoleccion,"/");
        strcat(rutacoleccion,coleccion);
        printf(rutacoleccion);
        if(rmdir(rutacoleccion,0777) == 0){
            printf("Coleccion borrada");
        }else{
            printf("No se ha podido borrar");
        }
    }else{
        printf("Operacion no valida");
    }
    
    return 0;
}