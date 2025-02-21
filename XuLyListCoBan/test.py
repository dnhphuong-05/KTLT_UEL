from PyQt6.QtWidgets import QApplication, QMainWindow

from XuLyListCoBan.listcobanext import listcobanext

app=QApplication([])
mainwindow=QMainWindow()
myui=listcobanext()
myui.setupUi(mainwindow)
myui.showMainWindow()
app.exec()