import psycopg2
import pandas as pd
from conexao import conectar
import os

def executar_consulta(query, arquivo):
    conn = conectar()
    if conn is None:
        return None
    
    try:
        # Executa a consulta e armazena em um DataFrame
        df = pd.read_sql_query(query, conn)
        
        # Definindo o caminho para salvar o CSV
        caminho_csv = os.path.join(os.path.dirname(__file__), '..', 'dados', arquivo)
        
        # Salvando o DataFrame em um arquivo CSV
        df.to_csv(caminho_csv, index=False)
        
        return df
    except Exception as e:
        print(f'Erro ao executar consulta: {e}')
    finally:
        conn.close()

def inernacoes_por_dia():
    query = """
    SELECT DATE_TRUNC('day', data_atendimento)::date AS dia, COUNT(*) AS total_internacoes
    FROM sigh.ficha_amb_int
    WHERE data_atendimento IS NOT null
    AND EXTRACT(year FROM data_alta) = 2023
    GROUP BY dia
    ORDER BY dia;
    """
    # Salva os dados da consulta em 'internacoes_por_dia.csv'
    return executar_consulta(query, 'internacoes_por_dia.csv')

def altas_por_dia():
    query = """
    SELECT DATE_TRUNC('day', data_alta)::date AS dia, COUNT(*) AS total_altas
    FROM sigh.ficha_amb_int
    WHERE data_alta IS NOT NULL
    AND EXTRACT(year FROM data_alta) = 2023
    GROUP BY dia 
    ORDER BY dia;
    """
    # Salva os dados da consulta em 'altas_por_dia.csv'
    return executar_consulta(query, 'altas_por_dia.csv')

def internacoes_por_mes():
    query = """
    SELECT DATE_TRUNC('month', data_atendimento)::date AS mes, COUNT(*) AS total_internacoes
    FROM sigh.ficha_amb_int
    WHERE data_atendimento IS NOT NULL
    AND EXTRACT(year FROM data_atendimento) = 2023
    GROUP BY mes
    ORDER BY mes;
    """
    # Salva os dados da consulta em 'internacoes_por_mes.csv'
    return executar_consulta(query, 'internacoes_por_mes.csv')

def altas_por_mes():
    query = """
    SELECT DATE_TRUNC('month', data_alta)::date AS mes, COUNT(*) AS total_altas
    FROM sigh.ficha_amb_int
    WHERE data_alta IS NOT NULL
    AND EXTRACT(year FROM data_alta) = 2023
    GROUP BY mes
    ORDER BY mes;
    """
    # Salva os dados da consulta em 'altas_por_mes.csv'
    return executar_consulta(query, 'altas_por_mes.csv')



# Executando as consultas e exportando os resultados
df_internacoes_dia = inernacoes_por_dia()
df_altas_dia = altas_por_dia()
df_internacoes_mes = internacoes_por_mes()
df_altas_mes = altas_por_mes()
