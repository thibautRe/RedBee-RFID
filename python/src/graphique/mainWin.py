from PyQt4 import QtGui, QtCore

from listTags import ListTags

from redBeeManagement import RedBees
from docks import ToolValidation

class MainWin(QtGui.QMainWindow) :
    def __init__(self) :
        QtGui.QMainWindow.__init__(self)

        self.initUID()

    def initUID(self) :

        ## Status Bar
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("L'application a été lancée avec succès")


        ## ACTIONS ##
        # RECHARGER REDBEES
        texte = "Recharger RedBees"
        reloadRedbees = QtGui.QAction(QtGui.QIcon('icons/refresh.png'), texte, self)
        reloadRedbees.setShortcut('Ctrl+R')
        reloadRedbees.setStatusTip(texte)
        reloadRedbees.triggered.connect(self.reloadRedbees)


        ## Ajout des actions
        toolbar = self.addToolBar("Barre de menus")
        toolbar.addAction(reloadRedbees)

        # DOCK WIDGET
        self.toolValidation = ToolValidation(self)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.toolValidation)

        # listTags
        self.listTags = ListTags(self)

        self.setCentralWidget(self.listTags)

        self.show()
        self.setWindowTitle("RedBee Management  --  Powered by Sopal'INT")
        self.resize(450,700)


    def reloadRedbees(self) :
        try :
            RedBees.removeAll()

            s = RedBees.readers_survey()
            msgBox = QtGui.QMessageBox(self)
            msgBox.setWindowTitle("RedBees trouvées !")
            msgBox.setText("Plusieurs redbees ont été trouvées :) :) :)")
            msgBox.setIconPixmap(QtGui.QPixmap("icons/logo.png"))
            infotext = ""
            for a in s.keys() :
                infotext += "Identifiant : " + str(a) + "\tPort : " + str(s[a]) + "\n"
            msgBox.setInformativeText(infotext)
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setDefaultButton(QtGui.QMessageBox.Ok)
            ret = msgBox.exec_()

            for a in s.keys() :
                msgBox = QtGui.QMessageBox(self)
                msgBox.setWindowTitle("Activation ?")
                msgBox.setText("Voulez-vous activer la RedBee n°" + str(a) + "(port " + str(s[a]) + ")")
                msgBox.setIcon(QtGui.QMessageBox.Question)
                msgBox.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                msgBox.setDefaultButton(QtGui.QMessageBox.Yes)
                ret = msgBox.exec_()

                if ret == QtGui.QMessageBox.Yes :
                    self.listTags.lancer_detection(a)


        except :
            msgBox = QtGui.QMessageBox(self)
            msgBox.setWindowTitle("Attention !")
            msgBox.setText("Aucune RedBee n'a été trouvée.")
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setInformativeText("Verifiez la connection puis réessayez")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setDefaultButton(QtGui.QMessageBox.Ok)
            ret = msgBox.exec_()








