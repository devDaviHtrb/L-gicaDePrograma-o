#include <stdio.h>
#include <math.h>
void eq(int a, int b, int c){
    float delta = b*b -(4*a*c);
    if (delta >= 0){
        float x1 = (((-b + pow(delta, 1/2))/(2*a))*-1);
        float x2 =  (((-b - pow(delta, 1/2))/(2*a))*-1);
        printf("x1 =  %.2f e x2 = %.2f", x1, x2);
    }else{printf("Conjunto solução vazio");} 
       
    }
int main(){
   eq(1, 4, 4);
   return 0;
}
