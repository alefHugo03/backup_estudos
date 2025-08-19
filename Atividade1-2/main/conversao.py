import json
import csv
import xml.etree.ElementTree as ET
import pandas as pd
import os
# Certifique-se de que geopandas está instalado para lidar com GeoDataFrames
# pip install geopandas pyarrow # pyarrow é para o formato parquet

# Obtém o diretório do arquivo atual (conversao.py, que está dentro de 'main/')
CURRENT_DIR = os.path.dirname(__file__)

# Define o caminho para a pasta 'data' (sobe um nível e entra em 'data')
DATA_FOLDER = os.path.join(CURRENT_DIR, '..', 'data')

# Define o caminho para a pasta 'pre_renderizacao' (dentro de 'main/')
# Certifique-se de que esta pasta existe ou será criada.
PRE_RENDER_FOLDER = os.path.join(CURRENT_DIR, 'pre_renderizacao')

# --- O restante do seu código de leitor_json, leitor_csv, leitor_xml e dados_saida permanece o mesmo ---

def leitor_json():
    dados_json_python = []
    file_path = os.path.join(DATA_FOLDER, 'data.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f_json:
            dados_json = json.load(f_json)
            for item in dados_json:
                pessoa = {
                    'nome': item.get('nome'),
                    'idade': item.get('idade'),
                    'estado': item.get('estado'),
                    'cep': item.get('cep'),
                    'salarios_minimos': item.get('salarios_minimos')
                }
                dados_json_python.append(pessoa)
            return dados_json_python
    except FileNotFoundError:
        print(f"Arquivo JSON não encontrado: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON em {file_path}: {e}")
        return []

def leitor_csv():
    dados_csv_python = []
    file_path = os.path.join(DATA_FOLDER, 'data.csv')
    try:
        with open(file_path, 'r', encoding='utf-8') as f_csv:
            reader = csv.DictReader(f_csv)
            for row in reader:
                pessoa = {
                    'nome': row.get('nome'),
                    'idade': row.get('idade'),
                    'estado': row.get('estado'),
                    'cep': row.get('cep'),
                    'salarios_minimos': row.get('salarios_minimos')
                }
                dados_csv_python.append(pessoa)
            return dados_csv_python
    except FileNotFoundError:
        print(f"Arquivo CSV não encontrado: {file_path}")
        return []
    except Exception as e:
        print(f"Erro inesperado ao ler CSV em {file_path}: {e}")
        return []

def leitor_xml():
    dados_xml_python = []
    file_path = os.path.join(DATA_FOLDER, 'data.xml')
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for pessoa_element in root.findall('pessoa'):
            pessoa = {
                'nome': pessoa_element.findtext('nome'),
                'idade': pessoa_element.findtext('idade'),
                'estado': pessoa_element.findtext('estado'),
                'cep': pessoa_element.findtext('cep'),
                'salarios_minimos': pessoa_element.findtext('salarios_minimos')
            }
            dados_xml_python.append(pessoa)
        return dados_xml_python
    except FileNotFoundError:
        print(f"Arquivo XML não encontrado: {file_path}")
        return []
    except ET.ParseError as e:
        print(f"Erro ao analisar XML em {file_path}: {e}")
        return []
    except Exception as e:
        print(f"Erro inesperado ao ler XML em {file_path}: {e}")
        return []

def dados_saida():
    dados_json = leitor_json()
    dados_csv = leitor_csv()
    dados_xml = leitor_xml()
    dados_unificados = dados_json + dados_csv + dados_xml
    df_unificado = pd.DataFrame(dados_unificados)
    return df_unificado