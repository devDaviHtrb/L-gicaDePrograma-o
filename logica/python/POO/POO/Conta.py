import datetime

class historico:
    def __init__(self):
        self.Abertura = datetime.datetime.today()
        self.transacoes = []
    
    def exibir(self):
       for transacao in self.transacoes:
           print(f"Data:{ transacao['Data'] }\n Tipo:{transacao['Tipo']}\n Valor:{transacao['valor']}\n")

class Conta:
    def __init__(self, saldo, numero):
        self.__saldo = saldo
        self.numero = numero
        self.hist = historico()
    def getSaldo(self):
        return self.__saldo
    def set_saldo(self, saldo):
         self.__saldo = saldo
    def deposita(self, valor):
        self.set_saldo(self.getSaldo()+valor) 
        self.hist.transacoes.append({"Data":datetime.date.today(), "Tipo": "Depósito", "valor": valor})
    def saca(self, valor):
        if valor <= self.getSaldo(): 
            self.set_saldo(self.getSaldo()-valor)
            self.hist.transacoes.append({"Data":datetime.date.today(), "Tipo": "Saque", "valor": valor})
            return True
        else:
            return False
        
    def transfere(self, remetente, valor, bancodeDados):
        for conta in range(0, len(bancodeDados)):
            if bancodeDados[conta].numero == remetente:
                if(self.saca(valor)):
                    bancodeDados[conta].deposita(valor)
                    self.hist.transacoes.pop()
                    self.hist.transacoes.append({"Data":datetime.date.today(), "Tipo": "Transferencia", "valor": valor})
                    return print("Transferencia realizada com sucesso")
                else:
                    return print("Erro na transferencia, saldo insuficiente"), print("Não houveram alterações em seu saldo")
            if conta == len(bancodeDados)-1 and bancodeDados[conta].numero != remetente:
                return print("Conta inexistente"), print("Não houveram alterações em seu saldo")
    pass
conta1 = Conta(12200, "121232")
conta2 = Conta(0, "32432")
contas = [conta1, conta2]
conta1.transfere("32432", 122, contas )
conta2.deposita(1223)
conta2.saca(12)
conta2.hist.exibir()
conta1.hist.exibir()





        






