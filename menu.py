from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import getpass
from planilhas.leitura import Ler_planilha
from planilhas.escrevendo import Escrever
import time

class Principal:
    def __init__(self):

        self.user = getpass.getuser()
        self.app = QtWidgets.QApplication([])
        self.janela = uic.loadUi('QT/principal.ui')
        self.janela.pushButton_3.clicked.connect(self.buscar)
        self.janela.pushButton.clicked.connect(self.gerar)
        self.janela.pushButton_2.clicked.connect(self.baixa)
        self.arquivo = ''
        self.text = ''

    def buscar(self):
        self.arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]
        print(self.arquivo)
        self.janela.lineEdit.setText(self.arquivo)
        self.janela.label_2.setText('')


    def gerar(self):
        empresa = self.janela.comboBox.currentText()
        print(empresa)
        if empresa == "MEDWARE":
            if self.arquivo == '':
                QMessageBox.about(self.janela, "ALERTA",
                                  "Nenhum arquivo selecionado, favor selecionar um arquivo  para gerar.")
            else:
                self.conciliar()
        else:
            QMessageBox.about(self.janela, "ALERTA",
                              "Nenhuma empresa selecionada, favor selecionar uma empresa  para gerar.")

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
            QMessageBox.about(self.janela, "ALERTA", "Nenhum arquivo foi gerado, favor gerar um arquivo para poder baixalo.")
        else:
            nome_arquivo = QtWidgets.QFileDialog.getSaveFileUrl()[0]
            nome_arquivo = f'{nome_arquivo}'
            print(nome_arquivo)
            Escrever(nome_arquivo).escrevendo(self.text)




if __name__ == '__main__':
    p = Principal()
    p.janela.show()
    p.app.exec()
