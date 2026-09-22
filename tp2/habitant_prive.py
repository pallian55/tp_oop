"""Implémentation de la classe habitant"""
class Habitant :
    """Classe représentant un habitant du village"""
    def __init__(self, nom, age, adresse, animaux = None):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux

    def get_nom(self):
        """"Retourne le nom de l'habitant"""
        return self.__nom

    def get_age(self):
        """"Retourne l'age de l'habitant"""
        return self.__age

    def get_adresse(self):
        """Retourne l'adresse de l'habitant"""
        return self.__adresse

    def get_animaux(self):
        """Retourne le dictionnaire des animaux de l'habitant"""
        return self.__animaux

    def set_nom(self, nom):
        """Modifie le nom de l'habitant"""
        self.__nom = nom

    def set_age(self, age):
        """Modifie l'age de l'habitant"""
        self.__age = age

    def set_adresse(self, adresse):
        """Modifie l'dresse de l'habitant"""
        self.__adresse = adresse

    def set_animaux(self, animaux):
        """Modifie le dictionnaire des animaux de l'habitant"""
        self.__animaux = animaux

    def affichage_adresse(self):
        """Affiche le nom et l'adresse de l'habitant"""
        print(self.get_nom() + " habite a " + self.get_adresse())

    def compte_animal(self, animal):
        """Retourne le nombre d'animaux de type animal que posséde l'habitant"""
        if animal in self.get_animaux():
            return self.get_animaux()[animal]
        else :
            return 0

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.get_nom() == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"
