import sys
from PySide2.QtWidgets import QApplication, QWidget,QVBoxLayout,QSlider
from PySide2.QtGui import QPainter, QPaintEvent, QPen
from PySide2 import QtCore
from PySide2.QtCore import QTimer, Qt, QTime

import time

class monClock(QWidget):
    def __init__(self, parent=None):
        super(monClock, self).__init__(parent)

        self.interval_time = 1000

        local_time = QTime.currentTime()

        self.valeur_sec = local_time.second()
        self.valeur_min = local_time.minute()
        self.valeur_h   = local_time.hour()

        # self.slider.valueChanged.connect(self.compteur.interval_time)
        self.timer = QTimer()
        self.timer.setInterval(self.interval_time)
        self.timer.timeout.connect(self.setValeur_sec_min_h)
        self.timer.start()
        print("Time refreshing",self.interval_time)

    def setValeur_sec_min_h(self):
        #print("I am getting here")

        if self.valeur_sec < 59 :
            self.valeur_sec += 1
        else:
            self.valeur_min += 1
            self.valeur_sec = 0
            if self.valeur_min > 59:
               self.valeur_h += 1
               self_valeur_min = 0

            if self.valeur_h > 12:
                self.valeur_h = 0

        self.update()

    def setSpeed(self,value):
        value = abs(value)
        print('its getting here?', value)
        self.interval_time = value
        #self.timer = QTimer()
        self.timer.setInterval(self.interval_time)
        self.timer.timeout.connect(self.setValeur_sec_min_h)
        self.timer.start()
        #self.update()



    def paintEvent(self, event:QPaintEvent):
        p = QPainter(self)

        #p.setBrush(Qt.blue)
        #p.drawRect(10,10,self.width()-20, self.height()-20)
        #p.setBrush(Qt.black)
        #p.drawEllipse(20,20,self.width()-40, self.height()-40)

        p.translate(0,0)
        p.setBrush(QtCore.Qt.black)
        p.drawEllipse(0, 0, self.height() , self.height())
        p.translate(self.height()/2 , self.height()/2)

        angle_sec = 360. * self.valeur_sec / 60.
        angle_min = 360. * ( self.valeur_min  + self.valeur_sec /60. ) / 60.
        angle_h   = 360. * ( self.valeur_h + self.valeur_min/60. + self.valeur_sec/3600) / 12.

        #angle_sec = 360 * self.valeur_sec / 60
        #angle_min = 360 * ( self.valeur_min) / 60
        #angle_h   = 360 * ( self.valeur_h) / 12

        p.rotate(180)
        p.rotate(angle_sec)
        #p.setPen(QtCore.Qt.red,4)
        pen = QPen(Qt.green, 2)
        p.setPen(pen)
        p.drawLine(0, 0, 0, 0.85*self.height()/2)
        p.rotate(-1 * angle_sec)
        p.rotate(angle_min)
        pen = QPen(Qt.blue, 3)
        p.setPen(pen)
        p.drawLine(0, 0, 0, 0.8*self.height()/2)
        p.rotate(-1 * angle_min)
        p.rotate(angle_h)
        pen = QPen(Qt.red, 4)
        p.setPen(pen)
        p.drawLine(0, 0, 0, 0.6*self.height()/2)

        p.setBrush(QtCore.Qt.green)
        pen = QPen(Qt.green, 3)
        p.setPen(pen)
        p.translate(self.height()/100 , self.height()/100)
        p.drawEllipse(0, 0, -1*self.height()/50 ,-1*self.height()/50)




class fen(QWidget):
    def __init__(self, parent=None):
        super(fen, self).__init__(parent)

        self.setMinimumSize(500,500)
        self.clock=monClock()
        self.slider = QSlider(QtCore.Qt.Horizontal)


        layout = QVBoxLayout()


        layout.addWidget(self.clock)
        layout.addWidget(self.slider)
        #horizontalLayout = QtWidgets.QHBoxLayout(layout)


        self.setLayout(layout)


        self.slider.setMinimum(-2000)
        self.slider.setMaximum(-1)
        self.slider.setValue(-1000)

        #self.clock.valeur_sec = 0
        #self.clock.valeur_min = 0

        self.slider.valueChanged.connect(self.clock.setSpeed)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    aux = fen()


    aux.show()

    sys.exit(app.exec_())