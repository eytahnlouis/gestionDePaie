from importBib import *

collaborateurs = {
    str(sal.definirIdentifiant()): sal.display()
}
# Output: {'010120211': {'Nom: Doe\nPrénom: John\nDate de naissance: 1/1/2021\nAge: 0 identifiant: 10120211'}}
def demandeAjout():
    demande = input("Voulez-vous ajouter un collaborateur? (oui/non): ")
    while demande == "oui":
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        jourNaissance = int(input("Jour de naissance: "))
        moisNaissance = int(input("Mois de naissance: "))
        anneeNaissance = int(input("Année de naissance: "))
        salaireHoraire = int(input("Salaire horaire: "))
        salarie = sal(nom, prenom, jourNaissance, moisNaissance, anneeNaissance, salaireHoraire)
        collaborateurs[str(salarie.definirIdentifiant())] = salarie.display() # ajoute un collaborateur
        demande = input("Voulez-vous ajouter un collaborateur? (oui/non): ")
        print(collaborateurs) # affiche le dictionnaire des collaborateurs

def demandeAjout():
    demandeIdentification = input("Voulez-vous identifier un collaborateur? (oui/non): ")
    while demandeIdentification == "oui":
        identifiant = input("Entrez l'identifiant: ")
        if identifiant in collaborateurs.keys():
            print(collaborateurs[identifiant])
        else:
            print("Collaborateur non trouvé")
        demandeIdentification = input("Voulez-vous identifier un collaborateur? (oui/non): ")

def afficherCollaborateurs():
    print(collaborateurs.items())

