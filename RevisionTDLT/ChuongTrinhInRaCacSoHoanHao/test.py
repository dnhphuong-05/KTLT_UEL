from PyQt6.QtWidgets import QApplication, QMainWindow

from RevisionTDLT.ChuongTrinhInRaCacSoHoanHao.hoanhaoext import hoanhaoext

app=QApplication([])
mainwindow=QMainWindow()
myui=hoanhaoext()
myui.setupUi(mainwindow)
myui.showMainwindow()
app.exec()