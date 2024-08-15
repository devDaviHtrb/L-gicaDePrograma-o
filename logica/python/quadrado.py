n = int(input("digute um número e inteiro e direi a soma de seu quadrado com o dos seus: "))
soma = 0
for i in range(0, n+1, 1):
    print(f"{i}**2 = {i**2}")
    soma += i**2
