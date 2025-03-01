def Qsort(arr):
    if len(arr)<2:
       return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo] 
        maiores = [i for i in arr[1:] if i > pivo] 
        return Qsort(menores)+[pivo]+Qsort(maiores)
print(Qsort([0,43,2,1,5,23,3,8]))
