# grafrico.py
# import conversao # Não é mais necessário aqui se o DataFrame for passado como argumento
import pandas as pd
import plotly.express as px
import io
from PIL import Image # Pillow já está sendo usado

# Modifique a assinatura da função para aceitar um DataFrame
def gerar_grafico_pessoas_por_estado(df_entrada):
    # dados_lista = conversao.dados_saida() # REMOVA ou comente esta linha
    # df = pd.DataFrame(dados_lista) # REMOVA ou comente esta linha
    df = df_entrada # Use o DataFrame fornecido como entrada

    if df.empty or 'estado' not in df.columns:
        print("DataFrame vazio ou sem coluna 'estado' para o gráfico.")
        # Retorna None ou uma imagem de erro placeholder, se preferir
        return None 
        
    contagem_por_estado = df['estado'].value_counts().reset_index()
    contagem_por_estado.columns = ['estado', 'quantidade']
    fig = px.bar(contagem_por_estado, x='estado', y='quantidade',
                title='Distribuição de Pessoas por Estado',
                labels={'estado': 'Estado', 'quantidade': 'Quantidade de Pessoas'})
    
    img_buf = io.BytesIO()
    try:
        fig.write_image(img_buf, format='png') # Requer Kaleido: pip install kaleido
        img_buf.seek(0)
        img = Image.open(img_buf)
        return img
    except Exception as e:
        print(f"Erro ao gerar imagem do gráfico (plotly.write_image): {e}")
        print("Certifique-se de que 'kaleido' está instalado: pip install kaleido")
        return None # Retorna None em caso de erro