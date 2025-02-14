class listaOrdenada:
    def __init__(self, arrDesordenado):
        self.arrayOrdenado = list()
        self.array = arrDesordenado
#verifica se um item é menor que todos os outros da lista e retorna seu index
    def achaMenor(self):
        menor = self.array[0]
        for item in self.array:
            if item < menor:
                menor = item
        return self.array.index(menor)

    def ordenaLista(self):
        for item in range(len(self.array)):
#para o tamanho da lista é trasferido para nova lista o menor item da lista desordenada
            self.arrayOrdenado.append(self.array[self.achaMenor()])
            self.array.pop(self.achaMenor())
        return self.arrayOrdenado
lista = [0, 2, 4, 1, 4, 6, 9]
print(listaOrdenada(lista).ordenaLista())