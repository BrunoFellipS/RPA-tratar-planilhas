import pyodbc
from planilhas.escrevendo import Escrever


class Dominio_conect:
    def __init__(self):
        self.empresa = 548
        dbdominio = pyodbc.connect('DSN=Contabil')
        self.cursor = dbdominio.cursor()
        self.listaentradas = []
        self.listasaidas = []

    def buscando_notas(self, data1, data2):
        dicionario = {}
        self.cursor.execute(f"SELECT codi_emp, dent_ent, nume_ent, codi_for, vprod_ent, codi_ent, vcon_ent "
                            f"FROM externo.bethadba.efentradas "
                            f"WHERE codi_emp = {self.empresa} AND dent_ent BETWEEN '{data1}' AND '{data2}'")
        self.efentradas = self.cursor.fetchall()
        self.cursor.execute(f"SELECT codi_cli, vcon_sai, DATA_ESCRITURACAO, nume_sai, VALOR_DESCONTO_SAI, obse_sai "
                            f"FROM externo.bethadba.efsaidas "
                            f"WHERE codi_emp = {self.empresa} AND DATA_ESCRITURACAO BETWEEN '{data1}' AND '{data2}'")
        # Retorno dos dados extraidos em forma de lista
        self.efsaidas = self.cursor.fetchall()
        print(self.efsaidas)

        # print(self.efentradas)
        # self.contagem = efentradas

        # self.erro = len(efentradas)

    def lendo_notas(self):
        for notas in self.efentradas:
            data = notas[1]
            num_nf = notas[2]
            cod_for = notas[3]
            valor = notas[6]
            cod_ent = notas[5]
            data_br = f'{data:%d/%m/%Y}'
            # print(num_nf)
            # print(cod_for)
            # print(valor)
            # print(cod_ent)
            # print(data_br)
            # print('-----------------------')
            # print(f'Numero da nf:{num_nf}, Codigo do fornecedor:{cod_for}, '
            #       f'Valor:{valor}, Codigo de entrada:{cod_ent}, Data de entrada:{data_br}')
            tuplaentrada = (data_br, num_nf, valor)
            self.listaentradas.append(tuplaentrada)
        # print('-----------------------')
        for infos in self.efsaidas:
            codigocliente = infos[0]
            valorinicio = infos[1]
            data_escrituracao = infos[2]
            data_escrituracao = f'{data_escrituracao:%d/%m/%Y}'
            chave_de_saida = infos[3]
            desconto = infos[4]
            obs_saida = infos[5]
            valor_final = valorinicio - desconto
            # print(chave_de_saida)
            # print(data_escrituracao)
            # print(codigocliente)
            # print(valor_final)
            # print(obs_saida)
            # print("______________________________________")

            # print(f"A nota de numero: {chave_de_saida}, com a data de escrituração: {data_escrituracao}"
            #       f", emitida para o cliente de codigo{codigocliente}, tinha o valor inical de {valorinicio} e ao receber o desconto de {desconto} teve o valor final de {valor_final}")
            tuplasaidas = (data_escrituracao, chave_de_saida, '', valor_final)
            self.listasaidas.append(tuplasaidas)

        Escrever().escrevendobanco(self.listaentradas, self.listasaidas)



if __name__ == '__main__':
    dc = Dominio_conect()
    dc.buscando_notas('2022-01-01', '2022-01-31')
    dc.lendo_notas()
