from PyQt5 import uic, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import time
import getpass

class Login:
    def __init__(self):

        self.app = QtWidgets.QApplication([])
        self.login = uic.loadUi('QT/login_janela.ui')
        self.login.pushButton.clicked.connect(self.entrar)




        self.user = getpass.getuser()

        #coneção ao banco para validação
        db = sqlite3.connect(rf'C:\Users\{self.user}\Documents\RPA-tratar-planilhas\database\DBlogin.db')
        self.cursor = db.cursor()
        self.cursor.execute('SELECT login, senha '
                            'FROM LOGINS')
        self.lista_logins = self.cursor.fetchall()
        # print(self.lista_logins)

        #segubda janela
        self.user = getpass.getuser()
        self.app1 = QtWidgets.QApplication([])
        self.janela = uic.loadUi('QT/principal.ui')
        lista_opcao1 = ['Escolha uma Opção', 'Opção1', 'Opção2']
        self.janela.comboBox.addItems(lista_opcao1)
        self.janela.pushButton_3.clicked.connect(self.buscar)
        self.janela.pushButton.clicked.connect(self.gerar)
        self.janela.pushButton_2.clicked.connect(self.baixa)
        self.janela.pushButton_4.clicked.connect(self.confirmar_empresa)
        self.arquivo = ''
        self.lista_depara = ''



    def entrar(self):
        login = self.login.lineEdit.text()
        senha = self.login.lineEdit_2.text()
        conection = (f'{login}', f'{senha}')
        if login == '' or senha == '':
            if login == '':
                QMessageBox.about(self.login, "ALERTA", "Ei, digite o usuario por favor!!")

            elif senha == '':
                QMessageBox.about(self.login, "ALERTA", "Digite o senha por favor!!")

        else:
            if conection in self.lista_logins:
                if self.login.radioButton.isChecked():
                    print('opção1')
                if self.login.radioButton_2.isChecked():
                    self.login.close()
                    # segunda janela
                    self.janela.show()

                if self.login.radioButton_3.isChecked():
                    print('opção2')
                if self.login.radioButton_4.isChecked():
                    print('opção3')
            else:
                LS_erro = QMessageBox()
                LS_erro.setIcon(QMessageBox.Warning)
                LS_erro.setText('Usuario ou Senha Incorreto')
                LS_erro.setInformativeText('Por favor, insira um usuario e senha corretos')
                LS_erro.setWindowTitle('Login Incorreto')
                # LS_erro.setStandardButtons(QMessageBox.Ok)
                LS_erro.setDefaultButton(QMessageBox.Ok)
                LS_erro.exec_()

    def confirmar_empresa(self):

        self.empresa = self.janela.comboBox.currentText()
        print(self.empresa)
        print(self.janela.comboBox_2.currentText())

        if self.empresa == 'Escolha uma Opção':
            QMessageBox.about(self.janela, "ALERTA",
                              "Voce não selecionou nenhuma empresa, favor selecionar uma empresa.")
        elif self.empresa == 'Opção1':
            if self.janela.comboBox_2.currentText() == '':
                lista_acao = ["Escolha uma Opreação para Opção1", "Opção1.1", "Opção1.2"]
                self.janela.comboBox_2.addItems(lista_acao)

            elif self.janela.comboBox_2.currentText() == 'Escolha uma Opreação para Opção2' or "Opção2.1" or "Opção2.2":
                self.janela.comboBox_2.clear()
                lista_acao = ["Escolha uma Opreação para Opção1", "Opção1.1", "Opção1.2"]
                self.janela.comboBox_2.addItems(lista_acao)
                print(self.janela.comboBox_2.currentText())

        elif self.empresa == "Opção2":
            if self.janela.comboBox_2.currentText() == '':
                lista_acao = ["Escolha uma Opreação para Opção2", "Opção2.1", "Opção2.2"]
                self.janela.comboBox_2.addItems(lista_acao)

            elif self.janela.comboBox_2.currentText() == 'Escolha uma Opreação para Opção1' or "Opção1.1" or "Opção1.2":
                self.janela.comboBox_2.clear()
                lista_acao = ["Escolha uma Opreação para Opção2", "Opção2.1", "Opção2.2"]
                self.janela.comboBox_2.addItems(lista_acao)

    def buscar(self):
        self.arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]
        print(self.arquivo)
        self.janela.lineEdit.setText(self.arquivo)
        self.janela.label_2.setText('')

    def gerar(self):
        self.empresa = self.janela.comboBox.currentText()
        print(self.empresa)
        if self.arquivo == '':
            QMessageBox.about(self.janela, "ALERTA",
                              "Nenhum arquivo selecionado, favor selecionar um arquivo  para continuar.")

        else:
            print('Entrou na Opção')
            if self.empresa == 'Opção1':
                print('entrou na Opção1.2')
                self.Opcao1()

            elif self.empresa == 'Opção2':

                self.Opcao2()

            elif self.empresa == 'Escolha uma Opção':
                QMessageBox.about(self.janela, "ALERTA",
                                  "Nenhuma opção secundaria selecionada, favor selecionar alguma opção secundaria  para continuar.")

    def Opcao1(self):

        print('Opcao1')

    def Opcao2(self):
        print('Opcao2')

    def baixa(self):

        nome_arquivo = QtWidgets.QFileDialog.getSaveFileUrl()[0]
        print('nome_arquivo')




if __name__ == '__main__':
    L = Login()
    L.login.show()
    L.app.exec()
