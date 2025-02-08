import psycopg2
from psycopg2 import sql

def conectar():
    try:
        conn = psycopg2.connect(
            dbname="bd2424",
            user="postgres",
            password="postgres",
            host="192.168.0.105",
            port="5432"
        )
        print("Conexão bem-sucedida!")  # Mensagem de sucesso
        return conn
    
    except Exception as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None

# if __name__== "__main__":
#     conexao = conectar()
#     if conexao:
#         conexao.close()