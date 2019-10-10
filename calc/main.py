import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui import Ui_MainWindow


READY = 0
INPUT = 1


class APP_ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.memory = 0
        self.history= [0]
        self.dott = 0
        self.count = 1
        self.setFixedSize(self.size())
        for i in range(0,10):
            print(i)
            getattr(self,'pushButton_%s' % i).pressed.connect(lambda v=i: self.input_number(v))
        self.reset()
        self.pushButton_plus.pressed.connect(lambda:self.operation('+'))
        self.pushButton_div.pressed.connect(lambda:self.operation('/'))
        self.pushButton_minus.pressed.connect(lambda:self.operation('-'))
        self.pushButton_multi.pressed.connect(lambda:self.operation('*'))
        self.pushButton_equal.pressed.connect(lambda:self.equal())
        self.pushButton_reset.pressed.connect(lambda:self.reset())
        self.pushButton_negative.pressed.connect(lambda:self.negative())
        self.pushButton_delete.pressed.connect(lambda:self.delete())
        self.pushButton_times.pressed.connect(lambda:self.operation("^"))
        self.pushButton_10.pressed.connect(lambda:self.dot())
        
    def input_number(self,num): 
        if self.state == READY:
            self.history.append(num)
            self.state = INPUT
            self.memory = num
        else:
            if self.dott == 1:
                self.count *= 10
                if self.history[-1] >= 0:
                    self.history[-1] = self.history[-1] + num/self.count
                else:
                    self.history[-1] = self.history[-1] - num/10
                self.memory = self.memory*10 + num
            else:
                if self.history[-1] >= 0:
                    self.history[-1] = self.history[-1] * 10 + num
                else:
                    self.history[-1] = self.history[-1] * 10 - num
                self.memory = self.memory*10 + num
        self.display()

    def display(self):
        self.lcdNumber.display(self.history[-1])

    def negative(self):
        if self.state == INPUT:
            self.history[-1] *= -1
            self.display()

    def delete(self):
        print("delete")
        if self.state == INPUT:
            self.history[-1] = self.history[-1]//10
            self.display()
        if self.history[-1] == 0:
            self.dott = 0

    def dot(self):
        if self.state == INPUT:
                self.dott = 1
        print(self.dott)
    def reset(self):
        print('reset')
        self.state = READY
        self.oper = 0
        self.memory = None
        self.current_oper = READY
        self.history = ['0']
        self.display()
        self.dott = 0
        self.count = 1
        
    def operation(self, oper):
        if self.current_oper == INPUT:
            print('hz')
            self.equal()
            self.history.append(oper)
        if self.state == INPUT:
            self.history.append(oper)
            self.state = READY
            self.current_oper = INPUT
            self.memory = None
            self.dott = 0
            self.count = 1
            print(oper, self.current_oper)
        
    def equal(self):
        print(self.memory, self.current_oper, self.history)
        if self.memory != None or self.current_oper == READY:
            if self.history[-2] == "+":
                self.history.append(self.history[-3] + self.history[-1])
            if self.history[-2] == "-":
                self.history.append(self.history[-3] - self.history[-1])
            if self.history[-2] == "/":
                try:
                    self.history.append(self.history[-3] / self.history[-1])
                except ZeroDivisionError:
                    self.reset()
                    return
            if self.history[-2] == "*":
                self.history.append(self.history[-3] * self.history[-1])
            if self.history[-2] == "^":
                self.history.append(self.history[-3] ** self.history[-1])
            self.state = READY
            print(self.history)
            self.display() 
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = APP_ui()
    ex.setWindowTitle("Калькулятор")
    ex.show()
    sys.exit(app.exec_())
