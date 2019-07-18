import sys
from PySide2.QtWidgets import QApplication, QMainWindow
#from PySide2 import QtCore, QtUiTools
#from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
#    QVBoxLayout, QWidget, QLabel, QHBoxLayout,QSizePolicy,QDial,QLCDNumber)
from ul_mise_en_page import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PLAY_Button.clicked.connect(self.PLAY)
        self.ui.PAUSE_Button.clicked.connect(self.PAUSE)
        self.ui.STOP_Button.clicked.connect(self.STOP)
        self.ui.FFW_Button.clicked.connect(self.FFW)
        self.ui.REW_Button.clicked.connect(self.REW)
        self.ui.dial_volumen.minimum(0)


    def PLAY(self):
        print('PLAY PRESSED')

    def PAUSE(self):
        print('PAUSE PRESSED')

    def FFW(self):
        print('FFW PRESSED')

    def REW(self):
        print('REW PRESSED')

    def STOP(self):
        print('STOP PRESSED')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
