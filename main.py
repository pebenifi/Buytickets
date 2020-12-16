import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

#-------------------------------------------------------
#создаю главное окно

class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 400, 800)
        self.setWindowTitle('Главная страница')

        self.btn = QPushButton('Афиша', self)
        self.btn.resize(100, 50)
        self.btn.move(0,750)
        self.btn.clicked.connect(self.open_afisha_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Главная', self)
        self.btn.resize(100, 50)
        self.btn.move(100, 750)
        self.btn.clicked.connect(self.open_first_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Аккаунт', self)
        self.btn.resize(100, 50)
        self.btn.move(200,750)
        self.btn.clicked.connect(self.open_account_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Мои билеты', self)
        self.btn.resize(100, 50)
        self.btn.move(300, 750)
        self.btn.clicked.connect(self.open_ticket_form)
        self.btn.setStyleSheet('background-color: #70227E')




        self.label_pop = QLabel("   популярно сейчас в кино", self)
        self.label_pop.move(0,0)
        self.label_pop.resize(400, 50)
        self.label_pop.setStyleSheet('background-color: #70227E	')





    def open_account_form(self):
        self.account_form = account_form(self, "Данные для второй формы")
        self.account_form.show()
        self.hide()

    def open_afisha_form(self):
        self.afisha_form = afisha_form(self, "Данные для второй формы")
        self.afisha_form.show()

    def open_ticket_form(self):
        self.ticket_form = ticket_form(self, "Данные для второй формы")
        self.ticket_form.show()

    def open_first_form(self):
        self.first_form = first_form(self, "Данные для второй формы")
        self.first_form.show()
#---------------------------------------------------------------
#создаю окно аккаунт

class account_form(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(0, 35, 1980, 1920)
        self.setWindowTitle('Аккаунт')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

        self.btn = QPushButton('Афиша', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 0)
        self.btn.clicked.connect(self.open_afisha_form)

        self.btn = QPushButton('Мои билеты', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 100)
        self.btn.clicked.connect(self.open_ticket_form)

        self.btn = QPushButton('Главная страница', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 200)
        self.btn.clicked.connect(self.open_first_form)

        self.btn = QPushButton('О программе', self)
        self.btn.resize(100, 50)
        self.btn.move(0, 950)
        self.btn.clicked.connect(self.open_about_form)


    def open_afisha_form(self):
        self.afisha_form = afisha_form(self, "Данные для второй формы")
        self.afisha_form.show()

    def open_ticket_form(self):
        self.ticket_form = ticket_form(self, "Данные для второй формы")
        self.ticket_form.show()

    def open_about_form(self):
        self.about_form = about_form(self, "Данные для второй формы")
        self.about_form.show()

    def open_first_form(self):
        self.first_form = first_form(self, "Данные для второй формы")
        self.first_form.show()



        self.btn = QPushButton('Афиша', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 0)
        self.btn.clicked.connect(self.open_afisha_form)


        self.btn = QPushButton('Мои билеты', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 100)
        self.btn.clicked.connect(self.open_ticket_form)

        self.btn = QPushButton('Главная страница', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 300)
        self.btn.clicked.connect(self.open_first_form)

        self.btn = QPushButton('О программе', self)
        self.btn.resize(100, 50)
        self.btn.move(0, 950)
        self.btn.clicked.connect(self.open_about_form)

#------------------------------------------------------------------------
#создаю окно афиши

class afisha_form (QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(0, 35, 1980, 1920)
        self.setWindowTitle('Афиша')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

        self.btn = QPushButton('Аккаунт', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 0)
        self.btn.clicked.connect(self.open_account_form)

        self.btn = QPushButton('Мои билеты', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 100)
        self.btn.clicked.connect(self.open_ticket_form)

        self.btn = QPushButton('Главная страница', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 200)
        self.btn.clicked.connect(self.open_first_form)

        self.btn = QPushButton('О программе', self)
        self.btn.resize(100, 50)
        self.btn.move(0, 950)
        self.btn.clicked.connect(self.open_about_form)

    def open_account_form(self):
        self.account_form = account_form(self, "Данные для второй формы")
        self.account_form.show()

    def open_ticket_form(self):
        self.ticket_form = ticket_form(self, "Данные для второй формы")
        self.ticket_form.show()

    def open_about_form(self):
        self.about_form = about_form(self, "Данные для второй формы")
        self.about_form.show()

    def open_first_form(self):
        self.first_form = first_form(self, "Данные для второй формы")
        self.first_form.show()

#------------------------------------------------------------------------
#создаю окно билетов

class ticket_form (QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(0, 35, 1980, 1920)
        self.setWindowTitle('Мои билеты')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

        self.btn = QPushButton('Аккаунт', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 100)
        self.btn.clicked.connect(self.open_account_form)

        self.btn = QPushButton('Афиша', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 0)
        self.btn.clicked.connect(self.open_afisha_form)

        self.btn = QPushButton('Главная страница', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 200)
        self.btn.clicked.connect(self.open_first_form)

        self.btn = QPushButton('О программе', self)
        self.btn.resize(100, 50)
        self.btn.move(0, 950)
        self.btn.clicked.connect(self.open_about_form)

    def open_account_form(self):
        self.account_form = account_form(self, "Данные для второй формы")
        self.account_form.show()

    def open_afisha_form(self):
        self.afisha_form = afisha_form(self, "Данные для второй формы")
        self.afisha_form.show()

    def open_about_form(self):
        self.about_form = about_form(self, "Данные для второй формы")
        self.about_form.show()

    def open_first_form(self):
        self.first_form = first_form(self, "Данные для второй формы")
        self.first_form.show()
#-----------------------------------------------------------------------
#создаю окно о программе

class about_form (QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(0, 35, 1980, 1920)
        self.setWindowTitle('О программе')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

        self.btn = QPushButton('Аккаунт', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 200)
        self.btn.clicked.connect(self.open_account_form)

        self.btn = QPushButton('Афиша', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 0)
        self.btn.clicked.connect(self.open_afisha_form)

        self.btn = QPushButton('Мои билеты', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 100)
        self.btn.clicked.connect(self.open_ticket_form)

        self.btn = QPushButton('Главная страница', self)
        self.btn.resize(200, 100)
        self.btn.move(0, 300)
        self.btn.clicked.connect(self.open_first_form)

    def open_account_form(self):
        self.account_form = account_form(self, "Данные для второй формы")
        self.account_form.show()

    def open_afisha_form(self):
        self.afisha_form = afisha_form(self, "Данные для второй формы")
        self.afisha_form.show()

    def open_ticket_form(self):
        self.ticket_form = ticket_form(self, "Данные для второй формы")
        self.ticket_form.show()

    def open_first_form(self):
        self.first_form = first_form(self, "Данные для второй формы")
        self.first_form.show()



#----------------------------------------------------------------------------
#завершение программы

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
