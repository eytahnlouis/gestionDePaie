from convertisseurSalaire import recuperer_donnees, calculer_salaire, demande_salaire
from fpdf import FPDF
import sqlite3
from tkinter import Button
def creationSalaire() -> None:
    conn = sqlite3.connect("pointages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT employe_id, nom, prenom FROM employes")
    employes = cursor.fetchall()
    conn.close()

    for employe in employes:    # Parcourir les employés
        employe_id = employe[0]     # Récupérer l'ID de l'employé
        nom = employe[1]
        prenom = employe[2]
        resultat = recuperer_donnees(employe_id)
        employe_id, salaire, duree_heures = calculer_salaire(resultat)
        demande_salaire(employe_id)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        pdf.cell(200, 10, txt = "Salaire de l'employé " + str(nom) + " "+ str(prenom), ln = True, align = 'C') # Titre
        pdf.cell(200, 10, txt = "ID de l'employé: " + str(employe_id), ln = True, align = 'L')      # ID de l'employé
        pdf.cell(200, 10, txt = "Salaire: " + str(salaire), ln = True, align = 'L')
        pdf.cell(200, 10, txt = "Heures travaillées: " + str(duree_heures), ln = True, align = 'L')
        pdf.output("salaire_employe_" + str(employe_id) + "-" + str(nom) + "-" + str(prenom) + ".pdf")
        print("Le salaire de l'employé a été enregistré dans le fichier salaire_employe_" + str(prenom) + "_" + str(nom) + ".pdf.")
    print("Tous les salaires ont été enregistrés.")
    return None

class PointeuseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crées les salaires en un bouton")
        self.root.geometry("400x300")

        self.Button = Button(self.root, text="Créer les salaires", command=creationSalaire)

if __name__ == "__main__":
    creationSalaire()
    print("Le programme a terminé l'enregistrement des salaires.")
    print("Merci d'avoir utilisé notre programme.")
    print("Au revoir !")