from Fraction.fraction import Ui_MainWindow


class fractionext(Ui_MainWindow):
    def __init__(self):
        self.spt=0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlots()

    def showMainWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlots(self):
        self.nhap.clicked.connect(self.xu_ly_phan_so)
        self.pushButton_timkiem.clicked.connect(self.xu_ly_nut_tim_kiem)
        self.pushButton_cong.clicked.connect(self.xu_ly_nut_cong)
        self.pushButton_tru.clicked.connect(self.xu_ly_nut_tru)
        self.pushButton_nhan.clicked.connect(self.xu_ly_nut_nhan)
        self.pushButton_chia.clicked.connect(self.xu_ly_nut_chia)

    def xu_ly_phan_so(self):
        n=self.nhapps.text()
        tach=n.split("/")
        ts=int(tach[0])
        ms=int(tach[1])
        ps1=[ts,ms]
        self.spt+=1
        self.soluong.setText(str(self.spt))
        print(ts,ms)

    def xu_ly_nut_tim_kiem(self):
        pass

    def xu_ly_nut_cong(self):
        pass

    def xu_ly_nut_tru(self):
        pass

    def xu_ly_nut_nhan(self):
        pass

    def xu_ly_nut_chia(self):
        pass
