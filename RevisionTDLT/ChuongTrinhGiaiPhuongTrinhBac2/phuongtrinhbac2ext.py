from RevisionTDLT.ChuongTrinhGiaiPhuongTrinhBac2.haizzz import Ui_MainWindow
from math import sqrt


class phuongtrinhbac2ext(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlots()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlots(self):
        self.kq.clicked.connect(self.xu_ly_pt_bac2)

    def xu_ly_pt_bac2(self):
        if not self.nhapa.text() or not self.nhapb.text() or not self.nhapc.text():
            self.hienthikq.setText("Vui lòng nhập đầy đủ các hệ số!")
            return

        try:
            a = float(self.nhapa.text())
            b = float(self.nhapb.text())
            c = float(self.nhapc.text())
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
            self.hienthi.setText("Dữ liệu nhập không hợp lệ! Vui lòng nhập số.")

