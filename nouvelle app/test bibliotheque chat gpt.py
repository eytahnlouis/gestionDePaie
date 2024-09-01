from datetime import datetime, timedelta

# Fonction pour calculer le temps de travail à partir des heures d'arrivée, de départ, et de pause
def calculer_temps_travail(heure_arrivee, heure_depart, pause=timedelta(hours=1)):
    # Convertir les chaînes de caractères en objets datetime
    format_heure = "%H:%M"
    arrivee = datetime.strptime(heure_arrivee, format_heure)
    depart = datetime.strptime(heure_depart, format_heure)
    
    # Calculer la différence entre l'heure de départ et l'heure d'arrivée
    temps_travail = depart - arrivee
    
    # Soustraire la pause déjeuner
    temps_travail -= pause
    
    return temps_travail
