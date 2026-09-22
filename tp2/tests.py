"""Test sur les classes crées précedemment"""
import unittest

from habitant_decorateur import Habitant
from village import Village

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


class TestVillage(unittest.TestCase):
    """Tests des relations de composition et d'agregation d'un village."""

    def test_ajouter_habitant_composition(self):
        """Verifie que la composition cree et ajoute un habitant."""
        village = Village("PyTown")

        village.ajouter_habitant_composition("Alice", 30, "Rue A")

        habitants = village.get_habitants()
        self.assertEqual(len(habitants), 1)
        self.assertIsInstance(habitants[0], Habitant)
        self.assertEqual(habitants[0].get_nom(), "Alice")

    def test_ajouter_habitant_agregation_dans_deux_villages(self):
        """Verifie qu'un meme habitant peut appartenir a deux villages."""
        premier_village = Village("PyTown")
        second_village = Village("VillageVoisin")
        habitant = Habitant("Elise", 28, "Rue B")

        premier_village.ajouter_habitant_agregation(habitant)
        second_village.ajouter_habitant_agregation(habitant)

        self.assertIn(habitant, premier_village.get_habitants())
        self.assertIn(habitant, second_village.get_habitants())
        self.assertIs(premier_village.get_habitants()[0], habitant)
        self.assertIs(second_village.get_habitants()[0], habitant)

if __name__ == "__main__":
    unittest.main(verbosity=2)
