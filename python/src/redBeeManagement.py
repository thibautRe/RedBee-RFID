import redBee


class RedBees(object) :
    redbees = []
    
    def addRedBee(redBee) :
        """
        Ajouter une redBee dans le tableau
        """
        RedBees.redbees.append(redBee)
            
    def removeRedBee(redBee) :
        """
        Enlève une redBee du tableau.
        L'argument peut-être son id (int) ou l'instance elle-même
        """
        if type(redBee) == int :
            for id, redBee_ in enumerate(RedBees.redbees) :
                if redBee_.getId() == redBee :
                    del RedBees.redbees[id]
        else :
            RedBees.redbees.remove(redBee)
               
    def __new__(RedBees, id):
        return RedBees.getRedBeeById(id)
        
    def getRedBeeById(id) :
        """
        Retourne la redBee selon l'identifiant donné
        
        Note : il est préférable d'appeller directement la classe : RedBees(5) retournera la RedBee d'id 5,
        ou lancera une exception.
        """
        for redBee in RedBees.redbees :
            if redBee.getId() == id :
                return redBee
        
        raise Exception("RedBee d'id " + str(id) + " non trouvée !")
    
    def listing() :
        return RedBees.redbees
        
    def humanReadable() :
        string = ""
        for redBee in RedBees.redbees :
            string += redBee.humanReadable() + "\n"
            
        return string

if __name__ == "__main__" :
    redBee1 = redBee.RedBee(5, "oooo")
    RedBees.addRedBee(redBee1)
    print (RedBees.humanReadable())
    RedBees.removeRedBee(5)