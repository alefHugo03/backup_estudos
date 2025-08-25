# mapa.py
import folium
import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim
from shapely.geometry import Point

def converter_para_geodataframe(df):
    """
    Converte um DataFrame de pessoas com CEPs para um GeoDataFrame
    adicionando a coluna 'geometry' com as coordenadas (latitude, longitude).
    """
    # Aumentando o timeout para 30 segundos para dar mais tempo ao serviço Nominatim
    geolocator = Nominatim(user_agent="aplicacao_software_basico", timeout=30)

    def geocode_cep(cep):
        """Função interna para geocodificar um único CEP."""
        if not cep or pd.isna(cep): # Adicionado para tratar CEPs vazios/NaN mais cedo
            # print(f"CEP vazio ou inválido para geocodificação: '{cep}'")
            return None
        try:
            # Tenta encontrar a localização do CEP no Brasil
            location = geolocator.geocode(f"{cep}, Brasil", exactly_one=True)
            if location:
                print(f"CEP '{cep}' geocodificado com sucesso: Lat={location.latitude}, Lon={location.longitude}")
                return Point(location.longitude, location.latitude)
            else:
                print(f"CEP não encontrado ou inválido: '{cep}'")
                return None
        except Exception as e:
            print(f"Erro ao geocodificar o CEP '{cep}': {e}")
            return None

    # Garante que a coluna 'cep' é string e preenche valores nulos para evitar erros
    df['cep'] = df['cep'].astype(str).fillna('')
    # Aplica a geocodificação para cada CEP, criando a coluna 'geometry'
    df['geometry'] = df['cep'].apply(geocode_cep)
    
    # Remove linhas onde a geocodificação falhou (geometry é None)
    conversao_geo = df.dropna(subset=['geometry']).copy()

    if conversao_geo.empty:
        print("Nenhum CEP pôde ser geocodificado. GeoDataFrame resultante está vazio.")
        # Retorna um GeoDataFrame vazio com as colunas corretas se não houver dados geocodificados
        return gpd.GeoDataFrame([], columns=df.columns.tolist(), crs="EPSG:4326")

    # Cria o GeoDataFrame a partir do DataFrame com a coluna 'geometry'
    gdf = gpd.GeoDataFrame(conversao_geo, geometry='geometry', crs="EPSG:4326")
    return gdf

# A função gerar_mapa não é mais usada diretamente para exibição no seu app Tkinter,
# mas mantemos ela aqui caso você queira usar o objeto folium.Map para outras finalidades no futuro
# (por exemplo, salvar um mapa HTML independente).
def gerar_mapa(gdf):
    """
    Gera um mapa Folium com marcadores para cada ponto no GeoDataFrame.
    Esta função gera um objeto de mapa Folium, não um widget Tkinter.
    """
    brasil_centro = [-15.7801, -47.9292] # Coordenadas aproximadas do centro do Brasil
    mapa_brasil = folium.Map(location=brasil_centro, zoom_start=4) # Inicializa o mapa

    if not gdf.empty and 'geometry' in gdf.columns:
        for index, row in gdf.iterrows():
            nome = row.get('nome', 'N/A')
            salario = row.get('salarios_minimos', 'N/A')
            cep = row.get('cep', 'N/A')

            # Verifica se a geometria é válida e não está vazia antes de adicionar o marcador
            if row['geometry'] is not None and not row['geometry'].is_empty:
                latitude = row['geometry'].y
                longitude = row['geometry'].x
                
                # Adiciona um marcador Folium com popup e tooltip
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"<b>{nome}</b><br>Salários Mínimos: {salario}<br>CEP: {cep}",
                    tooltip=nome
                ).add_to(mapa_brasil)
    return mapa_brasil