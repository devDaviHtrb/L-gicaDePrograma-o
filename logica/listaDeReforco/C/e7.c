#include <stdio.h>
#include <stdlib.h>
int main(){
    int nota;
    nota = rand()% 10;
    if(nota>6){
        printf("Aprovado");
    }else{
        if(nota<3){
            printf("Reprovado");
        }else{
            printf("Esta de recuperacao");
        }
    }
}