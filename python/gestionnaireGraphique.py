import sys, os
from PyQt4 import QtGui


## Imports supplémentaires
sys.path.append("src/")
sys.path.append("src/serial/")
sys.path.append("src/graphique")

import redBee, redBeeManagement, serie
import mainWin

app = QtGui.QApplication(sys.argv)
app.setApplicationName("RedBee Management  --  Powered by Sopal'INT")
app.setWindowIcon(QtGui.QIcon("icons/logo.png"))

win = mainWin.MainWin()

sys.exit(app.exec_())
