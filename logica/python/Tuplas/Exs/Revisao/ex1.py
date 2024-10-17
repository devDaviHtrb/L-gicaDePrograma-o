lista = [[],[]]#celsius, Fahrenhaint
while True:
    temp = input("Digite a temperatura no seguinte modelo(numero°F/°C): \n").upper().strip().replace("°", " ").split()
    if temp[1] == "C":
        lista[0].append(int(temp[0]))
    else:
        lista[1].append(int(temp[0]))
    if input("Continuar a adicionar: S/N\n").upper() == "N":
        break
def tempconvert():
    for t in lista[0]:
            print(f"{t} graus celsius são equivalentes a {t*9/5+32} graus Fahrenheint")
    for h in lista[1]:
            print(f"{h} graus Fahrenheints são equivalentes a {(h-32)*5/9} graus Celsius") 
tempconvert()