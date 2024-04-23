#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int * p;
    long memadd;

    if(argc!=2){
	printf("Cantidad de argumentos invalidos!\n");
        printf("El uso correcto es:\n");
	printf("./punteros MEMAddress\n");
	printf("Donde MEMAddress es una direccion de memoria\n");
	exit(100);
    }else{
	memadd = atol(argv[1]); 
    }
    printf("%ld \n", memadd);
    p = (int*)(memadd);

    printf("DirMem: %p \n", p);
    printf("Contenido: %d \n\n", *p);
}
