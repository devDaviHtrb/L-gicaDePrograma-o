lista =[]
for n in range(0, 3):
    lista.append(int(input("escreva um número")))
    lista[n] = lista[n]**2

if lista[2] < 3000:
    lista.sort()
    print(lista)