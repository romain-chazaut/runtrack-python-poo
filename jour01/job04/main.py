class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis", self.nom, self.prenom)

Mon_nom = Personne("John","Doe")
Mon_nom2 = Personne("Jean", "Dupond")

Mon_nom.SePresenter()
Mon_nom2.SePresenter()

    
