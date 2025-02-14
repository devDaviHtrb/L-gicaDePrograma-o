#Pilha  de chamadas é um conceito ligado a recursividade, quando uma função é chamada dentro de outra é criada uma pilha onde as variáveis alocadas para a 1° função fica na base e a outra no topo, quando a segunda é executada ela é retirada do topo e assim por diante

def Oi(nome):
    #A função oi e o nome são alocados na base da pilha
    print(f"Olá {nome}!!!")
    #A função Oi2 é alocada no topo da pilha enquanto a função Oi é pausada parcialmente completa
    Oi2(nome)
    #A função Oi2 é retirada de cima da pilha e a função Oi é finalizada
    return print(f"tchau {nome}")

def Oi2(nome):
    print(f"Como vai nome")