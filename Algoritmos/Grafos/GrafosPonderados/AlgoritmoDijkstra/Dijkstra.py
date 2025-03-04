grafo = {}
grafo["Inicio"] = {}
#O vértice Inicio possui como vizinhos: a e b> A aresta Inicio -> a tem peso 6 enquanto a Início->b tem peso 2
grafo["Inicio"]["a"] = 6
grafo["Inicio"]["b"] = 2
grafo["a"] = {}
grafo["a"]["fim"] = 1
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5
grafo["fim"] = {}

infinito = float("inf")
#tabela de custos para se chegar até um vértice a partir do início
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

#tabela que armazena os pais(vértices que permitem chegar a outros com menos custo)
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def MaisBaixo(arr):
    valorMaisBaixo = infinito
    NodeMaisBarato = None
    for n in arr:
        if n not in processados:
            if arr[n]< valorMaisBaixo:
                valorMaisBaixo = arr[n]
                NodeMaisBarato = n
    return NodeMaisBarato

def Dijkstra():
    Node = MaisBaixo(custos)
    while Node != None:
        custoNode = custos[Node]
        vizinhos = grafo[Node]
        for n in vizinhos.keys():
            novoCusto = vizinhos[n] + custoNode
            if novoCusto< custos[n]:
                custos[n] =  novoCusto
                pais[n] = Node
        processados.append(Node)
        Node = MaisBaixo(custos)
Dijkstra()
print(pais)
