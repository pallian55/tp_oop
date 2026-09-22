"""Implémentation de de l'héritage"""
from abc import ABC
from abc import abstractmethod
from multipledispatch import dispatch

class Habitant ( ABC ) :
    """Classe représentant un habitant du village"""
    def __init__(self, nom, prenom, age, adresse):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__adresse = adresse

    def __str__(self):
        """Permet d'imprimer les infos sur un habitant"""
        return self.__prenom + " " + self.__nom + ", " + str(self.__age) + " ans, habite a " + self.__adresse

    def get_nom(self):
        """"Retourne le nom de l'habitant"""
        return self.__nom

    def get_prenom(self):
        """Retourne le prenom de l'habitant"""
        return self.__prenom

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

    def set_nom(self, nom):
        """Modifie le nom de l'habitant"""
        self.__nom = nom

    def set_prenom(self, prenom):
        """Modifie le prenom de l'habitant"""
        self.__prenom = prenom

    def set_adresse(self, adresse):
        """Modifie l'dresse de l'habitant"""
        self.__adresse = adresse

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

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        """Methode abstraite qui calcule le nombre d'année avant la retraite si c'est un adulte et 
        renvoie une erreur si c'est un enfant"""
        pass

class Adulte(Habitant):
    """classe héritant d'habitant qui représente un adulte"""
    def __init__(self, nom, prenom, age, adresse):
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans")
        else:
            super().__init__(nom, prenom, age, adresse)

    def calcul_nombre_annee_avant_retraite(self):
        if self.age >= 62:
            return "Deja a la retraite"
        else:
            return 62 - self.age

class Enfant(Habitant):
    """Classe eritant d'Habitant representant un enfant"""
    def __init__(self, nom, prenom, age, adresse):
        if age >=18:
            raise ValueError("Un enfant doit avoir moins de 18 ans")
        else:
            super().__init__(nom, prenom, age, adresse)

    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur: un enfant ne peut pas calculer sa retraite"

def affichage(h : Habitant):
    """Imprime un habitant peu importe son type"""
    print(str(h))

adulte = Adulte("Dupont", "Marie", 35, "Rue A")
enfant = Enfant("Martin", "Lucas", 12, "Rue B")
assert isinstance(adulte, Habitant)
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()
try:
    Enfant("Oups", "prenom", 25, "Rue C")
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass
print(adulte)
affichage(adulte)
affichage(enfant)
