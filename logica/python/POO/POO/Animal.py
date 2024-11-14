class Animal:
    def som():
        return "som"
    
class cachorro(Animal):
    def som(self):
        return "au"
class gato(Animal):
    def som(self):
        return "miau"
Gato = gato()
print(Gato.som())
Cachorro = cachorro()
print(Cachorro.som())