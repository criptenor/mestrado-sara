import pandas as pd
import json


# Função para carregar a planilha e converter em JSON
def excel_to_json(file_path):
    # Ler o arquivo Excel
    df = pd.read_excel(file_path)

    # Converter todas as linhas em uma lista de dicionários
    data = df.to_dict(orient='records')

    return data


# Caminhos para os arquivos Excel
file_path_2011_2015 = '/home/tom/Área de trabalho/sara/planilhas/HC LTS_2011-2015.xlsx'
file_path_2022_2024 = '/home/tom/Área de trabalho/sara/planilhas/HC LTS_2022-2024.xlsx'

# Processar cada arquivo e gerar JSON
data_2011_2015 = excel_to_json(file_path_2011_2015)
data_2022_2024 = excel_to_json(file_path_2022_2024)

# Combinar os dados das duas planilhas
combined_data = {
    '2011_2015': data_2011_2015,
    '2022_2024': data_2022_2024
}

# Caminho para salvar o JSON
json_file_path = '/web/grafico_mensal_dados.json'

# Salvar em um arquivo JSON
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(combined_data, json_file, ensure_ascii=False, indent=4)

print(f'Dados salvos em: {json_file_path}')
