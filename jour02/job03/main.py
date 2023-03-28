class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, valeur):
        self.__longueur = valeur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, valeur):
        self.__largeur = valeur

    def périmètre(self):
        return (self.__longueur * 2) + (self.__largeur * 2)
        
    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur
    
    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, valeur):
        self.__hauteur = valeur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur

mon_parallelepipede = Parallelepipede(5, 6, 7)

print("Périmètre:", mon_parallelepipede.périmètre())
print("Surface:", mon_parallelepipede.surface())
print("Volume:", mon_parallelepipede.volume())
