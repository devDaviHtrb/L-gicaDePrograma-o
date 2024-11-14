class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir(self):
        print(f"{self.nome}\n {self.idade}")
pessoa1 = Pessoa("Claudia", 23)
pessoa2 = Pessoa("Davi", 15)
pessoa1.exibir()
pessoa2.exibir()
