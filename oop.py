
class Chien():
    """
    class qui represente la catégorie animale "chien"
    """
    nombre_pattes = 4 

    def __init__(self, nom, couleur, sexe, nbre_pattes):  # constructeur de la class
        self.nom = nom
        self.couleur = couleur
        self.sexe =  sexe
        self.nbre_pattes = nbre_pattes

    def courir(self):
        print(f"{self.nom} se deplace ")

    def aboyer(self):
         print( f"{self.nom} haw haw ")

    def manger(self):
        print(f"{self.nom}mange")

ch1 = Chien("REX", "Noir", "M" , 4)
ch2 = Chien("RED", "Rouge", "M" , 4)
ch2 = Chien("ALEXA", "Blanc", "F" , 4)
