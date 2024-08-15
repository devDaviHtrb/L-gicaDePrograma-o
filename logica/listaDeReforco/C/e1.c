#include <stdio.h>

int main(){
    int a,b;
    printf("Digite o valor A\n");
    scanf("%d", &a);
    printf("Digite o valor B\n");
    scanf("%d", &b);
    if(a>b){
        printf("%d, %d", b, a);
    }else{
        printf("%d, %d", a, b);
    };
}