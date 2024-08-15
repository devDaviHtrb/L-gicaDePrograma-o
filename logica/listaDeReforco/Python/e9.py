print("---------------\n Banco IFSP\n ---------------\n 1. depósito\n 2. saque\n 3. extrato \n 4. transferencia \n---------------\n E = encerrar\n---------------\n Sua escolha: ")
escolha = input()
resp = ["depósito", "saque", "extrato", "transferencia", "Encerrando operações"]
if escolha == "1" or escolha =="2" or escolha =="3" or escolha =="4":
    print(f"Operação de {resp[int(escolha)-1]}")
else:
    escolha.capitalize()
    if escolha != "E":
        print("Encerrando operações")