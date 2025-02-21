from math import sqrt
from PyQt6 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi('hoanhao.ui', self)
        self.show()
        self.lien_ket_nut_lenh()
        self.show()

    def lien_ket_nut_lenh(self):
        self.timsohoanhao.clicked.connect(self.xu_ly_so_hoan_hao)

    def xu_ly_so_hoan_hao(self):
        try:
            n = int(self.gioihan.text())
            if n < 2:
                self.insohoanhao.setText("Không có số hoàn hảo nào.")
                return
            so_hoan_hao = []
            for num in range(2, n + 1):
                if self.kiem_tra_so_hoan_hao(num):
                    so_hoan_hao.append(num)
            if so_hoan_hao:
                result = ", ".join(map(str, so_hoan_hao))
                self.insohoanhao.setText(f"Các số hoàn hảo nhỏ hơn hoặc bằng {n} là: {result}")
            else:
                self.insohoanhao.setText("Không có số hoàn hảo nào.")
        except ValueError:
            self.insohoanhao.setText("Vui lòng nhập một số nguyên hợp lệ.")

    def kiem_tra_so_hoan_hao(self, num):
        uoc_so = [i for i in range(1, num) if num % i == 0]
        return sum(uoc_so) == num


app=QtWidgets.QApplication(sys.argv)
window=Ui()
app.exec()