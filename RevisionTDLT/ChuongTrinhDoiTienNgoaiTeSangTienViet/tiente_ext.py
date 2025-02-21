from RevisionTDLT.ChuongTrinhDoiTienNgoaiTeSangTienViet.tiente import Ui_MainWindow
from PyQt6 import QtWidgets

class tiente_ext(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlots()
        self.exchange_rates = {
            "USD": 25170,
            "EUR": 25298.81,
            "GBP": 30079.78,
            "JPY": 155.75,
            "AUD": 15207.01,
            "SGD": 18042.13,
            "THB": 645.77,
            "HKD": 3181.03,
            "CNY": 3377.75,
            "KRW": 14.94,
        }
        self.donggia.addItems(self.exchange_rates.keys())

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlots(self):
        self.chuyendoi.clicked.connect(self.xu_ly_tien_te)

    def xu_ly_tien_te(self):
        try:
            tien_ngoai_te = float(self.ngoaite.text())
            loai_tien_te = self.donggia.currentText()
            ty_gia_nhap = self.tygia.text().strip()

            if ty_gia_nhap == "":
                ty_gia = self.exchange_rates.get(loai_tien_te, None)
                if ty_gia is None:
                    QtWidgets.QMessageBox.critical(self, "Lỗi",
                                                   f"Không có tỷ giá cho {loai_tien_te}. Vui lòng nhập tỷ giá!")
                    return
            else:
                ty_gia = float(ty_gia_nhap)

            ket_qua = round(tien_ngoai_te * ty_gia,2)
            self.lineEdit_ketqua.setText(f"{ket_qua:} VND")
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Lỗi", "Vui lòng nhập giá trị hợp lệ!")


