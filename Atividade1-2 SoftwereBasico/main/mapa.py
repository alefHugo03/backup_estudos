import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim
from shapely.geometry import Point
import folium
import conversao
import webbrowser
import time

# Sua lista de dados (substitua com seus dados reais)
dados = conversao.dados_saida()
# Converter a lista de dicionários para um DataFrame do Pandas
df = pd.DataFrame(dados)

# Inicializar o geocodificador
geolocator = Nominatim(user_agent="seu_aplicativo") # Substitua "seu_aplicativo" por um nome descritivo

# Função para geocodificar um CEP
def geocode_cep(cep):
    try:
        location = geolocator.geocode(f"{cep}, Brasil", exactly_one=True, timeout=10)
        if location:
            return Point(location.longitude, location.latitude)
        else:
            return None
    except Exception as e:
        print(f"Erro ao geocodificar o CEP '{cep}': {e}")
        return None
# Aplicar a geocodificação à coluna de CEP e criar uma coluna de geometria
df['geometry'] = df['cep'].apply(geocode_cep)
# Remover as linhas onde a geocodificação falhou
df_geo = df.dropna(subset=['geometry']).copy()
# Converter o DataFrame para um GeoDataFrame

gdf = gpd.GeoDataFrame(df_geo, geometry='geometry', crs="EPSG:4326") # WGS 84
# Coordenadas do centro do Brasil para centralizar o mapa inicialmente

brasil_centro = [-15.7801, -47.9292]
# Criar o mapa Folium

mapa_brasil = folium.Map(location=brasil_centro, zoom_start=4)
# Adicionar marcadores para cada ponto no GeoDataFrame

for index, row in gdf.iterrows():
    nome = row['nome']
    salario = row['salarios_minimos']
    cep = row['cep']
    longitude, latitude = row['geometry'].xy
    folium.Marker(
        [latitude[0], longitude[0]],
        popup=f"<b>{nome}</b><br>Salários Mínimos: {salario}<br>CEP: {cep}",
        tooltip=nome
    ).add_to(mapa_brasil)

# Salvar o mapa como um arquivo HTML
nome_arquivo_mapa = "mapa_brasil.html"
mapa_brasil.save(nome_arquivo_mapa)

print(f"Mapa do Brasil gerado com sucesso (usando GeoPandas e CEPs) em {nome_arquivo_mapa}")

# Abrir o arquivo HTML no navegador padrão
webbrowser.open(nome_arquivo_mapa)
time.sleep(1)  # Espera 5 segundos antes de fechar o navegador