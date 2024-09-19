#lista: armazena varios valores(Em python é permitido multiplos tipos de dados)
l = [2, 3, "abacate", [1, 3, 5], 9.8]
print(l[2])
#2 é o indice, sendo que a lista começa em 0
print(l[3][2])
#printa o número 3, pois é uma lista dentro de uma lista
l[3] = "oi"
#pode alterar as estrututra
"""operações: 
len: tmanho da lista; 
min: menor valor da lista; 
max: maior valor da lista: 
sum: retorna a soma dos valores da lista; 
append: adiciona um item no final da lista; 
extend: coloca uma lista no fim da lista; 
del/remove: remove um elemento da lista pelo indice; 
in: pertence(condicional); 
sort: coloca em ordem crescente; 
reverse: inverte os elementos; 
count: ve se tem numeros repetidos; 
index: mostra oindice do valor"""
list = list(range(5))#lista até o 4


#tuplas: são imutáveis
tupla = (1,2, "davi", 9.5, True)
a,b,c,d,e = tupla
#empacotamento e desempacotamento

dicionario = {"comida": "arroz", "feijão": True}
print(dicionario["feijão"])