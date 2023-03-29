class Vehicule:
    def __init__(self, modele, marque, année, prix):
        self.modele = modele
        self.marque = marque
        self.année = année
        self.prix = prix

    def informationVehicule(self, modele, marque, année, prix):
        self.modele = modele
        self.marque = marque
        self.année = année
        self.prix = prix
        return Vehicule
    
    def demarrer():
        print("Attention, je roule.")
    
class Voiture(Vehicule):
    def __init__(self, modele, marque, année, prix, portes=4):
        self.modele = modele
        self.marque = marque
        self.année = année
        self.prix = prix
        self.portes = portes

    def informationVehicule(self, modele, marque, année, prix, portes):
        self.modele = modele
        self.marque = marque
        self.année = année
        self.prix = prix
        self.portes = portes
        print(Voiture)



class Moto(Vehicule):
    
    def __init__(self, modele, marque, année, prix, portes, roue=2):
         self.modele = modele
         self.marque = marque
         self.année = année
         self.prix = prix
         self.portes = portes
         self.roue = roue

    def demarrer():
        print("Vas-y Roule!!")


voiture = Voiture("Class A", "Mercedes", "2020", "18500", 4)
print("Informations sur la voiture :")
print("Marque :", voiture.marque)
print("Modèle :", voiture.modele)
print("Année :", voiture.année)
print("Prix :", voiture.prix)
print("Nombre de portes :", voiture.portes)
Voiture.demarrer()

moto = Moto("1200 Vmax", "Yamaha", "1987", "4500", 2)
print("Informations sur la moto :")
print("Marque :", moto.marque)
print("Modèle :", moto.modele)
print("Année :", moto.année)
print("Prix :", moto.prix)
print("Nombre de roues :", moto.roue)
Moto.demarrer()



    
        