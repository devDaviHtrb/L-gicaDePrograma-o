#include <stdio.h>

void main(){
    float A, B, C;
    printf("digite o valor do lado A \n");
    scanf("%f", &A);
    printf("digite o valor do lado B \n");
    scanf("%f", &B);
    printf("digite o valor do lado C \n");
    scanf("%f", &C);
    if(A+B > C && A+C>B&& B+C>A){
        if(A==B && B==C){
            printf("O triangulo e equilatero");
        }else{
            if(A != B && A != C && C!=B){
                printf("O triangulo e escaleno");
            }else{
                if(A==B && A!=C || A==C && A!=B || B==C && B != A){
                    printf("O triangulo e isósceles");
                }
            }
        }
    }else{
        printf("triangulo invalido");
    };
  
}