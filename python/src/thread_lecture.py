import serie
import time

def check(lecteur):
    
    while 1:
        rep = lecteur.communiquer('')
        if rep and rep[0]:
            statut = rep[0].split(' ')[0]
            if statut == "TACK":
                #étiquette reconnue
                print("\bétiquette OK! : "+rep[0][5:]+" (s pour la supprimer)\n>", end='')
            elif statut == "TNACK":
                #étiquette non reconnue
                print("\bétiquette non reconnue ! : "+rep[0][6:]+" (a pour l'ajouter)\n>", end='')
                
        time.sleep(0.1)
    
    
if __name__ == '__main__':

    id = 2
    
    series = serie.Serie.attribuer()
    lecteur = serie.Serie(id, series[id])
    
    #lancement du thread de lecture
    import threading
    th = threading.Thread(None, check, None, (lecteur,))
    th.start()
    
    #envoi d'autres requetes
    while 1:
        ordre = input(">")
        
        #sortie
        if ordre == "q":
            break
            
        elif ordre == "s":
            lecteur.communiquer("del", id)
            print("étiquette supprimée !")
        elif ordre == "a":
            lecteur.communiquer("sv", id)
            print("étiquette ajoutée !")
        