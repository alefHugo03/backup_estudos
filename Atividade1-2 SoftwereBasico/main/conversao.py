import json
import csv
import xml.etree.ElementTree as ET
import pandas as pd

def leitor_json():
    dados_json = []
    try:
        with open('Atividade1-2 SoftwereBasico\\data\\data.json', 'r', encoding='utf-8') as f_json:
            dados_json = json.load(f_json)
            return dados_json
    except FileNotFoundError:
        print("Arquivo data.json não encontrado.")
        return []

def leitor_csv():
    dados_csv = []
    try:
        with open('Atividade1-2 SoftwereBasico\\data\\data.txt', 'r', encoding='utf-8') as f_csv:
            reader = csv.DictReader(f_csv)
            for row in reader:
                dados_csv.append(row)
            return dados_csv
    except FileNotFoundError:
        print("Arquivo data.txt não encontrado.")
        return []

def leitor_xml():
    dados_xml = []
    try:
        tree = ET.parse('Atividade1-2 SoftwereBasico\data\data.xml')
        root = tree.getroot()
        for pessoa_element in root.findall('pessoa'):
            pessoa = {}
            for item in pessoa_element:
                pessoa[item.tag] = item.text
            dados_xml.append(pessoa)
        return dados_xml
    except FileNotFoundError:
        print("Arquivo data.xml não encontrado.")
        return []

def dados_saida():
    dados_unificados = leitor_json() + leitor_csv() + leitor_xml()
    df_unificado = pd.DataFrame(dados_unificados)
    print("\nDataFrame unificado do Pandas:")
    return df_unificado