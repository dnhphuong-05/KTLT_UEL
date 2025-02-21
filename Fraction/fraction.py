# Form implementation generated from reading ui file 'D:\K234111362\KTLT\Fraction\fraction.ui'
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
        self.groupBox.setGeometry(QtCore.QRect(60, 30, 681, 521))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("\n"
"background-color: rgb(239, 243, 255);")
        self.groupBox.setObjectName("groupBox")
        self.ketqua = QtWidgets.QTextEdit(parent=self.groupBox)
        self.ketqua.setGeometry(QtCore.QRect(60, 240, 531, 121))
        self.ketqua.setStyleSheet("background-color: rgb(189, 215, 231);")
        self.ketqua.setObjectName("ketqua")
        self.ketthuc = QtWidgets.QPushButton(parent=self.groupBox)
        self.ketthuc.setGeometry(QtCore.QRect(460, 180, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ketthuc.setFont(font)
        self.ketthuc.setStyleSheet("background-color: rgb(159, 130, 206);")
        self.ketthuc.setObjectName("ketthuc")
        self.nhap = QtWidgets.QPushButton(parent=self.groupBox)
        self.nhap.setGeometry(QtCore.QRect(110, 180, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nhap.setFont(font)
        self.nhap.setStyleSheet("background-color: rgb(255, 193, 195);")
        self.nhap.setObjectName("nhap")
        self.nhapps = QtWidgets.QLineEdit(parent=self.groupBox)
        self.nhapps.setGeometry(QtCore.QRect(220, 60, 101, 51))
        self.nhapps.setStyleSheet("background-color: rgb(189, 215, 231);")
        self.nhapps.setObjectName("nhapps")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 60, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(360, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.soluong = QtWidgets.QTextEdit(parent=self.groupBox)
        self.soluong.setGeometry(QtCore.QRect(440, 60, 101, 51))
        self.soluong.setStyleSheet("background-color: rgb(189, 215, 231);")
        self.soluong.setObjectName("soluong")
        self.pushButton_cong = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_cong.setGeometry(QtCore.QRect(80, 380, 93, 28))
        self.pushButton_cong.setStyleSheet("background-color: rgb(243, 224, 247);")
        self.pushButton_cong.setObjectName("pushButton_cong")
        self.pushButton_tru = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_tru.setGeometry(QtCore.QRect(210, 380, 93, 28))
        self.pushButton_tru.setStyleSheet("background-color: rgb(243, 224, 247);")
        self.pushButton_tru.setObjectName("pushButton_tru")
        self.pushButton_nhan = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_nhan.setGeometry(QtCore.QRect(340, 380, 93, 28))
        self.pushButton_nhan.setStyleSheet("background-color: rgb(243, 224, 247);")
        self.pushButton_nhan.setObjectName("pushButton_nhan")
        self.pushButton_chia = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_chia.setGeometry(QtCore.QRect(470, 380, 93, 28))
        self.pushButton_chia.setStyleSheet("background-color: rgb(243, 224, 247);")
        self.pushButton_chia.setObjectName("pushButton_chia")
        self.pushButton_timkiem = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_timkiem.setGeometry(QtCore.QRect(290, 190, 93, 28))
        self.pushButton_timkiem.setStyleSheet("background-color: rgb(243, 224, 247);")
        self.pushButton_timkiem.setObjectName("pushButton_timkiem")
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
        self.groupBox.setTitle(_translate("MainWindow", "Fraction"))
        self.ketthuc.setText(_translate("MainWindow", "Kết thúc"))
        self.nhap.setText(_translate("MainWindow", "Nhập "))
        self.label.setText(_translate("MainWindow", "Nhập phân số"))
        self.label_2.setText(_translate("MainWindow", "Số lượng"))
        self.pushButton_cong.setText(_translate("MainWindow", "Cộng"))
        self.pushButton_tru.setText(_translate("MainWindow", "Trừ"))
        self.pushButton_nhan.setText(_translate("MainWindow", "Nhân"))
        self.pushButton_chia.setText(_translate("MainWindow", "Chia"))
        self.pushButton_timkiem.setText(_translate("MainWindow", "Tìm kiếm"))
