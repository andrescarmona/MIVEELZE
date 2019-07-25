import sys
import datetime
from PySide2.QtWidgets import(QLabel, QApplication,
    QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy,QMainWindow)
from PySide2.QtCore import QUrl, QTime
from  PySide2.QtWidgets import QFileDialog, QListWidgetItem
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
import PySide2
import numpy as np
import matplotlib.pyplot as plt
from PySide2.QtGui import QPixmap
from io import BytesIO
import base64
import json


from bulletin_notes_main_page import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #load JSON file
        filename='school_short.json'
        with open(filename) as json_file:
            self.database = json.load(json_file)
        self.loadAcademies()

        #if one academy is selected load the schools
        #self.ui.academyList.currentIndexChanged.connect(self.loadEcoles)
        self.ui.academyList.activated.connect(self.loadEcoles)

    def loadAcademies(self):
        print('Loading Academies')
        self.academyList=[]
        for academy in self.database['academies']:
            print(academy['nom'])
            self.academyList.append(academy['nom'])
        self.ui.academyList.clear()
        self.ui.academyList.addItems(self.academyList)
        self.loadEcoles()
        self.update()


    def loadEcoles(self):
        self.academy = self.ui.academyList.currentText()
        print('Loading school for:', self.academy)
        #currentAcademy = self.database['academies'][self.ui.academyList.currentIndex()]
        #nbE = len(currentAcademy["etablisements"])
        #for i in range(nbE):
        #    print(currentAcademy["etablisements"][i]["nom"])

        self.dataAcademy=self.database['academies'][self.ui.academyList.currentIndex()]
        self.ecoleList=[]
        for ecole in self.dataAcademy["etablisements"]:
            print(ecole['nom'])
            self.ecoleList.append(ecole['nom'])
        self.ui.ecoleList.clear()
        self.ui.ecoleList.addItems(self.ecoleList)
        self.update()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
