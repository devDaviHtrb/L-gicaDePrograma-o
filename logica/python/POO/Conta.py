import datetime
class Banco:
    def __init__(self):
        self.contas = []
        self.clientes = []
    def criarCliente(self, classe, saldo, classe2, nome, numero, rg, cpf):
        conta = self.criarConta(saldo, classe2, numero)
        self.clientes.append(classe(conta), nome, cpf, rg )
        self.contas.append(conta)
    def criarConta( saldo, classe, numero):
        return classe(saldo, numero)
    def exibirClientes(self):
        for cliente in self.clientes:
            print(cliente.nome)

class cliente:
    def __init__(self, conta, nome, cpf, rg):
        self.conta = conta
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

class historico:
    def __init__(self):
        self.Abertura = datetime.datetime.today()
        self.transacoes = []
    
    def exibir(self):
       for transacao in self.transacoes:
           print(f"Data:{ transacao['Data'] }\n Tipo:{transacao['Tipo']}\n Valor:{transacao['valor']}\n")

class Conta:
    def __init__(self, saldo, numero):
        self.saldo = saldo
        self.numero = numero
        self.hist = historico()
    
    def deposita(self, valor):
        self.saldo += valor
        self.hist.transacoes.append({"Data":datetime.date.today(), "Tipo": "Depósito", "valor": valor})
    def saca(self, valor):
        if valor <= self.saldo: 
            self.saldo -= valor
            self.hist.transacoes.append({"Data":datetime.date.today(), "Tipo": "Saque", "valor": valor})
            return True
        else:
            return False
        
    def transfere(self, remetente, valor, bancodeDados):
        for conta in range(0, len(bancodeDados)):
            if bancodeDados[conta].numero == remetente:
                if(self.saca(valor)):
                    bancodeDados[conta].deposita(valor)
                    self.hist.transacoes.append({"Data":datetime.date.today(), "Tipo": "Transferencia", "valor": valor})
                    return print("Transferencia realizada com sucesso")
                else:
                    return print("Erro na transferencia, saldo insuficiente"), print("Não houveram alterações em seu saldo")
            if conta == len(bancodeDados)-1 and bancodeDados[conta].numero != remetente:
                return print("Conta inexistente"), print("Não houveram alterações em seu saldo")
    pass


banco = Banco()

        






