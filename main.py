from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sqlite3
import PyQt5
import sys


# ----------------------------------------------------
# основа всех форм

class BaseForm(QMainWindow):
    def __init__(self):
        super(BaseForm,self).__init__()
        self.initUi()

        self.label = QLabel("Кино", self)
        self.label.move(0, 0)


    def initUi(self):
        self.setGeometry(0, 0, 400, 800)
        self.setWindowTitle("Кинотеатр")

# кнопки

        self.btn_afisha = QPushButton('Афиша', self)
        self.btn_afisha.resize(100, 50)
        self.btn_afisha.move(0, 750)
        self.btn_afisha.clicked.connect(self.open_afisha_form)
        self.btn_afisha.setStyleSheet('background-color: #8E5094')

        self.btn_first = QPushButton('Главная', self)
        self.btn_first.resize(100, 50)
        self.btn_first.move(100, 750)
        self.btn_first.clicked.connect(self.open_first_form)
        self.btn_first.setStyleSheet('background-color: #8E5094')

        self.btn_acc = QPushButton('Аккаунт', self)
        self.btn_acc.resize(100, 50)
        self.btn_acc.move(200, 750)
        self.btn_acc.clicked.connect(self.open_account_form)
        self.btn_acc.setStyleSheet('background-color: #8E5094')

        self.btn_buy = QPushButton('Купить билеты', self)
        self.btn_buy.resize(100, 50)
        self.btn_buy.move(300, 750)
        self.btn_buy.clicked.connect(self.open_ticket_form)
        self.btn_buy.setStyleSheet('background-color: #8E5094')

# функции

    def open_account_form(self):
        self.account_form = account_form(self, "Аккаунт")
        self.account_form.show()
        self.hide()

    def open_afisha_form(self):
        self.afisha_form = afisha_form(self, "Афиша")
        self.afisha_form.show()
        self.hide()

    def open_ticket_form(self):
        self.ticket_form = ticket_form(self, "Билеты")
        self.ticket_form.show()
        self.hide()

    def open_first_form(self):
        self.first_form = first_form(self, "Главная страница")
        self.first_form.show()
        self.hide()
# -------------------------------------------------------------
# форма "Популярное"

class FirstForm(BaseForm):
    def initUi(self):
        super(FirstForm, self).initUi()
        self.setGeometry(0, 0, 400, 800)
        self.setWindowTitle("Кинотеатр")


# --------------------------------------------------------------
# форма "Афиша"

class AfishaForm(BaseForm):
    def initUi(self):
        super(AfishaForm, self).initUi()
        self.db = sqlite3.connect("films_db.sqlite")


        def get_film(self):
            cur = self.con.cursor()
            data = cur.execute("""SELECT film FROM films WHERE year = 2004""").fetchall()
            self.label.setText(str(data[0]))




# ----------------------------------------------------------------
# завершение программы

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = FirstForm()
    form.show()
    sys.exit(app.exec())