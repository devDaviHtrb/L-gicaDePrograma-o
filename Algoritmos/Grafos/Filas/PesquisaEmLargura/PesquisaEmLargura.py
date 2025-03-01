from collections import deque
#Crio um grafo onde os vertices são dicionários, o que abre possibilidades para objetos também
grafo = {}
grafo["eu"] = [{"Nome":"Marcos", "Gamer":"Não"},{"Nome":"Matheus", "Gamer":"Não"}, {"Nome":"Maria", "Gamer":"Não"}]
grafo['Marcos'] = [{"Nome":"Claudio", "Gamer":"Sim"}]
grafo["Matheus"] = []
grafo["Maria"] = []

def encontraGamer():
    #Crio uma fila
    filaPesquisa = deque()
    #adiciono a fila todos os meus vizinhos
    filaPesquisa +=  grafo["eu"]
    verificado = []
    while filaPesquisa:
        #Pego o primeiro vizinho
        pessoa = filaPesquisa.popleft()
        #escolhi usar o atributo nome para que não fosse necessário verificar se todo um dicionário é igual, mas se fosse um objeto seria possivel apenas adicionar seu endereço
        if not pessoa["Nome"] in verificado:
            #se a pessoa for gamer
            if pessoa["Gamer"] == "Sim":
                return print(f"{pessoa['Nome']} é gamer")
            else:
                #adiciona a lista de verificados o nome da pessoa
                verificado.append(pessoa["Nome"])
                #Adiciona a lista de pesquisa todos os vizinhos da pessoa
                filaPesquisa +=  grafo[pessoa["Nome"]]
encontraGamer()
            
        