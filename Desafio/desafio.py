class Jogador:
    def __init__(self):
        self.nome = input("Digite seu nome:\n")
        self.pontuacao = int(input("Digite sua pontuação:\n"))
        if self.pontuacao >=500:
            print("você passou de nível")
        else:
            print(f"Faltam {500- self.pontuacao} para você passar de nível")
            while self.pontuacao <500:
                if input("Deseja aumentar a pontuação? S/N").upper() == "S":
                    self.aumentaponto()
            print("Passou de nível")
    def aumentaponto(self):
        self.pontuacao+=50
        print(f"sua pontuação atual é {self.pontuacao} e faltam  {500- self.pontuacao} para você passar de nível")
Okimura = Jogador()