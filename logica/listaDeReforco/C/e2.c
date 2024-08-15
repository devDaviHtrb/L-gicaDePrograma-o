#include <stdio.h>

int main()
{
    int a, b, c;
    printf("Digite o valor A\n");
    scanf("%d", &a);
    printf("Digite o valor B\n");
    scanf("%d", &b);
    printf("Digite o valor C\n");
    scanf("%d", &c);
    if (a < 0 || b < 0 || c < 0)
    {
        printf("Os valores são negativos");
    }
    else
    {
        if (a != b && b != c && c != a)
        {
            if (a < b && a < c)
            {
                printf("%d", a);
            }
            else
            {
                if (c < b && c < a)
                {
                    printf("%d", c);
                }
                else
                {
                    if (b < a && b < c)
                    {
                        printf("%d", b);
                    }
                }
            }
        }
        else
        {
            if (a == b && b < c)
            {
                printf("A e igual a B e valem %d", a);
            }
            else
            {
                if (a == c && b > c)
                {
                    printf("A e igual a B e valem %d", a);
                }
                else
                {
                    if (b == c && a > c)
                    {
                        printf("C e igual a B e valem %d", b);
                    }
                    else
                    {
                        if(a==b && b==c){
                            printf("Os valores sao iguais e valem %d", a);
                        }
                        
                    }
                }
            }
        }
    }
}

