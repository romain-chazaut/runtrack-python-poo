class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("J'ai", self.age, "ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

# Instanciation d'une personne avec l'âge par défaut de 14 ans
personne1 = Personne()
# Instanciation d'un élève avec l'âge par défaut de 14 ans
eleve1 = Eleve()
eleve1.affichageAge() # affichera "J'ai 14 ans" dans la console
