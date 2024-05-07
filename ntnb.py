import pandas as pd
import requests as req
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

HEADERS = {'accept': 'application/json',
           'X-API-Key': '-'}

URL_BASE = 'https://api.fintz.com.br'
PARAMS = { 'pagina': 1, 'tamanho': 3000, 'dataInicio': '2012-04-13', 'dataFim': '2024-04-29' }

codigo = "NTNBP20350515"
endpoint = URL_BASE + f'/titulos-publicos/tesouro/{codigo}/precos/historico'
res = req.get(endpoint, headers=HEADERS, params=PARAMS)
data = res.json()
print(data)

# Extrair os dados da coluna 'dados' e criar um novo DataFrame com esses dados
df_dados = pd.DataFrame(data['dados'])

# Colocar o código NTN-B35 na coluna para facilitar o entendimento
df_dados['codigo'] = 'NTN-B 35'

# Listar as colunas indesejadas para exclusão
colunas_indesejadas = ['taxaJurosVenda', 'puCompra', 'puBase', 'puVenda', 'pagina', 'tamanho', 'total']

# Verificando as colunas antes de ser removida
colunas_existentes = [col for col in colunas_indesejadas if col in df_dados.columns]

df_dados = df_dados.drop(colunas_existentes, axis=1)

# Filtra o Data frame para taxas acima de cada um
df_dados1 = df_dados.query('taxaJurosCompra >= 0.075').reset_index(drop=True)

df_dados2 = df_dados.query('taxaJurosCompra >= 0.070').reset_index(drop=True)

df_dados3 = df_dados.query('taxaJurosCompra >= 0.065').reset_index(drop=True)

df_dados4 = df_dados.query('taxaJurosCompra >= 0.06').reset_index(drop=True)

df_dados5 = df_dados.query('taxaJurosCompra >= 0.055').reset_index(drop=True)

df_dados6 = df_dados.query('taxaJurosCompra >= 0.05').reset_index(drop=True)

df_dados7 = df_dados.query('taxaJurosCompra >= 0.045').reset_index(drop=True)

df_dados8 = df_dados.query('taxaJurosCompra >= 0.040').reset_index(drop=True)

df_dados.reset_index(drop=True, inplace=True)

# Exibir o DataFrame resultante
df_dados

URL_BASE = 'https://api.fintz.com.br'
PARAMS = { 'pagina': 1, 'tamanho': 3000, 'dataInicio': '2010-03-10', 'dataFim': '2012-04-12' }

codigo = "NTNBP20350515"
endpoint = URL_BASE + f'/titulos-publicos/tesouro/{codigo}/precos/historico'
res = req.get(endpoint, headers=HEADERS, params=PARAMS)
data = res.json()
print(data)

# Extrair os dados da coluna 'dados' e criar um novo DataFrame com esses dados
df_dados = pd.DataFrame(data['dados'])

df_dados['codigo'] = 'NTN-B 35'

# Excluir essas colunas
colunas_indesejadas = ['taxaJurosVenda', 'puCompra', 'puBase', 'puVenda', 'pagina', 'tamanho', 'total']

# Verificar se as colunas indesejadas estão presentes no DataFrame antes de tentar removê-las
colunas_existentes = [col for col in colunas_indesejadas if col in df_dados.columns]

df_dados = df_dados.drop(colunas_existentes, axis=1)

# Filtrar o data frame para cada taxa acima de X
df_dados_1 = df_dados.query('taxaJurosCompra >= 0.075').reset_index(drop=True)

df_dados_2 = df_dados.query('taxaJurosCompra >= 0.070').reset_index(drop=True)

df_dados_3 = df_dados.query('taxaJurosCompra >= 0.065').reset_index(drop=True)

df_dados_4 = df_dados.query('taxaJurosCompra >= 0.06').reset_index(drop=True)

df_dados_5 = df_dados.query('taxaJurosCompra >= 0.055').reset_index(drop=True)

