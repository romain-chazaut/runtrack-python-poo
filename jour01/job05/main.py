class Animal:
    def __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom

    def setvieillir(self, age_to_add):
        self.age += age_to_add
        print("L'age de l'animal", self.age)

    def setNom(self, nom_Animal):
        self.prenom = nom_Animal
        print("L'animal se nomme", self.prenom)

animal = Animal(0, "")

animal.setvieillir(6)
animal.setvieillir(8)
animal.setNom("michel")



