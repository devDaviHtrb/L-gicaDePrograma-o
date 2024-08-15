#include <stdio.h>

int main()
{
    int a, b, c;
    printf("escreva um numero");
    scanf("%d", &a);
    printf("escreva um numero");
    scanf("%d", &b);
    printf("escreva um numero");
    scanf("%d", &c);
    a = a*a;
    b=b*b;
    c=c*c;
    if (c>3000){
        return 0;
    }else{
        printf("%d. %d, %d", a, b, c);
    }
}