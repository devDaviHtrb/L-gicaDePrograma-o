class Node:
    def __init__(self, item):
#cria um objeto novo com o endereço livre para alocar seu sucessor
        self.item = item
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        #primeiro item da lista
        self.primeiro = None

    def AdicionaItem(self, valor):
        novoNo = Node(valor)
        #Caso a lista não tenha nenhum item 
        if self.primeiro is None:
            self.primeiro = novoNo
            self.ItemAtual = self.primeiro
        else:
            #Se o ponteiro do item atual não estiver vazio, o item atual vira o do ponteiro
            if self.ItemAtual.prox != None:
                self.ItemAtual = self.ItemAtual.prox
            #aloca o novo nó para um ponteiro
            self.ItemAtual.prox = novoNo
    def Imprimir(self):
        item = self.primeiro
        while item.prox != None:
            print(item.item)
            item = item.prox

