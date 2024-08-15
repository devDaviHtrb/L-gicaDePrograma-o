#include <stdio.h>


int main(){
    int n, q, i, s;
    printf("digite um numewro inteiro e direi a soma de seu quadrado com os do seus antecessores:\n");
    scanf("%d", &n);
    for(i= 0; i<=n; i++){
    	q = i*i;
        s += q;
    }
    printf("%d", s);

}