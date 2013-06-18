from PyQt4 import QtGui, QtCore
from redBeeManagement import RedBees
from threadLecture import ThreadLecture

class ListTags(QtGui.QListWidget) :
    def __init__(self, parent) :
        QtGui.QListWidget.__init__(self, parent)
        self.threads = []


    def lancer_detection(self, id) :
        redBee = RedBees(id)
        thread = ThreadLecture(self, redBee)
        self.threads.append(thread)
        thread.start()

    def addMessage(self, message, ok, redBee) :
        if ok : img = QtGui.QIcon("icons/ok.png")
        else :img = QtGui.QIcon("icons/nope.png")
        item = QtGui.QListWidgetItem(img,"RedBee " + str(redBee.id) + " : " + message)
        QtGui.QListWidget.addItem(self, item)
        self.scrollToItem(item)

        self.parent().toolValidation.setLastEvent(redBee, not ok)
