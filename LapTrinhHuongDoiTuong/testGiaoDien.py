from PyQt6.QtWidgets import QApplication, QMainWindow

from LapTrinhHuongDoiTuong.GiaoDienNhapHoaDonExt import GiaoDienNhapHoaDonExt

app=QApplication([])
Mainwindow=QMainWindow()
myui=GiaoDienNhapHoaDonExt()
myui.setupUi(Mainwindow)
myui.showMainWindow()
app.exec()