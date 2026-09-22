"""Test sur les classes crées précedemment"""
import unittest

from habitant_decorateur import Habitant

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l’encapsulation."""
    def setUp(self):
        """Prepare un habitant reutilise par les differents tests."""
        self.habitant = Habitant("Lilian", 20, "Rue A", {"vaches": 3, "chiens": 1})

    def test_compte_animal_possede(self):
        """Verifie que le nombre d'animaux possédé est le bon"""
        self.assertEqual(self.habitant.compte_animal("vaches"), 3)

    def test_compte_animal_non_possede(self):
        """Verifie que zero est renvoye pour une espece absente."""
        self.assertEqual(self.habitant.compte_animal("moutons"), 0)

    def test_age_setter_valide(self):
        """Verifie qu'un age compris entre 0 et 130 est accepte."""
        self.habitant.age = 26
        self.assertEqual(self.habitant.age, 26)

    def test_age_setter_invalide(self):
        """Les ages inferieurs a 0 ou superieurs a 130 sont refuses."""
        with self.assertRaises(ValueError):
            self.habitant.age = -1

        with self.assertRaises(ValueError):
            self.habitant.age = 131

if __name__ == "__main__":
    unittest.main(verbosity=2)
