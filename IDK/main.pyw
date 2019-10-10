import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui import Ui_MainWindow
from def_db import *
from ui_add import Ui_Dialog

numbers = (0,1,2,3,4,5,6,7,8,9)


class APP_ui_add(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_ok.pressed.connect(self.add_data)
    def add_data(self):
        for i in self.lineEdit.text():
            print(i)
            if i in int(numbers):
                self.error_message()    
        try:
            insert_data(self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text())
        except ValueError:
            self.error_message()
        else:
            self.destroy()
            ex.fill_table(read_db())
    def error_message(self):
        msg = QMessageBox()
        msg.setText("Error")
        msg.setInformativeText('Incorrect values')
        msg.setWindowTitle("Error")
        msg.exec_()
        
class APP_ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_table(read_db())
        self.pushButton_add.pressed.connect(self.add_data_btn)
        self.pushButton_delete.pressed.connect(self.delete_data_btn)
        
    def fill_table(self, st):
        _translate = QCoreApplication.translate
        self.tableWidget.setRowCount(len(st))
        for row_number , row_data in enumerate(st):      
            for column_number, column_data  in enumerate(row_data):
                if column_number != 0:
                    self.tableWidget.setItem(row_number,column_number-1, QTableWidgetItem(str(column_data)))
                else:
                    self.tableWidget.setVerticalHeaderItem(row_number, QTableWidgetItem(str(row_data[0])))
    def add_data_btn(self):
        self.window_add = APP_ui_add()
        self.window_add.show()

    def delete_data_btn(self):

        text, ok = QInputDialog.getText(self, 'Delete data',
            'Enter ID:')

        if ok:
            delete_data(text)
            self.fill_table(read_db())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = APP_ui()
    ex.setWindowTitle("DB")
    ex.show()
    sys.exit(app.exec_())
