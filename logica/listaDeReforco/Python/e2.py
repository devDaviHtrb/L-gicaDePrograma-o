lista = []
for n in range(0, 3):
    lista.append(int(input(f"Digite o valor {n+1}: ")))
lista.sort()
if lista[0] <0 or lista[1]<0 or lista[2]<0:
  print("valores negativos")
else:
  for n in range (1, 3):
    for i in range(1, 3):
      if n!=i:
        if lista[n] == lista[i]:
         print(f"{lista[n]} = {lista[i]}")
print(f"O menor valor é {lista[0]}")
