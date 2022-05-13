from PyQt5 import uic, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import time
import getpass
from planilhas.leitura import Ler_planilha
from planilhas.escrevendo import Escrever

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
        # print(self.lista_logins)

        #segubda janela
        self.user = getpass.getuser()
        self.app1 = QtWidgets.QApplication([])
        self.janela = uic.loadUi('QT/principal.ui')
        self.janela.pushButton_3.clicked.connect(self.buscar)
        self.janela.pushButton.clicked.connect(self.gerar)
        self.janela.pushButton_2.clicked.connect(self.baixa)
        self.arquivo = ''
        self.text = ''



    def entrar(self):
        login = self.login.lineEdit.text()
        senha = self.login.lineEdit_2.text()
        conection = (f'{login}', f'{senha}')
        if login == '' or senha == '':
            if login == '':
                QMessageBox.about(self.login, "ALERTA", "Ei Colaborador, digite o usuario por favor!!")

            elif senha == '':
                QMessageBox.about(self.login, "ALERTA", "Digite o senha por favor!!")

        else:
            if conection in self.lista_logins:
                if self.login.radioButton.isChecked():
                    print('fiscal')
                if self.login.radioButton_2.isChecked():
                    self.login.close()
                    # segunda janela
                    self.janela.show()

                if self.login.radioButton_3.isChecked():
                    print('Finaceiro')
                if self.login.radioButton_4.isChecked():
                    print('Dp')
            else:
                LS_erro = QMessageBox()
                LS_erro.setIcon(QMessageBox.Warning)
                LS_erro.setText('Usuario ou Senha Incorreto')
                LS_erro.setInformativeText('Por favor, insira um usuario e senha corretos')
                LS_erro.setWindowTitle('Lofin Incorreto')
                # LS_erro.setStandardButtons(QMessageBox.Ok)
                LS_erro.setDefaultButton(QMessageBox.Ok)
                LS_erro.exec_()


    def buscar(self):
        self.arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]
        print(self.arquivo)
        self.janela.lineEdit.setText(self.arquivo)
        self.janela.label_2.setText('')

    def gerar(self):
        empresa = self.janela.comboBox.currentText()
        print(empresa)
        if empresa == "Tratamento Medware":
            if self.arquivo == '':
                QMessageBox.about(self.janela, "ALERTA",
                                  "Nenhum arquivo selecionado, favor selecionar um arquivo  para gerar.")
            else:
                self.conciliar()
        else:
            QMessageBox.about(self.janela, "ALERTA",
                              "Nenhuma modelo selecionada, favor selecionar um modelo  para gerar.")

    def conciliar(self):

        self.text, text_box = Ler_planilha(self.arquivo).ler()
        # print(text)
        time.sleep(2)
        self.janela.label_2.setText('Gerando...')
        i = len(self.text)
        i = i / 100
        i = str(i)
        i = i.split('.')
        i = int(i[0])
        h = 100
        print(i)
        for linha in text_box:
            # print(linha)
            linha = str(linha)
            self.janela.listWidget.addItem(f'{linha}')
        for g in range(h):
            time.sleep(0.01)
            self.janela.progressBar.setValue(g + 1 + i)
        time.sleep(2)
        self.janela.label_2.setText('Arquivo Gerado')
        time.sleep(4)
        self.janela.progressBar.setValue(0)
        self.janela.label_2.setText('Arquivo Gerado')

    def baixa(self):
        if self.text == '':
            QMessageBox.about(self.janela, "ALERTA",
                              "Nenhum arquivo foi gerado, favor gerar um arquivo para poder baixalo.")
        else:
            nome_arquivo = QtWidgets.QFileDialog.getSaveFileUrl()[0]
            nome_arquivo = f'{nome_arquivo}'
            nome_arquivo = nome_arquivo.replace('file:///', '')
            print(nome_arquivo)
            Escrever(nome_arquivo).escrevendo(self.text)


            




if __name__ == '__main__':
    L = Login()
    L.login.show()
    L.app.exec()
