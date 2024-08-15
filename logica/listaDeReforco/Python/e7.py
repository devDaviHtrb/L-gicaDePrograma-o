from random import *
nota = random()
while nota>10 or nota<0:
  nota = random(0, 10)
if nota<6:
    if nota<3:
        print("Está de recuperação")
    else:
        print("Reprovado")
else:
    print("Aprovado")