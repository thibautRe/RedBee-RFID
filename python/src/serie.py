from serial import Serial
import os
import time
from threading import Lock

class Serie:
    
    baudrate = 9600
    nb_tentatives = 6
    
    def __init__(self, id, port):
        
        #mutex d'accès à la série
        self.mutex = Lock()
        
        #périphérique série de l'imprimante (une fois la carte trouvée)
        self.serie = Serial(port, Serie.baudrate, timeout=0.1)
        self.id = id

    def _clean_string(chaine):
        """
        supprime des caractères spéciaux sur la chaine
        """
        return chaine.replace("\n","").replace("\r","").replace("\0","")         

    def attribuer():
        #liste les chemins trouvés dans /dev
        sources = os.popen('ls -1 /dev/ttyUSB* 2> /dev/null').readlines()
        sources.extend(os.popen('ls -1 /dev/ttyACM* 2> /dev/null').readlines())

        for k in range(len(sources)):
            sources[k] = sources[k].replace("\n","")
            
        series = {}
        
        for source in sources:
            serie = Serial(source, Serie.baudrate, timeout=0.1)

            #vide le buffer série coté pc
            serie.flushInput()

            #clean buffer et récupération de l'identifiant
            serie.write(bytes("@0:ping\r","utf-8"))
            
            #il faut parfois vider quelques lignes du buffer
            tentatives = 0
            rep = ""
            while (len(rep)<2 or not rep[0] == "@") and tentatives < Serie.nb_tentatives:
                rep = Serie._clean_string(str(serie.readline(),"utf-8"))
                tentatives += 1
                time.sleep(0.1)
            
            if tentatives < Serie.nb_tentatives:
                #enregistrement du périphérique
                series[int(rep[1])] = source
            
                #évacuation du prompt
                serie.readline()
                
        if not series:
            raise Exception("Aucune Redbee trouvée sur la série !")
        
        return series
            
        
    def communiquer(self, message, destinataire=None):
    
        self.mutex.acquire()
        time.sleep(0.01)
        
        if destinataire:
            self.serie.write(bytes("@0/"+str(destinataire)+":"+message+"\r","utf-8"))
        else:
            self.serie.write(bytes("@0:"+message+"\r","utf-8"))
        
        reponse = []
        rep = ''
        
        #première trame non vide
        tentatives = 0
        while rep == '' and tentatives<Serie.nb_tentatives:
            rep = Serie._clean_string(str(self.serie.readline(),"utf-8"))
            time.sleep(0.1)
            tentatives += 1
            
        if tentatives == Serie.nb_tentatives:
            self.mutex.release()
            return ['']
            
        #dernière trame non vide
        while not rep == '':
            reponse.append(rep)
            rep = Serie._clean_string(str(self.serie.readline(),"utf-8"))
            
        #trames ayant du sens
        t = 0
        while t < len(reponse):
            #supprime les trames ne respectant pas le format attendu
            if not reponse[t][:2] == "@"+str(self.id):
                del reponse[t]
            else:
                #supprime les informations expéditeur/destinataire
                reponse[t] = "".join(reponse[t].split(":")[1:])
                t += 1
            
        #supprime les doublons
        reponse = list(set(reponse))
        
        self.mutex.release()
        return reponse
        
        
if __name__ == '__main__':
    #affichage des Redbee trouvées
    series = Serie.attribuer()
    print(series)
    
    id = int(input("id ?"))
    lecteur = Serie(id, series[id])
    
    while 1:
        ordre = input(">")
        
        #sortie
        if ordre == "q":
            break
            
        elif ordre == "ping":
            print(lecteur.communiquer(ordre))
        else:
            print(lecteur.communiquer(ordre, id))
        