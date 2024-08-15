#include <stdio.h>
#include <stdlib.h>
int main()
{
    float saldo;
    printf("digite seu saldo em reais: R$");
    scanf("%f", &saldo);
    if (saldo == 1000)
    {
        printf("Voce tem um desconto de 20 por cento na tarifa");
    }
    else
    {
        if (saldo == 3000)
        {
            printf("Voce tem um desconto de 45 por cento na tarifa");
        }
        else
        {
            if (saldo == 5000)
            {
                printf("Voce tem um desconto de 50 por cento na tarifa");
            }
        }
    }
}