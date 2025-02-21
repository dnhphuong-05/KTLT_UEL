from PyQt6.QtWidgets import QApplication, QMainWindow

from Fraction.fractionext import fractionext

app=QApplication([])
mainwindow=QMainWindow()
myui=fractionext()
myui.setupUi(mainwindow)
myui.showMainWindow()
app.exec()