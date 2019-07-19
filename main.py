import sys
import datetime
from PySide2.QtWidgets import QApplication, QMainWindow
#from PySide2 import QtCore, QtUiTools
#from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
#    QVBoxLayout, QWidget, QLabel, QHBoxLayout,QSizePolicy,QDial,QLCDNumber)


from PySide2.QtCore import QUrl, QTime
from  PySide2.QtWidgets import QFileDialog, QListWidgetItem
#import PySide2.QtWidgets
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
import PySide2

from ul_mise_en_page import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PLAY_Button.clicked.connect(self.PLAY)
        self.ui.PAUSE_Button.clicked.connect(self.PAUSE)
        self.ui.STOP_Button.clicked.connect(self.STOP)
        self.ui.PREV_Button.clicked.connect(self.PREV)
        self.ui.NEXT_Button.clicked.connect(self.NEXT)
        self.ui.next_file_button.clicked.connect(self.nextFile)
        self.ui.del_file_button.clicked.connect(self.delFile)
        self.ui.dial_volumen.setMinimum(0)
        self.ui.dial_volumen.setMaximum(100)
        self.ui.dial_volumen.setValue(3)
        self.ui.volumen_level.setText(str(self.ui.dial_volumen.value())+'%')

        self.ui.sliderTime.setMinimum(0)
        self.ui.sliderTime.setMaximum(3600)
        self.ui.sliderTime.setValue(0)
        self.ui.timePlayed.setText(str(self.ui.sliderTime.value())+'s')

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setVideoOutput(self.ui.wVideo)
        #mediaContent = QMediaContent(QUrl.fromLocalFile('big_buck_bunny.avi'))
        #self.mediaPlayer.setMedia(mediaContent)
    #Dialog
        self.ui.dial_volumen.valueChanged.connect(self.changeVolDial)
        self.mediaPlayer.positionChanged.connect(self.updateTime)
        self.ui.sliderTime.valueChanged.connect(self.changeTime)
        self.ui.file_list.itemDoubleClicked.connect(self.loadfile)

    def changeVolDial(self):
        print('VOLUMEN CHANGED')
        self.ui.volumen_level.setText(str(self.ui.dial_volumen.value()) + '%')
        self.mediaPlayer.setVolume(self.ui.dial_volumen.value())

    def updateTime(self):
        self.ui.sliderTime.valueChanged.disconnect(self.changeTime)
        localTime = QTime(0, 0, 0)
        currentTime = localTime.addMSecs(self.mediaPlayer.position())
        #print(self.mediaPlayer.position()-self.mediaPlayer.duration())
        timeLeft = localTime.addMSecs(self.mediaPlayer.duration()-self.mediaPlayer.position())
        #h, res = divmod(t, 3600)
        #m, s = divmod(res, 60)
        #time_str = f'{int(h):02}:{int(m):02}:{int(s):02}'
        self.ui.timePlayed.setText(currentTime.toString("HH:mm:ss"))
        self.ui.timeTotal.setText('-'+timeLeft.toString("HH:mm:ss"))
        self.ui.sliderTime.setValue(self.mediaPlayer.position())
        self.ui.sliderTime.valueChanged.connect(self.changeTime)

    def loadfile(self):
        #rowItem=self.ui.file_list.currentRow()
        currentItem=self.ui.file_list.currentItem()
        print(self.ui.file_list.currentItem().text())
        #mediaContent=QMediaContent(QUrl.fromLocalFile(currentItem.toolTip()))
        mediaContent=QMediaContent(QUrl.fromLocalFile(currentItem.text()))
        #mediaContent = QMediaContent(QUrl.fromLocalFile('big_buck_bunny.avi'))
        self.mediaPlayer.setMedia(mediaContent)
        self.PLAY()
        #print(self.ui.file_list.takeItem(0))


    def changeTime(self):
        self.mediaPlayer.positionChanged.disconnect(self.updateTime)
        print('Time CHANGED')
        self.mediaPlayer.setPosition(self.ui.sliderTime.value())
        localTime = QTime(0, 0, 0)
        currentTime = localTime.addMSecs(self.mediaPlayer.position())
        self.ui.timePlayed.setText(currentTime.toString("HH:mm:ss"))
        self.mediaPlayer.positionChanged.connect(self.updateTime)

    def delFile(self):
        print('delFile PRESSED')
        rowItem= self.ui.file_list.currentRow()
        if rowItem != -1:
            self.ui.file_list.takeItem(rowItem)

    def nextFile(self):
        print('nextFile PRESSED')
        filename=QFileDialog.getOpenFileName(self,"Choix Film")
        item = QListWidgetItem(filename[0])
        self.ui.file_list.addItem(item)

    def PLAY(self):
        print('PLAY PRESSED')
        self.mediaPlayer.setVolume(self.ui.dial_volumen.value())
        self.mediaPlayer.play()
        localTime = QTime(0, 0, 0)
        totalTime = localTime.addMSecs(self.mediaPlayer.duration())
        self.ui.sliderTime.setMaximum(self.mediaPlayer.duration())
        self.ui.timeTotal.setText(totalTime.toString("HH:mm:ss"))


    def PAUSE(self):
        print('PAUSE PRESSED')
        if self.mediaPlayer.state() == QMediaPlayer.PausedState:
            self.mediaPlayer.play()
        else:
            self.mediaPlayer.pause()

    def PREV(self):
        print('PREV PRESSED')
        rowItem = self.ui.file_list.currentRow()
        if rowItem == -1:
            return

        self.ui.file_list.setCurrentRow((rowItem - 1))
        filename = self.ui.file_list.currentItem().text()
        print('Loading ' + filename)
        mediaContent = QMediaContent(QUrl.fromLocalFile(filename))
        self.mediaPlayer.setMedia(mediaContent)
        self.PLAY()

    def NEXT(self):
        print('NEXT PRESSED')
        totalItems = self.ui.file_list.count()
        rowItem    = self.ui.file_list.currentRow()

        if rowItem+1 > totalItems:
          return

        self.ui.file_list.setCurrentRow((rowItem+1))
        filename = self.ui.file_list.currentItem().text()
        print('Loading '+ filename)
        mediaContent = QMediaContent(QUrl.fromLocalFile(filename))
        self.mediaPlayer.setMedia(mediaContent)
        self.PLAY()


    def STOP(self):
        print('STOP PRESSED')
        self.mediaPlayer.stop()

    def get_str_time(t):
        h, res = divmod(t, 3600)
        m, s = divmod(res, 60)
        return f'{int(h):02}:{int(m):02}:{int(s):02}'


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
