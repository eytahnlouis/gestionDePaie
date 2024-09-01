import unittest
from datetime import timedelta
from your_module import calculer_temps_travail

class TestCalculerTempsTravail(unittest.TestCase):
    def test_calculer_temps_travail(self):
        heure_arrivee = "09:00"
        heure_depart = "17:00"
        pause = timedelta(hours=1)
        expected_output = timedelta(hours=7)
        self.assertEqual(calculer_temps_travail(heure_arrivee, heure_depart, pause), expected_output)

    def test_calculer_temps_travail_with_no_pause(self):
        heure_arrivee = "09:00"
        heure_depart = "17:00"
        expected_output = timedelta(hours=8)
        self.assertEqual(calculer_temps_travail(heure_arrivee, heure_depart), expected_output)

    def test_calculer_temps_travail_with_custom_pause(self):
        heure_arrivee = "09:00"
        heure_depart = "17:00"
        pause = timedelta(minutes=30)
        expected_output = timedelta(hours=7, minutes=30)
        self.assertEqual(calculer_temps_travail(heure_arrivee, heure_depart, pause), expected_output)

if __name__ == '__main__':
    unittest.main()