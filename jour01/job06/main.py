class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def setlongueur(self, longueur):
        self.__longueur = longueur
        return self.__longueur
    
    def setlargeur(self, largeur):
        self.__largeur = largeur
        return self.__largeur
    
rectangle = Rectangle(10, 5)

print(rectangle.setlongueur(14))
print(rectangle.setlargeur(7))
      