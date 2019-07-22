import sys, json
import datetime
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QUrl, QTime
from  PySide2.QtWidgets import QFileDialog, QListWidgetItem
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
import PySide2

from JSON_main_page import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.filename = 'repertoire.data'

        # read the JSON file and create a dictionary named "repertoire"
        self.monRepertoire = self.lireJSON(self.filename)
        self.updateListNames()


        self.ui.Modify_button.clicked.connect(self.Modify)
        self.ui.Add_button.clicked.connect(self.Add)
        self.ui.textNom.returnPressed.connect(self.changeNom)
        self.ui.listNames.itemDoubleClicked.connect(self.loadUser)

        #self.ui.textNom.returnPressed.connect(self.changeNom,self.ui.textNom.placeholderText())
        #self.ui.textNom.returnPressed.connect(self.changeNom(self.ui.textNom.placeholderText()))
        #self.ui.textPrenom.returnPressed.connect(self.changePrenom(self.ui.textPrenom.placeholderText()))
        #self.ui.textPhone.returnPressed.connect(self.changePhone(self.ui.textPhone.placeholderText()))
        #self.ui.textPrenom.returnPressed.connect(self.changePrenom(self.ui.textPrenom.placeholderText()))
        #self.ui.textPhone.returnPressed.connect(self.changePhone(self.ui.textPhone.placeholderText()))


        #self.ui.temp_user = user()


    def lireJSON(self,fileName):
        with open(fileName) as json_file:
            dico = json.load(json_file)
            return dico
        return None

    def Modify(self):
        print("changed Modified clicked")

        index = self.ui.listNames.currentRow()

        fiche = {}
        fiche["nom"] = self.ui.textNom.text()
        fiche["prenom"] = self.ui.textPrenom.text()
        fiche["tel"] = self.ui.textPhone.text()

        # print(fiche)
        self.monRepertoire["repertoire"][index]=fiche
        self.updateListNames()


    def Add(self):
        print("change Add clicked")
        fiche={}
        fiche["nom"]    = self.ui.textNom.text()
        fiche["prenom"] = self.ui.textPrenom.text()
        fiche["tel"] = self.ui.textPhone.text()

        #print(fiche)
        self.monRepertoire["repertoire"].append(fiche)
        self.updateListNames()
        #self.sauveJSON()

    def changeNom(self):
        print("change Nom clicked")
        print(self.ui.textNom.displayText())
        #self.ui.temp_user.Nom=val

    def changePrenom(self,val):
        print("change Prenom clicked")
        print(val)
        #self.ui.temp_user.Prenom=val

    def changePhone(self,val):
        print("change Phone clicked")
        print(val)
        #self.ui.temp_user.Phone=val

    def loadUser(self):
        print('load user clicked')
        index=self.ui.listNames.currentRow()
        print(index)
        self.ui.textNom.setText(self.monRepertoire["repertoire"][index]["nom"])
        self.ui.textPrenom.setText(self.monRepertoire["repertoire"][index]["prenom"])
        self.ui.textPhone.setText(self.monRepertoire["repertoire"][index]["tel"])
        self.update()


    def updateListNames(self):
        self.ui.listNames.clear()
        for fiche in self.monRepertoire["repertoire"]:
            self.ui.listNames.addItem(fiche["nom"])



class user():
    def __init__(self, parent=None):
        self.Nom =''
        self.Prenom=''
        self.Telephone=0

    def changeNom(self,val):
        self.Nom=val


    def changePrenon(self,val):
        self.Prenom=val

    def changePhone(self,val):
        self.Phone=val

    def readJSON(self,filemane):
        print,filename

    def saveJSON(self,filaname):
        print,filename

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())