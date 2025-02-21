import traceback

from PyQt6.QtWidgets import QMessageBox

from XuLyListCoBan.listcoban import Ui_MainWindow


class listcobanext(Ui_MainWindow):
    def __init__(self):
        self.list_1 = []
        self.list_2 = []
        self.list_merge = []
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()

    def showMainWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlots(self):
        self.pushButton_nhap1.clicked.connect(self.xu_ly_nut_nhap_1)
        self.pushButton_nhap2.clicked.connect(self.xu_ly_nut_nhap_2)
        self.pushButton_sapxep.clicked.connect(self.xu_ly_nut_sap_xep)
        self.pushButton_chen.clicked.connect(self.xu_ly_nut_chen)
        self.pushButton_dem.clicked.connect(self.xu_ly_nut_dem)
        self.pushButton_tron.clicked.connect(self.xu_ly_nut_tron)
        self.pushButton_xoa.clicked.connect(self.xu_ly_nut_xoa)

    def display(self, content,my_list):
        list_str = ""
        for i in range(len(my_list)):
            list_str += str(my_list[i])
            if i < len(my_list) - 1:
                list_str += ","
        self.textEdit_hienthi.append(f"{content}: {list_str}")
    def input_data(self, data, lineEdit, my_list, disc):
        """Nhập list số nguyên từ ô lineEdit_nhaplist1 và lưu vào self.list_1."""
        try:
            # Lấy dữ liệu từ ô nhập liệu
            input_text = lineEdit.text()

            # Chuyển chuỗi thành danh sách các số nguyên
            my_list = list(map(int, input_text.split(',')))
            if disc == 1:
                self.list_1 = my_list
            if disc == 2:
                self.list_2 = my_list
            # Hiển thị kết quả trên textEdit_hienthi
            self.display(f"List {disc} đã nhập", my_list)
        except ValueError:
            # Xử lý lỗi khi nhập dữ liệu không hợp lệ
            self.textEdit_hienthi.append("Vui lòng nhập các số nguyên, cách nhau bởi dấu phẩy!")
    def xu_ly_nut_nhap_1(self):
        data = self.lineEdit_nhaplist1.text()
        self.input_data(data, self.lineEdit_nhaplist1, self.list_1, 1)

    def xu_ly_nut_nhap_2(self):
        data = self.lineEdit_nhaplist2.text()
        self.input_data(data, self.lineEdit_nhaplist2, self.list_2, 2)
    def sort(self, my_list):
        for i in range(len(my_list)):
            for j in range(i+1, len(my_list)):
                if my_list[i] > my_list[j]:
                    my_list[i], my_list[j] = my_list[j], my_list[i]
        return my_list
    def xu_ly_nut_sap_xep(self):
        try:
            msg = QMessageBox()
            msg.setWindowTitle("Confirm")
            msg.setText("Which list do you want to sort ?")
            button_list1 = msg.addButton("List 1", QMessageBox.ButtonRole.ActionRole)  # Nút Tiếp tục
            button_list2 = msg.addButton("List 2", QMessageBox.ButtonRole.ActionRole)
            msg.exec()
            if msg.clickedButton() == button_list1:
                list_sort = self.sort(self.list_1)
                self.display("List 1 đã sắp xếp" , list_sort)
            elif msg.clickedButton() == button_list2:
                list_sort = self.sort(self.list_2)
                self.display("List 2 đã sắp xếp", list_sort)
        except:
            traceback.print_exc()
    def insert(self, data, my_list):
        for i in range(len(my_list)):
            if data < my_list[i]:
                my_list.insert(i, data)
                break
        return my_list
    def xu_ly_nut_chen(self):
        try:
            data_1 = self.lineEdit_nhaplist1.text()
            data_2 = self.lineEdit_nhaplist2.text()
            if data_1 != "":
                data_1 = int(data_1)
                self.list_1 = self.insert(data_1, self.list_1)
                self.display("List 1 đã chèn: ", self.list_1)
            elif data_2 != "":
                data_2 = int(data_2)
                self.list_2 = self.insert(data_2, self.list_2)
                self.display("List 2 đã chèn: ", self.list_2)
        except:
            traceback.print_exc()
    def xu_ly_nut_tron(self):
        try:
            i = 0
            j = 0
            while i < len(self.list_1) and j < len(self.list_2):
                if self.list_2[j] < self.list_1[i]:
                    self.list_merge.append(self.list_2[j])
                    j += 1
                else:
                    self.list_merge.append(self.list_1[i])
                    i += 1
            while i < len(self.list_1):
                self.list_merge.append(self.list_1[i])
                i += 1
            while j < len(self.list_2):
                self.list_merge.append(self.list_2[j])
                j += 1
            self.display("List đã trộn ", self.list_merge)
        except:
            traceback.print_exc()
    def count_asc_child_list(self, my_list, disc):
        count = 0
        length = 1
        for i in range(1, len(my_list)):
            if my_list[i - 1] < my_list[i]:
                length += 1
            else:
                count += (length * (length - 1)) / 2
                length = 1
        count += (length * (length - 1)) / 2
        self.textEdit_hienthi.append(f"So list con tang dan trong list {disc}: {count}")
    def xu_ly_nut_dem(self):
        try:
            msg = QMessageBox()
            msg.setWindowTitle("Confirm")
            msg.setText("Which list do you want to count the children ascending list ?")
            button_list1 = msg.addButton("List 1", QMessageBox.ButtonRole.ActionRole)  # Nút Tiếp tục
            button_list2 = msg.addButton("List 2", QMessageBox.ButtonRole.ActionRole)
            button_list3 = msg.addButton("List Merge", QMessageBox.ButtonRole.ActionRole)
            msg.exec()
            if msg.clickedButton() == button_list1:
                self.count_asc_child_list(self.list_1, "1")
            elif msg.clickedButton() == button_list2:
                self.count_asc_child_list(self.list_2, "2")
            elif msg.clickedButton() == button_list3:
                self.count_asc_child_list(self.list_merge, "merge")
        except:
            traceback.print_exc()
    def delete(self, my_list):
        my_list.clear()
        msg = QMessageBox()
        msg.setWindowTitle("Announce")
        msg.setText(" You deleted list successfully.")
        button_close = msg.addButton("Close", QMessageBox.ButtonRole.DestructiveRole)
        msg.exec()

    def refresh(self):
        self.textEdit_hienthi.clear()
        self.lineEdit_nhaplist1.clear()
        self.lineEdit_nhaplist2.clear()
    def xu_ly_nut_xoa(self):
        try:
            msg = QMessageBox()
            msg.setWindowTitle("Confirm")
            msg.setText("Which list do you want to delete ?")
            button_list1 = msg.addButton("List 1", QMessageBox.ButtonRole.ActionRole)  # Nút Tiếp tục
            button_list2 = msg.addButton("List 2", QMessageBox.ButtonRole.ActionRole)
            msg.exec()
            if msg.clickedButton() == button_list1:
                self.delete(self.list_1)
            elif msg.clickedButton() == button_list2:
                self.delete(self.list_2)
            self.refresh()
        except:
            traceback.print_exc()













