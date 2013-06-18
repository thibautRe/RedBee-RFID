import redBee
import serie

class RedBees(object) :
    redbees = []

    def addRedBee(redBee) :
        """
        Ajouter une redBee dans le tableau
        """
        RedBees.redbees.append(redBee)

    def removeAll():
        """
        Supprime touts les lecteurs
        """
        #~ print("Suppression de tous les lecteurs...")
        for redBee in RedBees.redbees:
            RedBees.removeRedBee(redBee)

    def removeRedBee(redBee) :
        """
        Enlève une redBee du tableau.
        L'argument peut-être son id (int) ou l'instance elle-même
        """
        if type(redBee) == int :
            for id, redBee_ in enumerate(RedBees.redbees) :
                if redBee_.getId() == redBee :
                    RedBees.removeRedBee(redBee_)
                    return
        else :
            redBee.desinscrire()
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

    def readers_survey():
        series = serie.Serie.attribuer()
        for id in series.keys() :
            lecteur = redBee.RedBeeXBee(id, series[id])
            #sauvegarde de l'instance dans la collection
            RedBees.addRedBee(lecteur)
        return series

    def activerRedBees(ids) :
        for id in ids:
            try:
                #début du thread de lecture pour ce lecteur
                lecteur.lancer_detection()
            except: pass


    def scan_lecteurs():
        RedBees.readers_survey()
        if len(RedBees.listing()) == 1:
            #~ print("Vous vous adressez au lecteur " + str(redBeeManagement.RedBees.listing()[0].getId()) + " (le seul trouvé)")
            lecteur = RedBees.listing()[0]
        else:
            lecteur = None
        return lecteur




if __name__ == "__main__" :
    redBee1 = redBee.RedBeeXBee(5, "oooo")
    RedBees.addRedBee(redBee1)
    print (RedBees.humanReadable())
    RedBees.removeRedBee(5)
