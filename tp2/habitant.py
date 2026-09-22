"""Implémentation de la classe habitant"""
class Habitant :
    """Classe représentant un habitant du village"""
    def __init__(self, nom, age, adresse, animaux = None):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.animaux = animaux

    def affichage_adresse(self):
        """Affiche le nom et l'adresse de l'habitant"""
        print(self.nom + " habite a " + self.adresse)

    def compte_animal(self, animal):
        """Retourne le nombre d'animaux de type animal que posséde l'habitant"""
        if animal in self.animaux:
            return self.animaux[animal]
        else :
            return 0

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"
