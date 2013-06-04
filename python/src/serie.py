from serial import Serial
import os
import time
from threading import Lock

class Serie:
    
    baudrate = 9600
    
    def __init__(self):
        
        #mutex d'accès à la série
        self.mutex = Lock()
        
        #périphérique série de l'imprimante (une fois la carte trouvée)
        self.serie = None

        #recherche du port série
        self.attribuer()
        
    def _clean_string(self, chaine):
        """
        supprime des caractères spéciaux sur la chaine
        """
        return chaine.replace("\n","").replace("\r","").replace("\0","")         

    def attribuer(self):
        #liste les chemins trouvés dans /dev
        sources = os.popen('ls -1 /dev/ttyUSB* 2> /dev/null').readlines()
        sources.extend(os.popen('ls -1 /dev/ttyACM* 2> /dev/null').readlines())

        for k in range(len(sources)):
            sources[k] = sources[k].replace("\n","")
            
        for source in sources:
            serie = Serial(source, Serie.baudrate, timeout=0.1)

            #vide le buffer série coté pc
            serie.flushInput()

            #clean buffer et récupération de l'identifiant
            serie.write(bytes("@0:ping\r","utf-8"))
            
            #il faut vider le buffer de 5 lignes. 
            #Si on ne recoit pas une trame contenant #RFIDReader au delà, ce n'est pas le bon périphérique
            tentatives = 0
            rep = []
            while (len(rep)<2 or not rep[1] == "#RFIDReader") and tentatives < 6:
                rep = self._clean_string(str(serie.readline(),"utf-8")).split(":")
                tentatives += 1
            
            if tentatives <= 6:
                
                #enregistrement du périphérique
                self.id = rep[0][1]
                self.serie = serie
            
                #évacuation du prompt
                serie.readline()
                
                #on n'en cherche pas d'autres
                break
                
        if not self.serie:
            raise Exception("Redbee non trouvée sur la série !")
            
        
    def communiquer(self, destinataire, message, nb_lignes_reponse):
    
        self.serie.write(bytes("@0/"+str(destinataire)+":"+message+"\r","utf-8"))
        
        reponse = []
        rep = ''
        
        #première trame non vide
        while rep == '':
            rep = self._clean_string(str(self.serie.readline(),"utf-8"))
            time.sleep(0.1)
            
        #dernière trame non vide
        while not rep == '':
            reponse.append(rep)
            rep = self._clean_string(str(self.serie.readline(),"utf-8"))
            
        #trames ayant du sens
        t = 0
        while t < len(reponse):
            #supprime les trames ne respectant pas le format attendu
            if not reponse[t][:2] == "@"+self.id:
                del reponse[t]
            else:
                t += 1
            
        #supprime les doublons
        reponse = list(set(reponse))
        
        return reponse
        
        
serie = Serie()

while 1:
    ordre = input(">")
    
    #sortie
    if ordre == "q":
        break
        
    if not ordre == "":
        print(serie.communiquer(serie.id, ordre, 1))
    