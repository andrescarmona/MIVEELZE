# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mise_en_page.ui',
# licensing of 'mise_en_page.ui' applies.
#
# Created: Thu Jul 18 10:41:00 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QVideoWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.time1 = QtWidgets.QLabel(self.centralwidget)
        self.time1.setTextFormat(QtCore.Qt.PlainText)
        self.time1.setObjectName("time1")
        self.horizontalLayout_6.addWidget(self.time1)
        self.sliderTime = QtWidgets.QSlider(self.centralwidget)
        self.sliderTime.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTime.setObjectName("sliderTime")
        self.horizontalLayout_6.addWidget(self.sliderTime)
        self.time2 = QtWidgets.QLabel(self.centralwidget)
        self.time2.setObjectName("time2")
        self.horizontalLayout_6.addWidget(self.time2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        self.PLAY_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PLAY_Button.sizePolicy().hasHeightForWidth())
        self.PLAY_Button.setSizePolicy(sizePolicy)
        self.PLAY_Button.setObjectName("PLAY_Button")
        self.buttons_layout.addWidget(self.PLAY_Button)
        self.PAUSE_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PAUSE_Button.sizePolicy().hasHeightForWidth())
        self.PAUSE_Button.setSizePolicy(sizePolicy)
        self.PAUSE_Button.setObjectName("PAUSE_Button")
        self.buttons_layout.addWidget(self.PAUSE_Button)
        self.STOP_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STOP_Button.sizePolicy().hasHeightForWidth())
        self.STOP_Button.setSizePolicy(sizePolicy)
        self.STOP_Button.setObjectName("STOP_Button")
        self.buttons_layout.addWidget(self.STOP_Button)
        self.REW_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.REW_Button.sizePolicy().hasHeightForWidth())
        self.REW_Button.setSizePolicy(sizePolicy)
        self.REW_Button.setObjectName("REW_Button")
        self.buttons_layout.addWidget(self.REW_Button)
        self.FFW_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FFW_Button.sizePolicy().hasHeightForWidth())
        self.FFW_Button.setSizePolicy(sizePolicy)
        self.FFW_Button.setObjectName("FFW_Button")
        self.buttons_layout.addWidget(self.FFW_Button)
        self.verticalLayout_3.addLayout(self.buttons_layout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.file_list = QtWidgets.QListView(self.centralwidget)
        self.file_list.setObjectName("file_list")
        self.verticalLayout_2.addWidget(self.file_list)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.next_file_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_file_button.sizePolicy().hasHeightForWidth())
        self.next_file_button.setSizePolicy(sizePolicy)
        self.next_file_button.setIconSize(QtCore.QSize(8, 16))
        self.next_file_button.setObjectName("next_file_button")
        self.horizontalLayout_4.addWidget(self.next_file_button)
        self.prev_file_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_file_button.sizePolicy().hasHeightForWidth())
        self.prev_file_button.setSizePolicy(sizePolicy)
        self.prev_file_button.setIconSize(QtCore.QSize(8, 8))
        self.prev_file_button.setObjectName("prev_file_button")
        self.horizontalLayout_4.addWidget(self.prev_file_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_Volumen = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Volumen.sizePolicy().hasHeightForWidth())
        self.label_Volumen.setSizePolicy(sizePolicy)
        self.label_Volumen.setObjectName("label_Volumen")
        self.horizontalLayout_3.addWidget(self.label_Volumen)
        self.dial_volumen = QtWidgets.QDial(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial_volumen.sizePolicy().hasHeightForWidth())
        self.dial_volumen.setSizePolicy(sizePolicy)
        self.dial_volumen.setObjectName("dial_volumen")
        self.horizontalLayout_3.addWidget(self.dial_volumen)
        self.volumen_level = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumen_level.sizePolicy().hasHeightForWidth())
        self.volumen_level.setSizePolicy(sizePolicy)
        self.volumen_level.setObjectName("volumen_level")
        self.horizontalLayout_3.addWidget(self.volumen_level)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.time1.setText(QtWidgets.QApplication.translate("MainWindow", "0:00", None, -1))
        self.time2.setText(QtWidgets.QApplication.translate("MainWindow", "1h:30s:35s", None, -1))
        self.PLAY_Button.setText(QtWidgets.QApplication.translate("MainWindow", "PLAY", None, -1))
        self.PAUSE_Button.setText(QtWidgets.QApplication.translate("MainWindow", "PAUSE", None, -1))
        self.STOP_Button.setText(QtWidgets.QApplication.translate("MainWindow", "STOP", None, -1))
        self.REW_Button.setText(QtWidgets.QApplication.translate("MainWindow", "REW", None, -1))
        self.FFW_Button.setText(QtWidgets.QApplication.translate("MainWindow", "FFW", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.next_file_button.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.prev_file_button.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.label_Volumen.setText(QtWidgets.QApplication.translate("MainWindow", "VOLUMEN", None, -1))
        self.volumen_level.setText(QtWidgets.QApplication.translate("MainWindow", "3%", None, -1))

from PySide2.QtMultimediaWidgets import QVideoWidget
