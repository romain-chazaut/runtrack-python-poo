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

    def bonjour(self):
        print("Bonjour")

class Professeur:
    def __init__(self, age=30, matiereEnseignee="Français"):
        self.age = age
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

    def modifierAge(self, age):
        self.age = age

    def bonjour(self):
        print("Bonjour")

eleve1 = Eleve(age=15)
eleve1.bonjour()
eleve1.allerEnCours()

professeur1 = Professeur(age=40)
professeur1.bonjour()
professeur1.enseigner()
