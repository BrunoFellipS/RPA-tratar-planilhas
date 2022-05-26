from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import getpass





class Principal:
    def __init__(self):
        self.user = getpass.getuser()
        self.app = QtWidgets.QApplication([])
        self.janela = uic.loadUi('QT/principal.ui')



        self.janela.pushButton_3.clicked.connect(self.buscar)
        self.janela.pushButton.clicked.connect(self.gerar)
        self.janela.pushButton_2.clicked.connect(self.baixa)
        self.janela.pushButton_4.clicked.connect(self.confirmar_empresa)
        self.arquivo = ''
        self.lista_depara = ''

    def confirmar_empresa(self):

        self.empresa = self.janela.comboBox.currentText()
        print(self.empresa)
        print(self.janela.comboBox_2.currentText())

        if self.empresa == 'Escolha uma Opção':
            QMessageBox.about(self.janela, "ALERTA",
                              "Voce não selecionou nenhuma empresa, favor selecionar uma empresa.")
        elif self.empresa == 'Opção1':
            if self.janela.comboBox_2.currentText() == '':
                lista_acao = ["Escolha uma Opreação para Opção1",  "Opção1.1", "Opção1.2"]
                self.janela.comboBox_2.addItems(lista_acao)

            elif self.janela.comboBox_2.currentText() == 'Escolha uma Opreação para Opção2' or "Opção2.1" or "Opção2.2":
                self.janela.comboBox_2.clear()
                lista_acao = ["Escolha uma Opreação para Opção1",  "Opção1.1", "Opção1.2"]
                self.janela.comboBox_2.addItems(lista_acao)
                print(self.janela.comboBox_2.currentText())

        elif self.empresa == "Opção2":
            if self.janela.comboBox_2.currentText() == '':
                lista_acao = ["Escolha uma Opreação para Opção2",  "Opção2.1", "Opção2.2"]
                self.janela.comboBox_2.addItems(lista_acao)

            elif self.janela.comboBox_2.currentText() == 'Escolha uma Opreação para Opção1' or "Opção1.1" or "Opção1.2":
                self.janela.comboBox_2.clear()
                lista_acao = ["Escolha uma Opreação para Opção2",  "Opção2.1", "Opção2.2"]
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
    p = Principal()
    p.janela.show()
    p.app.exec()


