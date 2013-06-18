
from PyQt4 import QtCore, QtGui

class ToolValidation(QtGui.QDockWidget) :
    def __init__(self, parent) :
        QtGui.QDockWidget.__init__(self, parent)
        self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)

        self.add = False
        self.redBee=None

        self.initUID()



    def getText(self) :
        if self.redBee is None :
            return ("En attente")

        if self.add : return "Ajouter le dernier badge à RedBee " + str(self.redBee.id)
        else : return "Retirer le dernier badge à RedBee " + str(self.redBee.id)

    def getIcon(self)  :
        if self.add : return QtGui.QIcon("icons/ok.png")
        else : return QtGui.QIcon("icons/nope.png")

    def initUID(self) :
        self.widget = QtGui.QWidget(self)
        layout = QtGui.QGridLayout(self.widget)

        self.bouton = QtGui.QPushButton(self.getIcon(), self.getText(), self.widget)
        self.bouton.clicked.connect(self.action)
        self.bouton.setEnabled(False)

        layout.addWidget(self.bouton,0,0)
        self.widget.setLayout(layout)

        self.setWidget(self.widget)

    def setLastEvent(self, redBee, add) :
        self.bouton.setEnabled(True)
        self.redBee=redBee
        self.add=add

        self.bouton.setIcon(self.getIcon())
        self.bouton.setText(self.getText())

    def action(self) :
        if self.add :
            self.redBee.ajouter_dernier_badge()
        else :
            self.redBee.retirer_dernier_badge()

        self.bouton.setEnabled(False)
