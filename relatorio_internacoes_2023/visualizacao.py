import os
import pandas as pd
import matplotlib.pyplot as plt

# Definir o caminho base da pasta
base_dir = r"C:\Users\Administrador\Desktop\relatorio_internacoes_2023"
dados_dir = os.path.join(base_dir, "dados")  # Pasta onde estão os CSVs

# Arquivos CSV
arquivos = {
    "altas_por_dia": os.path.join(dados_dir, "altas_por_dia.csv"),
    "altas_por_mes": os.path.join(dados_dir, "altas_por_mes.csv"),
    "internacoes_por_dia": os.path.join(dados_dir, "internacoes_por_dia.csv"),
    "internacoes_por_mes": os.path.join(dados_dir, "internacoes_por_mes.csv"),
}

# Função para carregar os arquivos CSV
def carregar_csv(caminho):
    if os.path.exists(caminho):
        return pd.read_csv(caminho, parse_dates=[0])  # Converte a primeira coluna para data
    else:
        print(f"Arquivo não encontrado: {caminho}")
        return None

# Carregar os dados
df_altas_dia = carregar_csv(arquivos["altas_por_dia"])
df_altas_mes = carregar_csv(arquivos["altas_por_mes"])
df_internacoes_dia = carregar_csv(arquivos["internacoes_por_dia"])
df_internacoes_mes = carregar_csv(arquivos["internacoes_por_mes"])

# Gráfico de linha para internações por mês
plt.figure(figsize=(10, 5))
plt.plot(df_internacoes_mes["mes"], df_internacoes_mes["total_internacoes"], marker='o', linestyle='-', color='blue')
plt.xlabel("Mês")
plt.ylabel("Número de Internações")
plt.title("Internações por Mês")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Gráfico de linha para altas por mês
plt.figure(figsize=(10, 5))
plt.plot(df_altas_mes["mes"], df_altas_mes["total_altas"], marker='o', linestyle='-', color='red')
plt.xlabel("Mês")
plt.ylabel("Número de Altas")
plt.title("Altas por Mês")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Gráfico de linha com internações e altas juntas
plt.figure(figsize=(12, 6))
plt.plot(df_internacoes_mes["mes"], df_internacoes_mes["total_internacoes"], marker='o', linestyle='-', label="Internações", color='blue')
plt.plot(df_altas_mes["mes"], df_altas_mes["total_altas"], marker='s', linestyle='-', label="Altas", color='red')
plt.xlabel("Mês")
plt.ylabel("Número de Pacientes")
plt.title("Internações e Altas por Mês")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de colunas para internações por mês
plt.figure(figsize=(10, 5))
plt.bar(df_internacoes_mes["mes"], df_internacoes_mes["total_internacoes"], color='blue', alpha=0.7)
plt.xlabel("Mês")
plt.ylabel("Número de Internações")
plt.title("Internações por Mês (Barras)")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Gráfico de colunas para altas por mês
plt.figure(figsize=(10, 5))
plt.bar(df_altas_mes["mes"], df_altas_mes["total_altas"], color='red', alpha=0.7)
plt.xlabel("Mês")
plt.ylabel("Número de Altas")
plt.title("Altas por Mês (Barras)")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Gráfico de área para internações por dia
plt.figure(figsize=(12, 6))
plt.fill_between(df_internacoes_dia["dia"], df_internacoes_dia["total_internacoes"], color='blue', alpha=0.5)
plt.plot(df_internacoes_dia["dia"], df_internacoes_dia["total_internacoes"], color='blue', linewidth=2)
plt.xlabel("Data")
plt.ylabel("Número de Internações")
plt.title("Internações por Dia")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Gráfico de área para altas por dia
plt.figure(figsize=(12, 6))
plt.fill_between(df_altas_dia["dia"], df_altas_dia["total_altas"], color='red', alpha=0.5)
plt.plot(df_altas_dia["dia"], df_altas_dia["total_altas"], color='red', linewidth=2)
plt.xlabel("Data")
plt.ylabel("Número de Altas")
plt.title("Altas por Dia")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
