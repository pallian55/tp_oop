"""Implementation de la classe Village"""
from habitant_decorateur import Habitant


class Village:
    """Classe représentant un village composé d'habitant"""
    def __init__(self, nom):
        self.nom = nom
        self.__habitants = []

    def get_habitants(self):
        """Retourne la liste des habitants du village"""
        return self.__habitants

    def ajouter_habitant_composition(self, nom, age, adresse, animaux = None):
        """Crée un nouvel objet Habitant et l'ajoute à la liste"""
        self.get_habitants().append(Habitant(nom, age, adresse, animaux))

    def ajouter_habitant_agregation(self, habitant):
        """Ajoute à la liste un objet habitant qui existe deja"""
        self.get_habitants().append(habitant)

    def afficher_habitants(self):
        """Affiche tous les habitants du village"""
        for i in self.get_habitants():
            i.affichage_adresse()

pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise)
# meme habitant dans 2 villages
assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()

#Question 3 : ajouter_habitant_composition illustre une relation de composition car le village crée
#lui même l'habitant, les deux objets sont dépendants, tandis que ajouter_habitant_agregation
#illustre une relation d'agregation car le village ajoute un habitants qui existe déjà,
#les deux objets sont donc indépendants et le même habitants peut être dans plusieurs village
