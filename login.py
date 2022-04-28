from PyQt5 import uic, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from menu import Principal

class Login:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.login = uic.loadUi('QT/login_janela.ui')
        self.login.pushButton.clicked.connect(self.entrar)

        #coneção ao banco para validação
        db = sqlite3.connect('T:\DEPARTAMENTOS\AUTOMAÇÃO\DATABASES\jeremy\DB_jeremy.db')
        self.cursor = db.cursor()
        self.cursor.execute('SELECT login, senha '
                            'FROM Logins')
        self.lista_logins = self.cursor.fetchall()
        print(self.lista_logins)

        self.janela = uic.loadUi('QT/principal.ui')


    def entrar(self):
        login = self.login.lineEdit.text()
        senha = self.login.lineEdit_2.text()
        conection = (f'{login}', f'{senha}')
        if login == '' or senha == '':
            if login == '':
                QMessageBox.about(self.login, "ALERTA", "Digite o login por favor!!")

            elif senha == '':
                QMessageBox.about(self.login, "ALERTA", "Digite o senha por favor!!")

        else:
            if conection in self.lista_logins:
                self.login.close()
                # segunda janela

                self.janela.show()

            else:
                QMessageBox.about(self.login, "ALERTA", "Login ou Senha INCORRETO")

class Janela2:
    def __init__(self):
        pass

            




if __name__ == '__main__':
    L = Login()
    L.login.show()
    L.app.exec()