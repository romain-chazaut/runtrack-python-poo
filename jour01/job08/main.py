class Livre:
    def __init__(self, auteur, nbre_pages, titre, disponible):
        self.__auteur = auteur
        self.__nbre_pages = nbre_pages
        self.__titre = titre
        self.__disponible = disponible
        disponible = True

    def setnbre_pages(self, nbre_pages):
        if nbre_pages > 0:
            self.__nbre_pages = nbre_pages
        else:
            print("ERROR")
        return self.__nbre_pages

     
    def setauteur(self, auteur):
        self.__auteur = auteur
        return self.__auteur
    
    def settitre(self, titre):
        self.__titre = titre
        return self.__titre
    
    def setverifiquation(self, disponible):
        if disponible == True:
            self.__disponible = disponible
        if disponible == False:
            return self.__disponible
        
    def setemprunter(self, disponible):
        if disponible == False:
            self.__disponible = disponible
            print("Indisponible")
        else:
            print("disponible")
        
    
    
livre = Livre(177, "Michel gentil", "L'amour c'est beau", disponible = True)



print(livre.setnbre_pages(789))
print(livre.setauteur("Michel Pasgentil"))  
print(livre.settitre("L'Amour c'est nul"))      
print(livre.setverifiquation(True))
print(livre.setemprunter(False))