import time
import threading

import serie

class AbstractRedBee:
    def __init__(self, id, chemin) :
        self.id = id
        self.serie = serie.Serie(id, chemin)
        
    def getId(self) :
        return self.id
        
    def humanReadable(self) :
        phrase = "RedBee \t| id n° " + str(self.id)
        return phrase
        
    def ajouter_dernier_badge(self):
        """
        Ajoute le dernier badge passé à la liste de confiance
        """
        self.serie.communiquer("sv", self.id)
        
    def retirer_dernier_badge(self):
        """
        Retire le dernier badge passé de la liste de confiance
        """
        self.serie.communiquer("del", self.id)
        
    def lancer_detection(self):
        """
        Lance un thread de lecture des badges détectés
        """
        
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
        
        th = threading.Thread(None, check, None, (self.serie,))
        th.start()

class RedBeeSerie(AbstractRedBee) :
    def __init__(self, id, chemin) :
        AbstractRedBee.__init__(self, id, chemin)
        
        
class RedBeeXBee(AbstractRedBee) :
    def __init__(self, id, chemin) :
        AbstractRedBee.__init__(self, id, chemin)