df_dados_6 = df_dados.query('taxaJurosCompra >= 0.05').reset_index(drop=True)

df_dados_7 = df_dados.query('taxaJurosCompra >= 0.045').reset_index(drop=True)

df_dados_8 = df_dados.query('taxaJurosCompra >= 0.040').reset_index(drop=True)

df_dados.reset_index(drop=True, inplace=True)

df_dados

data_inicio = "2010-03-10"
data_fim = "2024-04-26"

datas = pd.date_range(start=data_inicio, end=data_fim, freq='B')

dias_uteis = len(datas)

print(dias_uteis)

# Calcular o total de registros de cada DataFrame
total_registros1 = len(df_dados1)
total_registros_1 = len(df_dados_1)

# Calcular o total de registros acumulados
total_registros_acumulado1 = total_registros1 + total_registros_1

porcentagem_taxas_acima_de_75 = (total_registros_acumulado1 / dias_uteis) * 100

total_registros2 = len(df_dados2)
total_registros_2 = len(df_dados_2)

total_registros_acumulado2 = total_registros2 + total_registros_2

porcentagem_taxas_acima_de_70 = (total_registros_acumulado2 / dias_uteis) * 100


# Para 6.5%
total_registros3 = len(df_dados3)
total_registros_3 = len(df_dados_3)
total_registros_acumulado3 = total_registros3 + total_registros_3
porcentagem_taxas_acima_de_65 = (total_registros_acumulado3 / dias_uteis) * 100


# Para 6.0%
total_registros4 = len(df_dados4)
total_registros_4 = len(df_dados_4)
total_registros_acumulado4 = total_registros4 + total_registros_4
porcentagem_taxas_acima_de_60 = (total_registros_acumulado4 / dias_uteis) * 100

# Para 5.5%
total_registros5 = len(df_dados5)
total_registros_5 = len(df_dados_5)
total_registros_acumulado5 = total_registros5 + total_registros_5
porcentagem_taxas_acima_de_55 = (total_registros_acumulado5 / dias_uteis) * 100

# Para 5.0%
total_registros6 = len(df_dados6)
total_registros_6 = len(df_dados_6)
total_registros_acumulado6 = total_registros6 + total_registros_6
porcentagem_taxas_acima_de_50 = (total_registros_acumulado6 / dias_uteis) * 100


# Para 4.5%
total_registros7 = len(df_dados7)
total_registros_7 = len(df_dados_7)
total_registros_acumulado7 = total_registros7 + total_registros_7
porcentagem_taxas_acima_de_45 = (total_registros_acumulado7 / dias_uteis) * 100


# Para 4.0%
total_registros8 = len(df_dados8)
total_registros_8 = len(df_dados_8)
total_registros_acumulado8 = total_registros8 + total_registros_8
porcentagem_taxas_acima_de_40 = (total_registros_acumulado8 / dias_uteis) * 100



# Definir os dados
porcentagens = [porcentagem_taxas_acima_de_75, porcentagem_taxas_acima_de_70, porcentagem_taxas_acima_de_65, porcentagem_taxas_acima_de_60, porcentagem_taxas_acima_de_55, porcentagem_taxas_acima_de_50, porcentagem_taxas_acima_de_45, porcentagem_taxas_acima_de_40]
labels = ['>= 7.5%', '>= 7%', '>= 6.5%', '>= 6%', '>= 5.5%', '>= 5%', '>= 4.5%', '>= 4%']

# Começar a fazer os gráficos de barra
plt.figure(figsize=(12, 8))
bars = plt.bar(labels, porcentagens, color='skyblue')

# Aqui coloca as informações no gra´fico
for bar, porcentagem in zip(bars, porcentagens):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, f'{porcentagem:.2f}%', ha='center', va='bottom')

# TÍTULO E ROTULOS
plt.title('Porcentagem de dias úteis com taxas de juros acima de determinado valor')
plt.xlabel('Taxa de Juros (%)')
plt.ylabel('Porcentagem de Dias Úteis')

plt.show()
