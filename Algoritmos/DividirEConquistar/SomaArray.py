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
    if len(arr)==1:
        return arr[0]
    else:
        if arr[0]> arr[1]:
            del(arr[1])
        else:
            del(arr[0])
        return AchaMaior(arr)
print(AchaMaior([0,23,12,3,21]))
