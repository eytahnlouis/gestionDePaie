# TiTannn
from datetime import date, datetime, timedelta as td
import time
class Employee(): # classe parent
    n = 1
    def __init__(self, nom, prenom, jourNaissance, moisNaissance, anneeNaissance):
        self.nom:str = nom
        self.prenom:str = prenom
        self.jourNaissance = jourNaissance # jour de naissance
        self.moisNaissance = moisNaissance
        self.anneeNaissance = anneeNaissance
        self.age:int =  time.localtime().tm_year - self.anneeNaissance

            
    def definirIdentifiant(self):
        
        self.identifiant = int(str(self.jourNaissance) + str(self.moisNaissance) + str(self.anneeNaissance) + str(self.n) )
        self.n += 1
        return self.identifiant
    
    def display(self):
        ficheIdentite = {f"Nom: {self.nom}\nPrénom: {self.prenom}\nDate de naissance: {self.jourNaissance}/{self.moisNaissance}/{self.anneeNaissance}\nAge: {self.age} identifiant: {self.identifiant}"}
        return ficheIdentite

class Salarie(Employee): # classe enfant
    def __init__(self, nom, prenom, jourNaissance, moisNaissance, anneeNaissance, salaireHoraire):
        Employee.__init__(self, nom, prenom, jourNaissance, moisNaissance, anneeNaissance)
        self.salaireHoraire = salaireHoraire

    def pointageDebut(self): # méthode pour pointer le début de travail
        print("Pointage de début")
        dateHeure = datetime.now()
        debut = dateHeure.strftime("%H:%M:%S")
        return debut

    def pointageFin(self): # méthode pour pointer la fin de travail
        print("Pointage de fin")
        dateHeure = datetime.now()
        fin = dateHeure.strftime("%H:%M:%S")
        return fin

    def calculHoraire(self): # méthode pour calculer le temps de travail
        jourTravaille = 0
        travailJournalier = td()
        print("Calcul horaire")
        format_heure = "%H:%M:%S"
        debut = self.pointageDebut()
        fin = self.pointageFin()
        tempsTravail = datetime.strptime(fin, format_heure) - datetime.strptime(debut, format_heure)

        travailJournalier += tempsTravail
        travailHebdo = 0
        r = []
        jourTravaille = 0
        if tempsTravail:
            jourTravaille += 1

        for i in range(jourTravaille):
            travailHebdo += travailJournalier
        
        for j in range(4):
            r.append(travailHebdo.total_seconds()/3600)
        
        return travailJournalier, jourTravaille, r
    
    def calculSalaire(self): # méthode pour calculer le salaire journalier
        # print("Calcul salaire")
        tempsTravail = self.calculHoraire()[0]
        salaire = int(tempsTravail.total_seconds()/3600) * self.salaireHoraire # salaire de base
        if tempsTravail > td(hours=8):
            salaire += (tempsTravail - td(hours=8)) * self.salaireHoraire * 1.34
        return salaire
    
    def salaireBrut(self): # méthode pour calculer le salaire brut
        salaireBrut = 0
        salaireBrut += self.calculSalaire()
        return salaireBrut
    
    def chargesSalariales(self): # méthode pour calculer les charges salariales
        salaireBrut = self.salaireBrut()
        assuranceMaladie = salaireBrut * 0.02
        assuranceVieillesse = salaireBrut * 0.06
        retraitesComplementaires = salaireBrut * 0.03
        assuranceChomage = salaireBrut * 0.024
        contributionFormation = salaireBrut * 0.01
        contributionSolidarite = salaireBrut * 0.0025
        chargesSalariales = assuranceMaladie + assuranceVieillesse + retraitesComplementaires + assuranceChomage + contributionFormation + contributionSolidarite
        return [chargesSalariales, assuranceMaladie, assuranceVieillesse, retraitesComplementaires, assuranceChomage, contributionFormation, contributionSolidarite] # retourne une liste des charges salariales
    
    def chargesPatronales(self): # méthode pour calculer les charges patronales
        salaireBrut = self.salaireBrut()
        assuranceMaladie = salaireBrut * 0.13
        assuranceVieillesse = salaireBrut * 0.36
        retraitesComplementaires = salaireBrut * 0.05
        assuranceChomage = salaireBrut * 0.04
        contributionFormation = salaireBrut * 0.01
        chargesPatronales = assuranceMaladie + assuranceVieillesse + retraitesComplementaires + assuranceChomage + contributionFormation
        return [chargesPatronales, assuranceMaladie, assuranceVieillesse, retraitesComplementaires, assuranceChomage, contributionFormation]
    
    def salaireNet(self): # méthode pour calculer le salaire net
        salaireBrut = self.salaireBrut()
        chargesSalariales = self.chargesSalariales()
        chargesPatronales = self.chargesPatronales()
        salaireNet = salaireBrut - (chargesSalariales + chargesPatronales) # salaire net = salaire brut - (charges salariales + charges patronales)
        return salaireNet

    def displaySalaire(self):
        feuille = {"identifiant": self.identifiant, "salaire": self.salaireHoraire, "salaire net": self.salaireNet, "salaire brut": self.salaireBrut, "jour travaillés": self.calculHoraire()[1], "charges salariales": self.chargesSalariales(), "charges patronales": self.chargesPatronales()}
        print(feuille)
        return feuille