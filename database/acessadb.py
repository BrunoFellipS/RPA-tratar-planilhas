import sqlite3

class Banco_depara:
    def __init__(self):
        self.db = sqlite3.connect(r"T:\DEPARTAMENTOS\AUTOMAÇÃO\DATABASES\Medware\DBatsy.db")
        self.cursor = self.db.cursor()

    def busca(self):
        linha = 0
        self.cursor.execute('SELECT codigo FROM teste')
        teste = self.cursor.fetchall()
        for i in teste:
            ii = i[0]
            print(ii)


bd = Banco_depara()
bd.busca()
