lista = []#celsius, Fahrenhaint
while True:
    lista.append(input("Digite a temperatura no seguinte modelo(numero°F/°C): \n").upper().strip().replace("°", " ").split())
    if input("Continuar a adicionar: S/N\n").upper() == "N": break
def tempconvert():
    for n in lista:print(f"{n[0]}°C são equivalentes a {int(n[0])*9/5+32}°F") if n[1]== "C" else print(f"{n[0]}°F são equivalentes a {(int(n[0])-32)*5/9}°C") 
tempconvert()