from PyQt4 import QtCore

class ThreadLecture(QtCore.QThread) :
    def __init__(self,parent, redBee) :
        QtCore.QThread.__init__(self)
        self.redBee = redBee
        self.parent = parent

        self.connect(self, QtCore.SIGNAL("addMessage"), self.addMessage)

    def sendMessage(self, message, ok) :
        self.emit(QtCore.SIGNAL("addMessage"), message, ok)

    def arreter_detection(self) :
        self.redBee.desinscrire()

    def run(self) :
        self.redBee.lancer_detection(self)

    def addMessage(self, message, ok) :
        self.parent.addMessage(message, ok, self.redBee)
