import sqlite3
from datetime import date, datetime, timedelta as td, time
 
def recuperer_donnees(employe_id: str) -> list:        # Fonction pour récupérer les données des pointages

    # Obtenir le mois et l'année du mois précédent
    aujourd_hui = date.today()    # Récupérer la date actuelle
    mois_precedent = aujourd_hui.month - 1 if aujourd_hui.month > 1 else 12
    annee_precedente = aujourd_hui.year if aujourd_hui.month > 1 else aujourd_hui.year - 1

    # Format du mois précédent pour la requête SQL (format YYYY-MM)
    mois_precedent_str = f"{annee_precedente}-{mois_precedent:02}"
    conn = sqlite3.connect("pointages.db")
    cursor = conn.cursor()  # Création d'un curseur

# Requête SQL pour récupérer les pointages du mois précédent

    cursor.execute("""
        SELECT * 
        FROM pointages 
        WHERE strftime('%Y-%m', date) = ? AND employe_id = ?;    
        """, (mois_precedent_str , employe_id))
    resultat = cursor.fetchall()    # Récupérer les résultats de la requête
    conn.close()
    return resultat

def calculer_salaire(resultat : list) -> list:    # Fonction pour calculer les salaires

    salaire = 0
    duree_heures = 0
    employe_id = None
    for pointage in resultat:   # Parcourir les pointages
        employe_id = pointage[1]    # Récupérer l'ID de l'employé
        date = pointage[2]  # Récupérer la date du pointage
        heure_debut = pointage[3]   # Récupérer l'heure de début
        heure_fin = pointage[4]     # Récupérer l'heure de fin
    
        # Calculer la durée du travail
        duree = heure_fin - heure_debut
        duree_heures += duree.total_seconds() / 3600 # Convertir la durée en heures

        # Récupérer le salaire horaire de l'employé
        conn = sqlite3.connect("pointages.db")
        cursor = conn.cursor()
        cursor.execute("SELECT salaire_horaire FROM employes WHERE employe_id = ?", (employe_id,))
        salaire_horaire = cursor.fetchone()[0]  # Récupérer le salaire horaire
        conn.close()

        # Calculer le salaire pour ce pointage
        salaire += duree_heures * salaire_horaire

    return employe_id, salaire, duree_heures

def creer_salaire_sql() -> None:        # Fonction pour créer la table des salaires dans la base de données
    conn = sqlite3.connect("pointages.db")
    cursor = conn.cursor()
    cursor.execute( '''

                    CREATE TABLE IF NOT EXISTS salaires (
                        employe_id INTEGER PRIMARY KEY,
                        salaire FLOAT NOT NULL,
                        heure_travaillee FLOAT NOT NULL
                    )
'''
                   )
    conn.commit()
    conn.close()

def enregistrer_salaire(employe_id, salaire, duree_heures) -> None:      # Fonction pour enregistrer les salaires dans la base de données
    conn = sqlite3.connect("pointages.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO salaires (employe_id, salaire, heure_travaillee) VALUES (?, ?, ?)", (employe_id, salaire, duree_heures))

    conn.commit()
    conn.close()

def demande_salaire(employe_id) -> None:      # Fonction principale enregistrant les salaires
    salaire, duree_heures = 0, 0
    resultat = recuperer_donnees(employe_id)
    creer_salaire_sql()
    employe_id, salaire, duree_heures = calculer_salaire(resultat)
    enregistrer_salaire(employe_id, salaire, duree_heures)

