def soma(arr):
    if arr == []:
        return 0
    else:
        return arr.pop(0)+soma(arr)

#Caso base: array Vazio
#Caso recursivo array com ao menos um item
#se o array estiver vazio ele retorna zero, se não ele remove o 1° item do array e o soma com o novo primeiro item até que o caso recursivo seja o caso base

def ContaItens(arr):
    if arr == []:
        return 0
    else:
        return  1 + ContaItens(arr[1:])

def AchaMaior(arr):
    #No topo da pilha valor mais alto é retornado
    if len(arr)==2:
        return arr[0] if arr[0]>arr[1] else arr[1]
    #Caso o array tenha mais de um elemento, ou seja, não esteja no topo da pilha, seu valor será dado pelo sgundo return
    sub = AchaMaior(arr[1:])#adiciona 1 elemento de cada vez se pensarmos de trás pra frente
    return sub if arr[0]< sub else arr[0]
print(AchaMaior([0,23,21]))
