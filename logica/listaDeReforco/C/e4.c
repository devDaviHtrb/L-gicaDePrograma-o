#include <stdio.h>

int main(){
    char meses[30][12] = {"janeiro", "fevereiro", "março", "agosto", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"};
    int mes;
    printf("digite o numero do mes\n");
    scanf("%d", &mes);
    if( mes<0|| mes>12){
        printf("o numero e invalido\n");
        printf("digite o numero do mes");
        scanf("%d", &mes);
    }else{
        printf("o mes e %s", meses[mes-1]);
    }
}