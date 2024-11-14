class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibir(self):
        print(f"{self.marca}\n{self.modelo}\n{self.ano}")
carro1 = Carro("Ford", "NSei", "2133")
carro1.exibir()