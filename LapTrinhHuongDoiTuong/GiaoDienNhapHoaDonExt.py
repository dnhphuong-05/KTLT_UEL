from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QInputDialog
import traceback

from LapTrinhHuongDoiTuong.GiaoDienNhapHoaDon import Ui_DangNgocHoaiPhuong_GiaoDienNhapHoaDon

class Product:
    def __init__(self, proid, name, quantity, price):
        self.productid = proid
        self.name = name
        self.quantity = quantity
        self.price = price

class CProductList:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_amount(self):
        return sum(p.quantity * p.price for p in self.products)

class Invoice:
    def __init__(self, invoice_number):
        self.invoice_number = invoice_number
        self.productlist = CProductList()

    def add_product(self, product):
        self.productlist.add_product(product)

class GiaoDienNhapHoaDonExt(Ui_DangNgocHoaiPhuong_GiaoDienNhapHoaDon):
    def __init__(self):
        self.Invoicelist = []
        self.current_invoice = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()

    def showMainWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlots(self):
        self.pushButton_nhapvao.clicked.connect(self.add_product)
        self.pushButton_taohoadon.clicked.connect(self.generate_invoice)
        self.pushButton_tong.clicked.connect(self.calculate_total)
        self.pushButton_sapxep.clicked.connect(self.sort_invoices)
        self.pushButton_xoahoadon.clicked.connect(self.delete_invoice)
        self.pushButton_capnhat.clicked.connect(self.update_invoice)
        self.pushButton_timkiem.clicked.connect(self.search_invoice)

    def add_product(self):
        try:
            name_id = self.lineEdit_mahang.text().strip()
            name = self.lineEdit_tenhang.text().strip()
            quantity = int(self.lineEdit_soluong.text().strip())
            price = float(self.lineEdit_dongia.text().strip())

            if not self.current_invoice:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Hãy tạo hóa đơn trước khi thêm sản phẩm!")
                return

            product = Product(name_id, name, quantity, price)
            self.current_invoice.add_product(product)

            row_position = self.tableWidget_danhsachhang.rowCount()
            self.tableWidget_danhsachhang.insertRow(row_position)
            self.tableWidget_danhsachhang.setItem(row_position, 0, QTableWidgetItem(name_id))
            self.tableWidget_danhsachhang.setItem(row_position, 1, QTableWidgetItem(name))
            self.tableWidget_danhsachhang.setItem(row_position, 2, QTableWidgetItem(str(quantity)))
            self.tableWidget_danhsachhang.setItem(row_position, 3, QTableWidgetItem(f"{price:.2f}"))

            self.lineEdit_mahang.clear()
            self.lineEdit_tenhang.clear()
            self.lineEdit_soluong.clear()
            self.lineEdit_dongia.clear()
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đúng định dạng dữ liệu!")
        except Exception:
            traceback.print_exc()

    def generate_invoice(self):
        invoice_number = self.lineEdit_mahoadon.text().strip()
        if not invoice_number:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Mã hóa đơn không được để trống!")
            return

        self.current_invoice = Invoice(invoice_number)
        self.Invoicelist.append(self.current_invoice)
        self.tableWidget_danhsachhang.setRowCount(0)  # Reset bảng sản phẩm
        self.lineEdit_mahoadon.clear()
        QMessageBox.information(self.MainWindow, "Thông báo", "Hóa đơn đã được tạo thành công!")

    def calculate_total(self):
        if not self.current_invoice:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không có hóa đơn hiện tại!")
            return

        total = self.current_invoice.productlist.total_amount()
        QMessageBox.information(self.MainWindow, "Tổng giá trị", f"Tổng giá trị hóa đơn: {total:.2f} VND")

    def delete_invoice(self):
        invoice_number, ok = QInputDialog.getText(self.MainWindow, 'Xóa hóa đơn', 'Nhập mã hóa đơn:')
        if ok and invoice_number:
            self.Invoicelist = [inv for inv in self.Invoicelist if inv.invoice_number != invoice_number]
            if self.current_invoice and self.current_invoice.invoice_number == invoice_number:
                self.current_invoice = None
                self.tableWidget_danhsachhang.setRowCount(0)
            QMessageBox.information(self.MainWindow, "Thông báo", "Đã xóa hóa đơn thành công!")
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Mã hóa đơn không hợp lệ!")

    def update_invoice(self):
        invoice_number, ok = QInputDialog.getText(self.MainWindow, 'Sửa hóa đơn', 'Nhập mã hóa đơn:')
        if ok and invoice_number:
            new_invoice_number, ok = QInputDialog.getText(self.MainWindow, 'Sửa hóa đơn', 'Nhập mã hóa đơn mới:')
            if ok and new_invoice_number:
                for invoice in self.Invoicelist:
                    if invoice.invoice_number == invoice_number:
                        invoice.invoice_number = new_invoice_number
                        QMessageBox.information(self.MainWindow, "Thông báo", "Đã sửa hóa đơn thành công!")
                        return
                QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy hóa đơn cần sửa!")
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Mã hóa đơn không hợp lệ!")

    def search_invoice(self):
        invoice_number, ok = QInputDialog.getText(self.MainWindow, 'Tìm kiếm hóa đơn', 'Nhập mã hóa đơn:')
        if ok and invoice_number:
            for invoice in self.Invoicelist:
                if invoice.invoice_number == invoice_number:
                    self.current_invoice = invoice
                    self.tableWidget_danhsachhang.setRowCount(0)  # Reset bảng
                    for product in invoice.productlist.products:
                        row_position = self.tableWidget_danhsachhang.rowCount()
                        self.tableWidget_danhsachhang.insertRow(row_position)
                        self.tableWidget_danhsachhang.setItem(row_position, 0, QTableWidgetItem(product.productid))
                        self.tableWidget_danhsachhang.setItem(row_position, 1, QTableWidgetItem(product.name))
                        self.tableWidget_danhsachhang.setItem(row_position, 2, QTableWidgetItem(str(product.quantity)))
                        self.tableWidget_danhsachhang.setItem(row_position, 3, QTableWidgetItem(f"{product.price:.2f}"))
                    QMessageBox.information(self.MainWindow, "Thông báo", "Đã tìm thấy hóa đơn!")
                    return
            QMessageBox.warning(self.MainWindow, "Thông báo", "Không tìm thấy hóa đơn!")

    def sort_invoices(self):
        self.Invoicelist.sort(key=lambda inv: inv.productlist.total_amount())
        QMessageBox.information(self.MainWindow, "Thông báo", "Đã sắp xếp hóa đơn theo giá trị tăng dần!")