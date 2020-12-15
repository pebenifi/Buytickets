import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 35, 1980, 1920)
        self.setWindowTitle('Главная страница')





        self.btn = QPushButton('Аккаунт', self)
        self.btn.resize(200, 100)
        self.btn.move(0,200)

        self.btn = QPushButton('Афиша', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 0)

        self.btn = QPushButton('Мои Билеты', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 100)

        self.btn = QPushButton('О программе', self)
        self.btn.resize(100, 50)
        self.btn.move(0, 950)






        self.btn.clicked.connect(self.open_second_form)

    def open_second_form(self):
        self.second_form = SecondForm(self, "Данные для второй формы")
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая форма')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
