# Form implementation generated from reading ui file 'D:\K234111362\KTLT\RevisionTDLT\ChuongTrinhGiaiPhuongTrinhBac2\haizzz.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(120, 50, 551, 191))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(255, 223, 224);\n"
"border-color: rgb(209, 175, 232);")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(180, 90, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(260, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.nhapa = QtWidgets.QLineEdit(parent=self.groupBox)
        self.nhapa.setGeometry(QtCore.QRect(180, 40, 141, 41))
        self.nhapa.setStyleSheet("background-color: rgb(255, 193, 195);\n"
"border-color: rgb(159, 130, 206);")
        self.nhapa.setObjectName("nhapa")
        self.nhapb = QtWidgets.QLineEdit(parent=self.groupBox)
        self.nhapb.setGeometry(QtCore.QRect(260, 90, 141, 41))
        self.nhapb.setStyleSheet("background-color: rgb(255, 193, 195);")
        self.nhapb.setObjectName("nhapb")
        self.nhapc = QtWidgets.QLineEdit(parent=self.groupBox)
        self.nhapc.setGeometry(QtCore.QRect(340, 140, 141, 41))
        self.nhapc.setStyleSheet("background-color: rgb(255, 193, 195);")
        self.nhapc.setObjectName("nhapc")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 270, 551, 191))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 223, 224);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.kq = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.kq.setGeometry(QtCore.QRect(90, 60, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kq.setFont(font)
        self.kq.setStyleSheet("background-color: rgb(243, 224, 247);")
        self.kq.setObjectName("kq")
        self.hienthi = QtWidgets.QTextEdit(parent=self.groupBox_2)
        self.hienthi.setGeometry(QtCore.QRect(240, 40, 251, 121))
        font = QtGui.QFont()
        font.setKerning(False)
        self.hienthi.setFont(font)
        self.hienthi.setStyleSheet("\n"
"background-color: rgb(239, 243, 255);\n"
"")
        self.hienthi.setObjectName("hienthi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Nhập giá trị"))
        self.label.setText(_translate("MainWindow", "Nhập a"))
        self.label_2.setText(_translate("MainWindow", "Nhập b"))
        self.label_3.setText(_translate("MainWindow", "Nhập c"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Kết quả"))
        self.kq.setText(_translate("MainWindow", "Kết quả"))
