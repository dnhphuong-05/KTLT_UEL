from PyQt6.QtWidgets import QApplication, QMainWindow

from RevisionTDLT.ChuongTrinhDoiTienNgoaiTeSangTienViet.tiente_ext import tiente_ext

app=QApplication([])
mainwindow=QMainWindow()
myui=tiente_ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()