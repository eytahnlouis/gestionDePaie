import unittest
from wageApp import Employee, Salarie

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Doe", "John", 1, 1, 1990)

    def test_displayEmployee(self):
        expected_output = "nom: Doe, prenom: John, date de naissance: 1/1/1990, age: 31"
        self.assertEqual(self.employee.displayEmployee(), expected_output)

    def test_definirIdentifiant(self):
        expected_output = "Identifiant: 10119901"
        self.assertEqual(self.employee.definirIdentifiant(), expected_output)

class TestSalarie(unittest.TestCase):
    def setUp(self):
        self.salarie = Salarie("Doe", "John", 1, 1, 1990, 10)

    def test_displaySalarie(self):
        expected_output = "identifiant: 10119901, salaire: 10"
        self.assertEqual(self.salarie.displaySalarie(), expected_output)

    def test_pointageDebut(self):
        expected_output = "Pointage de début"
        self.assertEqual(self.salarie.pointageDebut(), expected_output)

    def test_pointageFin(self):
        expected_output = "Pointage de fin"
        # self.assertEqual(self.salarie.pointageFin(), expected_output)
    def test_calculHoraire(self):
        expected_output = (8, 1)
        self.assertEqual(self.salarie.calculHoraire(), expected_output)

    def test_calculSalaire(self):
        expected_output = 80
        self.assertEqual(self.salarie.calculSalaire(), expected_output)

    def test_salaireBrut(self):
        expected_output = 80
        self.assertEqual(self.salarie.salaireBrut(), expected_output)

    def test_chargesSalariales(self):
        expected_output = 0.2
        self.assertEqual(self.salarie.chargesSalariales(), expected_output)

    def test_chargesPatronales(self):
        expected_output = 0.55
        self.assertEqual(self.salarie.chargesPatronales(), expected_output)

    def test_salaireNet(self):
        expected_output = 79.25
        self.assertEqual(self.salarie.salaireNet(), expected_output)

    def test_displaySalaire(self):
        expected_output = "identifiant: 10119901, salaire: 10, salaire net: 79.25"
        self.assertEqual(self.salarie.displaySalaire(), expected_output)

if __name__ == '__main__':
    unittest.main()
import unittest
from datetime import datetime
from wageApp import Employee, Salarie

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Doe", "John", 1, 1, 1990)

    def test_displayEmployee(self):
        expected_output = "nom: Doe, prenom: John, date de naissance: 1/1/1990, age: 31"
        self.assertEqual(self.employee.displayEmployee(), expected_output)

    def test_definirIdentifiant(self):
        expected_output = "Identifiant: 10119901"
        self.assertEqual(self.employee.definirIdentifiant(), expected_output)

class TestSalarie(unittest.TestCase):
    def setUp(self):
        self.salarie = Salarie("Doe", "John", 1, 1, 1990, 10)

    def test_displaySalarie(self):
        expected_output = "identifiant: 10119901, salaire: 10"
        self.assertEqual(self.salarie.displaySalarie(), expected_output)

    def test_pointageDebut(self):
        expected_output = "Pointage de début"
        self.assertEqual(self.salarie.pointageDebut(), expected_output)

    def test_pointageFin(self):
        expected_output = "Pointage de fin"
        self.assertEqual(self.salarie.pointageFin(), expected_output)

    def test_calculHoraire(self):
        expected_output = (8, 1)
        self.assertEqual(self.salarie.calculHoraire(), expected_output)

    def test_calculSalaire(self):
        expected_output = 80
        self.assertEqual(self.salarie.calculSalaire(), expected_output)

    def test_salaireBrut(self):
        expected_output = 80
        self.assertEqual(self.salarie.salaireBrut(), expected_output)

    def test_chargesSalariales(self):
        expected_output = 0.2
        self.assertEqual(self.salarie.chargesSalariales(), expected_output)

    def test_chargesPatronales(self):
        expected_output = 0.55
        self.assertEqual(self.salarie.chargesPatronales(), expected_output)

    def test_salaireNet(self):
        expected_output = 79.25
        self.assertEqual(self.salarie.salaireNet(), expected_output)

    def test_displaySalaire(self):
        expected_output = "identifiant: 10119901, salaire: 10, salaire net: 79.25"
        self.assertEqual(self.salarie.displaySalaire(), expected_output)

if __name__ == '__main__':
    unittest.main()