from PyQt6.QtWidgets import QApplication, QMainWindow

from RevisionTDLT.ChuongTrinhGiaiPhuongTrinhBac2.phuongtrinhbac2ext import phuongtrinhbac2ext

app=QApplication([])
mainwindow=QMainWindow()
myui=phuongtrinhbac2ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()