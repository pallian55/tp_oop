"""Implémentation de la classe habitant"""
class Habitant :
    """Classe représentant un habitant du village"""
    def __init__(self, nom, age, adresse, animaux = None):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.animaux = animaux
