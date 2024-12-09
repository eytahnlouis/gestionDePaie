from wageApp import Employee as emp
import sqlite3
import tkinter as tk
from tkinter import Tk, Label, Entry, Button, messagebox

def enregistrer_employe(employe_id, nom, prenom, jour_naissance, mois_naissance, annee_naissance, salaire_horaire):
    conn = sqlite3.connect("pointages.db")
    cursor = conn.cursor() # Création d'un curseur

    # Insérer l'employé
    cursor.execute('''
        INSERT INTO employes (employe_id, nom, prenom, jour_naissance, mois_naissance, annee_naissance, salaire_horaire)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (employe_id, nom, prenom, jour_naissance, mois_naissance, annee_naissance, salaire_horaire))

    conn.commit()
    conn.close()

class PointeuseApp:
    # Classe pour créer l'interface graphiquef
    def __init__(self, root):
        self.root = root
        self.root.title("Pointeuse")
        self.root.geometry("400x650")

        self.label = Label(self.root, text="Pointeuse", font=("Arial", 20)) 
        self.label.pack(pady=10)

        self.label_nom = Label(self.root, text="Nom:")  # Nom de l'employé
        self.label_nom.pack(pady=10)

        self.entry_nom = Entry(self.root)
        self.entry_nom.pack(pady=10)

        self.label_prenom = Label(self.root, text="Prénom:")    # Prénom de l'employé
        self.label_prenom.pack(pady=10)

        self.entry_prenom = Entry(self.root)
        self.entry_prenom.pack(pady=10)

        self.label_jour = Label(self.root, text="Jour de naissance:")   # Jour de naissance
        self.label_jour.pack(pady=10)

        self.entry_jour = Entry(self.root)
        self.entry_jour.pack(pady=10)

        self.label_mois = Label(self.root, text="Mois de naissance:")   # Mois de naissance
        self.label_mois.pack(pady=10)

        self.entry_mois = Entry(self.root)
        self.entry_mois.pack(pady=10)

        self.label_annee = Label(self.root, text="Année de naissance:")  # Année de naissance
        self.label_annee.pack(pady=10)

        self.entry_annee = Entry(self.root)
        self.entry_annee.pack(pady=10)

        self.label_salaire = Label(self.root, text="Salaire horaire:")  # Salaire horaire
        self.label_salaire.pack(pady=10)

        self.entry_salaire = Entry(self.root)
        self.entry_salaire.pack(pady=10)

        self.button = Button(self.root, text="Enregistrer", command=self.enregistrer)
        self.button.pack(pady=10)

    def enregistrer(self):
        nom = str(self.entry_nom.get())
        prenom = str(self.entry_prenom.get())
        jour_naissance = int(self.entry_jour.get())
        mois_naissance = int(self.entry_mois.get())
        annee_naissance = int(self.entry_annee.get())
        salaire_horaire = float(self.entry_salaire.get())
        employe = emp(nom, prenom, jour_naissance, mois_naissance, annee_naissance)    # Création d'un employé
        employe_id = employe.definirIdentifiant()

        try:
            enregistrer_employe(employe_id, nom, prenom, jour_naissance, mois_naissance, annee_naissance, salaire_horaire)
            messagebox.showinfo("Succès", "Employé enregistré avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

if __name__ == "__main__":

    root = Tk()
    app = PointeuseApp(root)
    root.mainloop()