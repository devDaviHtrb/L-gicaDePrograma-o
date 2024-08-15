from random import *
erros = randint(0, 256)
if erros == 0 or erros > 1:
    print(f"foram detectados {erros} erros")
else:
    print("Foi detectado 1 erro")