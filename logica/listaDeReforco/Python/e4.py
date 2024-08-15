mes = int(input("digite o número do mês: "))
meses = ["janeiro", "fevereiro", "março", "agosto", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
if mes<0 or mes>12:
    print("número inválido")
    mes = int(input("digite o número do mês: "))
print(f"o mês é {meses[mes-1]}")
