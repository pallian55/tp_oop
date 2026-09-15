"""Classe de test"""
import unittest

def recalibrer(liste_releve, capteur, valeur):
    """reconstruit la liste des relevés avec la nouvelle valeur pour le capteur concerné"""
    new_liste = []
    for i in liste_releve :
        if i[0] == capteur :
            new_tuple = (capteur,valeur,i[2])
            new_liste.append(new_tuple)
        else :
            new_liste.append(i)
    return new_liste

class TestJournalDeBord(unittest.TestCase):
	"""Tests pour les fonctions sur les relevés (tuples)."""
	
	def test_recalibrer_capteur_existant(self):
		releve1 = ("laser_avant", 2.35, "m")
		releve2 = ("laser_arriere", 1.10, "m")
		releve3 = ("gyroscope", 87.5, "deg")
		releves = [releve1, releve2, releve3]
		nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
		assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
		assert nouveaux_releves[1] == releve2
		assert nouveaux_releves[2] == releve3
	
	def test_recalibrer_capteur_absent(self):
		"""Cas limite : le capteur demande n’existe pas."""
		releve1 = ("laser_avant", 2.35, "m")
		releve2 = ("laser_arriere", 1.10, "m")
		releve3 = ("gyroscope", 87.5, "deg")
		releves = [releve1, releve2, releve3]
		nouveaux_releves = recalibrer(releves, "micro", 2.40)
		assert nouveaux_releves[0] == ("laser_avant", 2.35, "m")
		assert nouveaux_releves[1] == releve2
		assert nouveaux_releves[2] == releve3

robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

def robots_double_mission(set_explo, set_trans) :
    """Permet de savoir quels robots peuvent faire les deux missions"""
    ret = set()
    len_explo = len(set_explo)
    len_trans = len(set_trans)
    if len_explo>=len_trans :
        for i in set_explo :
            if i in set_trans :
                ret.add(i)
    else :
        for i in set_trans :
            if i in set_explo :
                ret.add(i)
    return ret

def ajouter_robot_mission(ensemble, nom) :
    """Crée un nouvel avec le nouveau robot dedans sans modifier celui passé en argument"""
    ret = set()
    for i in ensemble :
        ret.add(i)
    ret.add(nom)
    return ret

class TestFlottesRobots(unittest.TestCase):
	"""Tests Pour les fonctions sur les ensembles"""

	def test_robots_double_mission(self):
		double_mission = robots_double_mission(robots_exploration, robots_transport)
		assert double_mission == {"R5", "R7"}
	
	def test_robots_double_mission_même_ensemble(self):
		double_mission = robots_double_mission(robots_exploration, robots_exploration)
		assert double_mission == robots_exploration
	
	def test_ajouter_robot_mission(self):
		ajout = ajouter_robot_mission(robots_exploration, "R8")
		assert ajout == {"R2", "R5", "R7", "R8"}
		# L’ensemble d’origine ne doit pas avoir été modifié
		assert robots_transport == {"R5", "R9", "R7", "R3"}
	
	def test_ajouter_robot_mission_deja_la(self):
		ajout = ajouter_robot_mission(robots_exploration, "R7")
		assert robots_exploration == {"R2", "R5", "R7"}

if __name__ == "__main__":
	unittest.main(verbosity=2)