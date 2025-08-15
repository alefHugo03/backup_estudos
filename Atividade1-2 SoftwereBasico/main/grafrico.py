import conversao
import pandas as pd
import plotly.express as px

dados_lista = conversao.dados_saida()

df = pd.DataFrame(dados_lista)

# Contar o número de pessoas por região
contagem_por_estado = df['estado'].value_counts().reset_index()
contagem_por_estado.columns = ['estado', 'quantidade']

# Criar o gráfico de barras com Plotly Express
fig = px.bar(contagem_por_estado, x='estado', y='quantidade',
             title='Distribuição de Pessoas por Região do Brasil',
             labels={'nome': 'idade', 'estado': 'salarios minimos'})

# Exibir o gráfico
fig.show()