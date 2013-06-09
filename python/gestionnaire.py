import sys,os

#retrouve le chemin de la racine "software/pc"
directory = os.path.dirname(os.path.abspath(__file__))
racine = "RedBee-RFID/python"
chemin = directory[:directory.index(racine)]+racine
#répertoires d'importation
sys.path.insert(0, os.path.join(chemin, "src/"))

#modules du projet
import redBeeManagement

redBeeManagement.RedBees.readers_survey()
    
if len(redBeeManagement.RedBees.listing()) == 1:
    unique = True
    print("Vous vous adressez au lecteur " + str(redBeeManagement.RedBees.listing()[0].getId()) + " (le seul trouvé)")
    lecteur = redBeeManagement.RedBees.listing()[0]
else:
    unique = False
    
#envoi d'autres requetes
while 1:
    
    #cas de lecteurs multiples
    if not unique:
        id_destinataire = int(input("id du lecteur destinataire ?"))
        lecteur = redBeeManagement.RedBees.getRedBeeById(id_destinataire)
        
    #commande envoyée au lecteur
    ordre = input(">")
    
    #sortie de boucle
    if ordre == "q":
        break
        
    #reste du prompt...
    elif ordre == "s":
        lecteur.retirer_dernier_badge()
        print("étiquette supprimée !")
    elif ordre == "a":
        lecteur.ajouter_dernier_badge()
        print("étiquette ajoutée !")
    