#include <stdio.h>
#include <stdlib.h>

int main(){
    int erros;
    erros = rand() % 100;
    if(erros == 0 || erros > 1){
        printf("Foram detectados %d erros", erros);
    }else{
        printf("Foi detectado 1 erro");
    }
}