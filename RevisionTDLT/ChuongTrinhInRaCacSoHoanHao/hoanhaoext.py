from RevisionTDLT.ChuongTrinhInRaCacSoHoanHao.hoanhao import Ui_MainWindow


class hoanhaoext(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWondow=MainWindow
        self.setupSignalAndSlots()

    def showMainwindow(self):
        self.MainWondow.show()

    def setupSignalAndSlots(self):
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



