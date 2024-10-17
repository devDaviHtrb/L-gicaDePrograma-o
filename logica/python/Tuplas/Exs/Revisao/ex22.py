def primo(num):
    contador = 2
    while contador < num/2:
        if num%contador == 0:
            return print("Não é primo")
        contador +=1
    return print("é primo")
primo(int(input("Digite um número qualquer")))