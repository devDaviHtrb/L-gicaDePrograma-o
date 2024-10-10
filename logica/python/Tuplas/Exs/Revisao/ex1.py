
lista = [[],[]]#celsius, Fahrenhaint
while True:
    temp = float(input("Digite a temperatura: \n"))
    if input("Digite a unidade de temperatura: C/F\n").upper() == "C":
        lista[0].append(temp)
    else:
        lista[1].append(temp)
    if input("Continuar a adicionar: S/N\n").upper() == "N":
        break
def tempconvert():
    for t in lista[0]:
            print(f"{t} graus celsius são equivalentes a {t*9/5+32} graus Fahrenheint")
    for h in lista[1]:
            print(f"{h} graus Fahrenheints são equivalentes a {(h-32)*5/9} graus Celsius") 
tempconvert()


