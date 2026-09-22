"""Implémentation de de l'héritage"""
from abc import ABC
from abc import abstractmethod
from multipledispatch import dispatch

class Habitant ( ABC ) :
    """Classe représentant un habitant du village"""
    def __init__(self, nom, age, adresse, animaux = None):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux

    def get_nom(self):
        """"Retourne le nom de l'habitant"""
        return self.__nom

    @property
    def age(self):
        """"Retourne l'age de l'habitant"""
        return self.__age

    @age.setter
    def age(self, age):
        """Modifie l'age de l'habitant en vérifiant qu'il reste entre 0 et 130"""
        if age not in range(0,131):
            raise ValueError("L'âge doit être compris entre 0 et 130")
        else:
            self.__age = age

    def get_adresse(self):
        """Retourne l'adresse de l'habitant"""
        return self.__adresse

    def get_animaux(self):
        """Retourne le dictionnaire des animaux de l'habitant"""
        return self.__animaux

    def set_nom(self, nom):
        """Modifie le nom de l'habitant"""
        self.__nom = nom

    def set_adresse(self, adresse):
        """Modifie l'dresse de l'habitant"""
        self.__adresse = adresse

    def set_animaux(self, animaux):
        """Modifie le dictionnaire des animaux de l'habitant"""
        self.__animaux = animaux

    @dispatch(str)
    def set_info(self, nom):
        """Modifie le nom de l'habitant"""
        self.__nom = nom

    @dispatch(str, int)
    def set_info(self, nom, age):
        """Modifie le nom et l'age de l'habitant"""
        self.__nom = nom
        self.__age = age

    def affichage_adresse(self):
        """Affiche le nom et l'adresse de l'habitant"""
        print(self.get_nom() + " habite a " + self.get_adresse())

    def compte_animal(self, animal):
        """Retourne le nombre d'animaux de type animal que posséde l'habitant"""
        if animal in self.get_animaux():
            return self.get_animaux()[animal]
        else :
            return 0

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        """Methode abstraite qui calcule le nombre d'année avant la retraite si c'est un adulte et 
        renvoie une erreur si c'est un enfant"""
        pass

