lista = []
lista2 = ["isósceles", "equilatero", "escaleno"]
tipo = 0
for n in range(1, 4):
    lista.append(float(input(f"Digite o valor do lado {n} ")))
if lista[0]+lista[1] > lista[2] and lista[2]+lista[1] > lista[0] and lista[0]+lista[2] > lista[1]:
    for i in range(0, 3):
        for a in range (0,3):
            if lista[i] == lista[a]:
                tipo = tipo + 1/2
    tipo = int(tipo) - 2
    print(f"o triângulo é {lista2[tipo]}")
else: 
  print("triângulo inválido\n")