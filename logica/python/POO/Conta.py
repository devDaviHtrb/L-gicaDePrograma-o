class Conta:
    def __init__(self, saldo, proprietario, numero):
        self.saldo = saldo
        self.proprietario = proprietario
        self.numero = numero
    
    def deposita(self, valor):
        self.saldo += valor
    def saca(self, valor):
        if valor <= self.saldo: 
            self.saldo -= valor
            return True
        else:
            return False
        
    def transfere(self, remetente, valor, bancodeDados):
        for conta in range(0, len(bancodeDados)):
            if bancodeDados[conta].numero == remetente:
                if(self.saca(valor)):
                    bancodeDados[conta].deposita(valor)
                    return print("Transferencia realizada com sucesso"), print("Não houveram alterações em seu saldo")
                else:
                    return print("Erro na transferencia, saldo insuficiente"), print("Não houveram alterações em seu saldo")
            if conta == len(bancodeDados)-1 and bancodeDados[conta].numero != remetente:
                return print("Conta inexistente"), print("Não houveram alterações em seu saldo")
    pass

conta1 = Conta(1000, "Davi", "1421")
conta2 = Conta(1000, "Pedro", "1231")
contas = [conta1, conta2]
conta1.transfere("121", 122, contas)


