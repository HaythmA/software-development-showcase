from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1162, 750)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 750))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(420, 310))
        self.groupBox_2.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 221, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(350, 40, 51, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 41, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 150, 81, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 40, 101, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 71, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 150, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 80, 71, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 61, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(90, 180, 171, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 15, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 130, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setGeometry(QtCore.QRect(20, 110, 381, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 80, 71, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_24 = QtGui.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(160, 130, 81, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 150, 101, 21))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_29 = QtGui.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(20, 210, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_4.setGeometry(QtCore.QRect(120, 210, 141, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(290, 210, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 230, 51, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 230, 51, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 260, 111, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.powerSaveButton = QtGui.QPushButton(self.groupBox_2)
        self.powerSaveButton.setGeometry(QtCore.QRect(290, 180, 111, 23))
        self.powerSaveButton.setObjectName(_fromUtf8("powerSaveButton"))
        self.pauseAcqButton = QtGui.QPushButton(self.groupBox_2)
        self.pauseAcqButton.setGeometry(QtCore.QRect(20, 260, 71, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pauseAcqButton.setFont(font)
        self.pauseAcqButton.setObjectName(_fromUtf8("pauseAcqButton"))
        self.resumeAcqButton = QtGui.QPushButton(self.groupBox_2)
        self.resumeAcqButton.setGeometry(QtCore.QRect(100, 260, 71, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.resumeAcqButton.setFont(font)
        self.resumeAcqButton.setObjectName(_fromUtf8("resumeAcqButton"))
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_23 = QtGui.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(560, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setText(_fromUtf8(""))
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_25 = QtGui.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(40, 190, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_28 = QtGui.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(40, 210, 351, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 35, 261, 145))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_30 = QtGui.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(20, 40, 221, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.groupBox_3)
        self.label_31.setGeometry(QtCore.QRect(20, 70, 221, 51))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(40, 40, 371, 141))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_15 = QtGui.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(280, 23, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.line_2 = QtGui.QFrame(self.groupBox_5)
        self.line_2.setGeometry(QtCore.QRect(240, 0, 20, 161))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.groupBox_5)
        self.line_3.setGeometry(QtCore.QRect(250, 70, 118, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(60, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(270, 89, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_11 = QtGui.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(50, 120, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.maskLabel = QtGui.QLabel(self.groupBox_4)
        self.maskLabel.setGeometry(QtCore.QRect(40, 240, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.maskLabel.setFont(font)
        self.maskLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.maskLabel.setObjectName(_fromUtf8("maskLabel"))
        self.importButton = QtGui.QPushButton(self.groupBox_4)
        self.importButton.setGeometry(QtCore.QRect(200, 240, 75, 23))
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.exportButton = QtGui.QPushButton(self.groupBox_4)
        self.exportButton.setGeometry(QtCore.QRect(290, 240, 75, 23))
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(40, 270, 661, 16))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.upperLimitButton = QtGui.QRadioButton(self.groupBox_4)
        self.upperLimitButton.setGeometry(QtCore.QRect(390, 240, 82, 17))
        self.upperLimitButton.setObjectName(_fromUtf8("upperLimitButton"))
        self.lowerLimitButton = QtGui.QRadioButton(self.groupBox_4)
        self.lowerLimitButton.setGeometry(QtCore.QRect(480, 240, 82, 17))
        self.lowerLimitButton.setObjectName(_fromUtf8("lowerLimitButton"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(580, 240, 61, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1162, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.menu.addAction(self.action_Exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ViewerSecond", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Source", None))
        self.pushButton.setText(_translate("MainWindow", "...", None))
        self.label_4.setText(_translate("MainWindow", "Port", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "COM1", None))
        self.label.setText(_translate("MainWindow", "Load a log file", None))
        self.pushButton_2.setText(_translate("MainWindow", "Start", None))
        self.pushButton_3.setText(_translate("MainWindow", "Connect", None))
        self.pushButton_4.setText(_translate("MainWindow", "Stop", None))
        self.label_3.setText(_translate("MainWindow", "Sample rate", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "2 measurements per second", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "1 measurement per second", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "1 measurement every 2 seconds", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "1 measurement every 5 seconds", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "1 measurement every 10 seconds", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "1 measurement every minute", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "1 measurement every 2 minutes", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "1 measurement every 5 minutes", None))
        self.comboBox.setItemText(8, _translate("MainWindow", "1 measurement every 10 minutes", None))
        self.label_5.setText(_translate("MainWindow", "1. Disconnected mode", None))
        self.label_6.setText(_translate("MainWindow", "2. Connected mode", None))
        self.pushButton_5.setText(_translate("MainWindow", "Restart", None))
        self.label_24.setText(_translate("MainWindow", "Select output ", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "ACV", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "DCV", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "ACC", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "DCC", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "R", None))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "CT", None))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "LLI", None))
        self.label_29.setText(_translate("MainWindow", "Send range option", None))
        self.label_9.setText(_translate("MainWindow", "LCD Brightness", None))
        self.pushButton_6.setText(_translate("MainWindow", "+", None))
        self.pushButton_7.setText(_translate("MainWindow", "-", None))
        self.pushButton_8.setText(_translate("MainWindow", "Reset", None))
        self.powerSaveButton.setText(_translate("MainWindow", "Power Save Mode", None))
        self.pauseAcqButton.setText(_translate("MainWindow", "Pause", None))
        self.resumeAcqButton.setText(_translate("MainWindow", "Resume", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Multimeter", None))
        self.label_25.setText(_translate("MainWindow", "Time stamp", None))
        self.label_28.setText(_translate("MainWindow", "-----", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Mouse position", None))
        self.label_30.setText(_translate("MainWindow", "---", None))
        self.label_31.setText(_translate("MainWindow", "---", None))
        self.label_2.setText(_translate("MainWindow", "---", None))
        self.label_15.setText(_translate("MainWindow", "-", None))
        self.label_7.setText(_translate("MainWindow", "---", None))
        self.label_8.setText(_translate("MainWindow", "---", None))
        self.label_11.setText(_translate("MainWindow", "Normal", None))
        self.maskLabel.setText(_translate("MainWindow", "Mask Testing", None))
        self.importButton.setText(_translate("MainWindow", "Import", None))
        self.exportButton.setText(_translate("MainWindow", "Export", None))
        self.label_13.setText(_translate("MainWindow", "-----", None))
        self.upperLimitButton.setText(_translate("MainWindow", "Upper Limit", None))
        self.lowerLimitButton.setText(_translate("MainWindow", "Lower Limit", None))
        self.label_12.setText(_translate("MainWindow", "---", None))
        self.groupBox.setTitle(_translate("MainWindow", "Stripchart", None))
        self.menu.setTitle(_translate("MainWindow", "File", None))
        self.action_Exit.setText(_translate("MainWindow", "Exit", None))

import viewerSecond_rc