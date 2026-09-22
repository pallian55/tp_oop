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
