def contadorLetra(string):
    cont = {}
    for letra in string:
        cont[letra] = string.count(letra)
    print(cont)
contadorLetra(input("Digite uma palavra\n").replace(" ", ""))