import math

class Forme:
    def __init__(self):
        pass
    
    def aire(self, aire=0):
        self.aire = aire
        return aire
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
       
    
    def aire(self):
        rayon = 5
        return math.pi * self.radius **2
    
aire_cercle = Cercle(6)
aire = aire_cercle.aire()
print("Aire du cercle:", aire) 