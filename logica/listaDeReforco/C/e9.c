#include <stdio.h>

int main(){
    int op;
    char ops[5][40] = {"depósito", "saque", "extrato", "transferencia", "Encerrando operações"};
    printf("---------------\n Banco IFSP\n ---------------\n 1. depósito\n 2. saque\n 3. extrato \n 4. transferencia \n---------------\n 5 = encerrar\n---------------\n Sua escolha:\n");
    scanf("%d", &op);
    if(op == 5){
        printf("%s", ops[op-1]);
    }else{
        printf("Operacao de %s", ops[op-1]);
    }
}