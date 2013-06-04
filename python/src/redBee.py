#import serie


class AbstractRedBee:
    def __init__(self, id, serie) :
        self.id = id
        self.serie = serie
        
    def getId(self) :
        return self.id
        
    def humanReadable(self) :
        phrase = "RedBee \t| id n° " + str(self.id) + "\t| Série : " + str(self.serie)
        return phrase
        
RedBee = AbstractRedBee
        


class RedBeeSerie(AbstractRedBee) :
    def __init__(self, serie) :
        AbstractRedBee.__init__(self, serie)
        
        
class RedBeeXBee(AbstractRedBee) :
    def __init__(self, serie) :
        AbstractRedBee.__init__(self, serie)
