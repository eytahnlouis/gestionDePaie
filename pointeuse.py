import sqlite3
import tkinter as tk
from tkinter import Tk, Label, Entry, Button, messagebox
from datetime import datetime
from wageApp import Salarie as sal 

# ----------------------
# Création de la base de données
# ----------------------
def creer_base():
    conn = sqlite3.connect("pointages.db") # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    # Création de la table des pointages
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pointages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employe_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            heure_debut TEXT NOT NULL,
            heure_fin TEXT NOT NULL
        )
    ''')
    
    # Création de la table des employés (si besoin)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employes (
            employe_id INTEGER PRIMARY KEY,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            jour_naissance INTEGER NOT NULL,
            mois_naissance INTEGER NOT NULL,
            annee_naissance INTEGER NOT NULL,
            salaire_horaire FLOAT NOT NULL
            
        )
    ''')

    conn.commit()
    conn.close()

# ----------------------
# Enregistrement des pointages
# ----------------------
def enregistrer_pointage_debut(employe_id, date, heure_debut):
    conn = sqlite3.connect("pointages.db")
    cursor = conn.cursor() # Création d'un curseur

    # Vérifier si l'employé existe 
    cursor.execute("SELECT employe_id FROM employes WHERE employe_id = ?", (employe_id,))   # Requête SQL
    employe = cursor.fetchone() # Récupérer le résultat
    if employe is None:
        raise ValueError("L'employé avec cet ID n'existe pas dans la base de données.")

    # Insérer le pointage
    cursor.execute('''
        INSERT INTO pointages (employe_id, date, heure_debut, heure_fin)
        VALUES (?, ?, ?, '00:00:00')
    ''', (employe_id, date, heure_debut))

    conn.commit()
    conn.close()

def enregistrer_pointage_fin(employe_id, date, heure_fin):
    conn = sqlite3.connect("pointages.db")
    cursor = conn.cursor() # Création d'un curseur

    # Vérifier si l'employé existe 
    cursor.execute("SELECT employe_id FROM employes WHERE employe_id = ?", (employe_id,))   # Requête SQL
    employe = cursor.fetchone() # Récupérer le résultat
    if employe is None:
        raise ValueError("L'employé avec cet ID n'existe pas dans la base de données.")

    # Mettre à jour le pointage
    cursor.execute('''
        UPDATE pointages
        SET heure_fin = ?
        WHERE employe_id = ? AND date = ? AND heure_fin IS '00:00:00'
    ''', (heure_fin, employe_id, date))

    conn.commit()
    conn.close()

# ----------------------
# Interface graphique (GUI)
# ----------------------
class PointeuseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de Pointeuse")
        self.root.geometry("400x300")

        # Variables pour stocker les données
        self.employe_id_var = tk.StringVar()    # ID de l'employé
        self.pointage_en_cours = False
        self.heure_debut = None

        # Interface utilisateur
        self.creer_interface()

    def creer_interface(self) -> None:
        # Titre
        label_titre = Label(self.root, text="Système de Pointeuse", font=("Arial", 16, "bold"))
        label_titre.pack(pady=10)

        # Champ pour l'ID de l'employé
        label_id = Label(self.root, text="ID Employé :", font=("Arial", 12))
        label_id.pack(pady=5)
        self.entree_id = Entry(self.root, textvariable=self.employe_id_var, font=("Arial", 12), width=20)
        self.entree_id.pack(pady=5)

        # Bouton pour pointer (début)
        self.bouton_pointer = Button(self.root, text="Démarrer le pointage", font=("Arial", 12), bg="green", fg="black", command=self.gerer_pointage_debut)
        self.bouton_pointer.pack(pady=20)

        #Bouton pour pointer (fin)
        self.bouton_pointer_fin = Button(self.root, text="Terminer le pointage", font=("Arial", 12), bg="red", fg="black", command=self.gerer_pointage_fin)
        self.bouton_pointer_fin.pack(pady=30)

        # Label pour l'état actuel
        self.label_etat = Label(self.root, text="En attente...", font=("Arial", 12), fg="blue")
        self.label_etat.pack(pady=10)

    def gerer_pointage_debut(self) -> None:
        employe_id = self.employe_id_var.get() # Récupérer l'ID de l'employé
        test = sal(employe_id)

        if not employe_id:  # Vérifier si l'ID est vide
            messagebox.showerror("Erreur", "Veuillez entrer un ID Employé.")
            return

            # Commencer le pointage 
        pointage_debut = test.pointageDebut(employe_id)
        self.heure_debut = pointage_debut[0]
        date = pointage_debut[1]
        heure_debut_dt = datetime.strptime(self.heure_debut, '%H:%M:%S')
        self.label_etat.config(text=f"Pointage démarré à {heure_debut_dt.strftime('%H:%M:%S')}", fg="green")
        self.pointage_en_cours = True

            

            # Enregistrer dans la base de données
        try:    # Gestion des erreurs
            enregistrer_pointage_debut(int(employe_id), date, self.heure_debut)
            messagebox.showinfo("Succès", f"Pointage enregistré :\nDébut : {self.heure_debut}\n)")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")
            return

            # Réinitialiser l'interface
        self.label_etat.config(text="En attente...", fg="blue")
        self.pointage_en_cours = False
        self.heure_debut = None
        self.employe_id_var.set("") # Réinitialiser l'ID

    def gerer_pointage_fin(self) -> None:
        employe_id = self.employe_id_var.get()
        test = sal(employe_id)

        if not employe_id:  # Vérifier si l'ID est vide
            messagebox.showerror("Erreur", "Veuillez entrer un ID Employé.")
            return

            # Commencer le pointage
        pointage_fin = test.pointageFin(employe_id)
        self.heure_fin = pointage_fin[0]
        date = pointage_fin[1]
        heure_fin_dt = datetime.strptime(self.heure_fin, '%H:%M:%S')
        self.label_etat.config(text=f"Pointage terminé à {heure_fin_dt.strftime('%H:%M:%S')}", fg="green")
        self.bouton_pointer.config(text="Terminer le pointage", bg="red")
        self.pointage_en_cours = True

                    # Réinitialiser l'interface
        self.label_etat.config(text="En attente...", fg="blue")
        self.bouton_pointer.config(text="Démarrer le pointage", bg="green")
        self.pointage_en_cours = False
        self.heure_debut = None
        self.employe_id_var.set("") # Réinitialiser l'ID
    
        # Enregistrer dans la base de données

        try:    # Gestion des erreurs
            enregistrer_pointage_fin(int(employe_id), date, self.heure_fin)
            messagebox.showinfo("Succès", f"Pointage enregistré :\nFin : {self.heure_fin}\n)")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")
            return



# Point d'entrée principal
if __name__ == "__main__":
    creer_base()  # S'assurer que la base existe

    root = Tk()
    app = PointeuseApp(root)
    root.mainloop()
    
