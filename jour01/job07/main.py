class Livre:
    def __init__(self, auteur, nbre_pages, titre):
        self.__auteur = auteur
        self.__nbre_pages = nbre_pages
        self.__titre = titre

    def setnbre_pages(self, nbre_pages):
        if nbre_pages > 0:
            self.__nbre_pages = nbre_pages
        else:
            print("EROR")
        return self.__nbre_pages

     
    def setauteur(self, auteur):
        self.__auteur = auteur
        return self.__auteur
    
    def settitre(self, titre):
        self.__titre = titre
        return self.__titre
    
    
livre = Livre(177, "Michel gentil", "L'amour c'est beau")



print(livre.setnbre_pages(789))
print(livre.setauteur("Michel Pasgentil"))  
print(livre.settitre("L'Amour c'est nul"))      