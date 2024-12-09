from datetime import date, datetime, timedelta as td, time
from typing import List, Tuple
class Employee:  # classe parent
    _counter = 1  # compteur global pour les identifiants

    def __init__(self, nom, prenom, jourNaissance, moisNaissance, anneeNaissance, salaireHoraire):
        self.nom: str = nom
        self.prenom: str = prenom
        self.jourNaissance = jourNaissance  # jour de naissance
        self.moisNaissance = moisNaissance
        self.anneeNaissance = anneeNaissance
        self.identifiant: int = self.definirIdentifiant(jourNaissance, moisNaissance, anneeNaissance)
        self.salaireHoraire: float = float(salaireHoraire)

    def definirIdentifiant(jourNaissance, moisNaissance, anneeNaissance) -> int:
        identifiant = int(f"{jourNaissance}{moisNaissance}{anneeNaissance}{Employee._counter}")
        Employee._counter += 1
        return identifiant

    def display(self) -> dict:
        ficheIdentite = {
            "Nom": self.nom,
            "Prénom": self.prenom,
            "Date de naissance": f"{self.jourNaissance}/{self.moisNaissance}/{self.anneeNaissance}",
            "Identifiant": self.identifiant,
            "SalaireHoraire": self.salaireHoraire,
        }
        return ficheIdentite


class Salarie(Employee):  # classe enfant

    def __init__(self, identifiant):
        # super().__init__(nom, prenom, jourNaissance, moisNaissance, anneeNaissance, salaireHoraire)
        self.debut = None
        self.fin = None
        self.debut_nuit = None
        self.fin_nuit = None
        self.identifiant = identifiant

    def pointageDebut(self, identifiant):  # méthode pour pointer le début de travail

        if not self.identifiant:    # Vérifier si l'employé a un identifiant
            raise ValueError("L'employé n'a pas d'identifiant.")

        date_heure = datetime.now()
        self.debut = date_heure.strftime("%H:%M:%S")
        heure = date_heure.time()
        date = date_heure.strftime("%Y-%m-%d")

        if time(22, 0, 0) <= heure or heure <= time(6, 0, 0):
            self.debut_nuit = self.debut
        
        return self.debut or self.debut_nuit if self.debut_nuit else self.debut , date


    def pointageFin(self, identifiant):  # méthode pour pointer la fin de travail

        if not self.identifiant:    # Vérifier si l'employé a un identifiant
            raise ValueError("L'employé n'a pas d'identifiant.")

        date_heure = datetime.now() # Récupérer la date et l'heure actuelles
        self.fin = date_heure.strftime("%H:%M:%S")
        heure = date_heure.time()   # Récupérer l'heure actuelle

        if time(22, 0, 0) <= heure or heure <= time(6, 0, 0):
            self.fin_nuit = self.fin
        
        return self.fin or self.fin_nuit if self.fin_nuit else self.fin, date_heure.strftime("%Y-%m-%d")


    def calculHoraire(self):  # méthode pour calculer le temps de travail
        if not self.debut or not self.fin:
            raise ValueError("Les heures de début et de fin doivent être renseignées.")

        format_heure = "%H:%M:%S"
        debut = datetime.strptime(self.debut, format_heure)
        fin = datetime.strptime(self.fin, format_heure)

        if fin < debut:  # Gestion du passage à minuit
            fin += td(days=1)  # Ajoute un jour

        tempsTravail = fin - debut
        return tempsTravail

    def calculHoraireNuit(self):    # méthode pour calculer le temps de travail de nuit
        if not self.debut_nuit or not self.fin_nuit:
            return td()  # Aucun travail de nuit enregistré

        format_heure = "%H:%M:%S"
        debut_nuit = datetime.strptime(self.debut_nuit, format_heure)
        fin_nuit = datetime.strptime(self.fin_nuit, format_heure)

        if fin_nuit < debut_nuit:  # Gestion du passage à minuit
            fin_nuit += td(days=1)

        travailNuit = fin_nuit - debut_nuit
        return travailNuit

