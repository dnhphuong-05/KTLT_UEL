from math import sqrt
from PyQt6 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi('haizzz.ui', self)
        self.lien_ket_nut_lenh()
        self.show()

    def lien_ket_nut_lenh(self):
        self.kq.clicked.connect(self.giai_pt_bac2)

    def giai_pt_bac2(self):
        # Kiểm tra dữ liệu nhập vào
        if not self.nhapa.text() or not self.nhapb.text() or not self.nhapc.text():
            self.hienthikq.setText("Vui lòng nhập đầy đủ các hệ số!")
            return

        try:
            # Chuyển đổi dữ liệu nhập sang số thực
            a = float(self.nhapa.text())
            b = float(self.nhapb.text())
            c = float(self.nhapc.text())

            # Giải phương trình bậc 2
            if a == 0:
                if b == 0:
                    if c == 0:
                        self.hienthi.setText("Phương trình vô số nghiệm")
                    else:
                        self.hienthi.setText("Phương trình vô nghiệm")
                else:
                    x = -c / b
                    self.hienthi.setText(f"Phương trình có nghiệm x = {x}")
            else:
                delta = b ** 2 - 4 * a * c
                if delta > 0:
                    x1 = (-b - sqrt(delta)) / (2 * a)
                    x2 = (-b + sqrt(delta)) / (2 * a)
                    self.hienthi.setText(f"Phương trình có 2 nghiệm: x1 = {x1}, x2 = {x2}")
                elif delta == 0:
                    x = -b / (2 * a)
                    self.hienthi.setText(f"Phương trình có nghiệm kép x = {x}")
                else:
                    self.hienthi.setText("Phương trình vô nghiệm")

        except ValueError:
            # Xử lý nếu dữ liệu nhập không hợp lệ
            self.hienthi.setText("Dữ liệu nhập không hợp lệ! Vui lòng nhập số.")

app=QtWidgets.QApplication(sys.argv)
window=Ui()
app.exec()