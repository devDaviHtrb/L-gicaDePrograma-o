from random import *
lista = list()
for n in range(1000):
    lista.append(randint(0, 1000))
lista.sort()
print(lista)
#Cria uma lista aleatória e a ordena


#O It representa o indice mais alto no momento, enquanto o id o mais baixo
def PesquisaBinaria(lista, Item, It=len(lista)-1,  Id = 0):
#Verifica se o item existe e se deve continuar a pesquisa
    while It>=Id and Item in lista:
#Im representa o indice central em relação ao It e Id
        Im = int((It+Id)/2)
        chute = lista[Im]
        if chute == Item:
            return print(f"O item: {Item} está no index {lista.index(Item)} da lista")
        elif chute < Item:
#Caso o chute seja menor que o item o Id aumenta seu valor eliminando metade dos números
            Id = Im
        else:
#Elimina os numeros altos
            It = Im
    return print(None)
PesquisaBinaria(lista, int(input("Digite o número procurado: ")))
