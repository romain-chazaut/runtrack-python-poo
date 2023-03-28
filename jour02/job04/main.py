class Forme:
    def __init__(self):
        pass
    
    def aire(self, aire=0):
        self.aire = aire
        return aire

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur        
        
    def aire(self):
        return self.largeur * self.hauteur        

aire_rectangle = Rectangle(6, 7)
aire = aire_rectangle.aire()
print("Aire du rectangle:", aire)





