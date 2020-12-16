import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QUrl
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

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
        self.btn.move(0, 750)
        self.btn.clicked.connect(self.open_afisha_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Главная', self)
        self.btn.resize(100, 50)
        self.btn.move(100, 750)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Аккаунт', self)
        self.btn.resize(100, 50)
        self.btn.move(200, 750)
        self.btn.clicked.connect(self.open_account_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Купить билеты', self)
        self.btn.resize(100, 50)
        self.btn.move(300, 750)
        self.btn.clicked.connect(self.open_ticket_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.label_pop = QLabel("   Популярно сейчас в кино", self)
        self.label_pop.move(0, 0)
        self.label_pop.resize(400, 50)
        self.label_pop.setStyleSheet('background-color: #70227E	')

#встраивание видео с ютуба (форма не работает, если работает данный фрагмент кода)
#код встраивания взял от сюда: https://coderoad.ru/48103685/youtube-%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-pyqt

        #QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        #self.centralwid=QtWidgets.QWidget(self)
        #self.vlayout=QtWidgets.QVBoxLayout()
        #self.webview=QtWebEngineWidgets.QWebEngineView()
        #self.webview.setUrl(QUrl("https://www.youtube.com/watch?v=Mq4AbdNsFVw"))
        #self.vlayout.addWidget(self.webview)
        #self.centralwid.setLayout(self.vlayout)
        #self.setCentralWidget(self.centralwid)
        #self.show()



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

#---------------------------------------------------------------
#создаю окно аккаунт

class account_form(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(0, 0, 400, 800)
        self.setWindowTitle('Аккаунт')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

        self.btn = QPushButton('Афиша', self)
        self.btn.resize(100, 50)
        self.btn.move(0, 750)
        self.btn.clicked.connect(self.open_afisha_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Главная', self)
        self.btn.resize(100, 50)
        self.btn.move(100, 750)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Аккаунт', self)
        self.btn.resize(100, 50)
        self.btn.move(200, 750)
        self.btn.clicked.connect(self.open_account_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Купить билеты', self)
        self.btn.resize(100, 50)
        self.btn.move(300, 750)
        self.btn.clicked.connect(self.open_ticket_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.label_pop = QLabel("   Мой профиль", self)
        self.label_pop.move(0, 0)
        self.label_pop.resize(400, 50)
        self.label_pop.setStyleSheet('background-color: #70227E	')

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

#------------------------------------------------------------------------
#создаю окно афиши

class afisha_form (QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(0, 0, 400, 800)
        self.setWindowTitle('Афиша')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

        self.btn = QPushButton('Афиша', self)
        self.btn.resize(100, 50)
        self.btn.move(0, 750)
        self.btn.clicked.connect(self.open_afisha_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Главная', self)
        self.btn.resize(100, 50)
        self.btn.move(100, 750)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Аккаунт', self)
        self.btn.resize(100, 50)
        self.btn.move(200, 750)
        self.btn.clicked.connect(self.open_account_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Купить билеты', self)
        self.btn.resize(100, 50)
        self.btn.move(300, 750)
        self.btn.clicked.connect(self.open_ticket_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('БД', self)
        self.btn.resize(100, 50)
        self.btn.move(300, 500)
        self.btn.clicked.connect(self.open_ex_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.label_pop = QLabel("   Афиша", self)
        self.label_pop.move(0, 0)
        self.label_pop.resize(400, 50)
        self.label_pop.setStyleSheet('background-color: #70227E	')

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

    def open_ex_form(self):
        self.ex_form = ex_form(self, "БД")
        self.ex_form.show()
        self.hide()
#------------------------------------------------------------------------
#создаю окно билетов

class ticket_form (QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(0, 0, 400, 800)
        self.setWindowTitle('Купить билеты')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

        self.btn = QPushButton('Афиша', self)
        self.btn.resize(100, 50)
        self.btn.move(0, 750)
        self.btn.clicked.connect(self.open_afisha_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Главная', self)
        self.btn.resize(100, 50)
        self.btn.move(100, 750)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Аккаунт', self)
        self.btn.resize(100, 50)
        self.btn.move(200, 750)
        self.btn.clicked.connect(self.open_account_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Купить билеты', self)
        self.btn.resize(100, 50)
        self.btn.move(300, 750)
        self.btn.clicked.connect(self.open_ticket_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.label_pop = QLabel("   Покупка билетов", self)
        self.label_pop.move(0, 0)
        self.label_pop.resize(400, 50)
        self.label_pop.setStyleSheet('background-color: #70227E	')

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
#-----------------------------------------------------------------------
#создаю окно о программе

class about_form (QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(0, 0, 400, 800)
        self.setWindowTitle('О программе')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

        self.btn = QPushButton('Афиша', self)
        self.btn.resize(100, 50)
        self.btn.move(0, 750)
        self.btn.clicked.connect(self.open_afisha_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Главная', self)
        self.btn.resize(100, 50)
        self.btn.move(100, 750)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Аккаунт', self)
        self.btn.resize(100, 50)
        self.btn.move(200, 750)
        self.btn.clicked.connect(self.open_account_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.btn = QPushButton('Купить билеты', self)
        self.btn.resize(100, 50)
        self.btn.move(300, 750)
        self.btn.clicked.connect(self.open_ticket_form)
        self.btn.setStyleSheet('background-color: #70227E')

        self.label_pop = QLabel("   О программе", self)
        self.label_pop.move(0, 0)
        self.label_pop.resize(400, 50)
        self.label_pop.setStyleSheet('background-color: #70227E	')

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

#--------------------------------------------------------------------------
#пытаюсь подключить бд

class Ex(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self):
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('films_db.sqlite')
        # И откроем подключение
        db.open()

        # QTableView - виджет для отображения данных из базы
        view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('films')
        model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)

        self.setGeometry(0, 0, 400, 800)
        self.setWindowTitle('Пример работы с QtSql')

#----------------------------------------------------------------------------
#завершение программы

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
