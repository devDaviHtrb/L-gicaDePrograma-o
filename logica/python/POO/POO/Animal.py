class Animal:
    def som(self):
        return self.Som
    
class cachorro(Animal):
    def __init__(self):
        super().__init__()
        self.Som = "au"
class gato(Animal):
    def __init__(self):
        super().__init__()
        self.Som = "Miau"
Gato = gato()
print(Gato.som())
Cachorro = cachorro()
print(Cachorro.som())