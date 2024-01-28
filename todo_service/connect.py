import psycopg2

# Função para criar conexão no banco
class pgConnect():
    def dbConnect(self):
        con = psycopg2.connect(host='localhost', 
                                database='postgres',
                                user='postgres', 
                                password='postgres')
        return con