#include <stdio.h>

int main()
{
    int a, b, c;
    printf("escreva o valor do lado A");
    scanf("%d", &a);
    printf("escreva o valor do lado B");
    scanf("%d", &b);
    printf("escreva o valor do lado C");
    scanf("%d", &c);
    if(a*a+b*b==c*c||a*a+c*c==b*b||c*c+b*b==a*a){
        printf("O triangulo e retangulo");
    }else{
        printf("o triangulo não e retangulo");
    }
}