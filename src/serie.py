from serial import Serial
import os
import time

#liste les chemins trouvés dans /dev
sources = os.popen('ls -1 /dev/ttyUSB* 2> /dev/null').readlines()
sources.extend(os.popen('ls -1 /dev/ttyACM* 2> /dev/null').readlines())

for k in range(len(sources)):
    sources[k] = sources[k].replace("\n","")
    
baudrate = 9600

print("test sur "+sources[0])
serie = Serial(sources[0], baudrate, timeout=0.1)

#vide le buffer série coté pc
serie.flushInput()

def _clean_string( chaine):
    """
    supprime des caractères spéciaux sur la chaine
    """
    return chaine.replace("\n","").replace("\r","").replace("\0","")         

#récupération de l'identifiant
serie.write(bytes("@0:ping\r","utf-8"))
print(_clean_string(str(serie.readline(),"utf-8")))
print(_clean_string(str(serie.readline(),"utf-8")))
print(_clean_string(str(serie.readline(),"utf-8")))

id = input("id ?")

while 1:
    ordre = input(">")
    
    #sortie
    if ordre == "q":
        break
        
    if not ordre == "":
        serie.write(bytes("@0/"+str(id)+":"+ordre+"\r","utf-8"))
    
    #ligne vide
    serie.readline()
    
    rep = _clean_string(str(serie.readline(),"utf-8"))
    
    print(rep)