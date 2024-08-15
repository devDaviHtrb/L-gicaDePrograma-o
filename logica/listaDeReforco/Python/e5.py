lados = []
for n in range(0, 3):
    lados.append(int(input("Digite o valor do lado: ")))
    while(lados[n]<0):
        print("valor inválido")
        lados.append(int(input("Digite o valor do lado: ")))
lados.sort()
if lados[2]**2 == lados[0]**2+lados[1]**2:
    print("O triângulo é retângulo")
else:
    print("O triângulo não é retângulo")

