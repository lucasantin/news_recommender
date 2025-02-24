import pandas as pd
from collections import Counter
import glob
import json


def generate_popular(top_n=10, output_path='./app/data/popular_items.json'):
    histories = Counter()

    # Listar arquivos encontrados
    arquivos = glob.glob('./app/data/files/treino/*.csv')
    #print(f"Arquivos encontrados: {arquivos}")

    if not arquivos:
        #print("Nenhum arquivo de treino encontrado.")
        return

    # Ler arquivos de treino
    for fpath in arquivos:
        #print(f"\nProcessando arquivo: {fpath}")
        try:
            df = pd.read_csv(fpath, sep=None, engine='python', encoding='utf-8')
        except Exception as e:
            #print(f"Erro ao ler o arquivo {fpath}: {e}")
            continue

        if 'history' not in df.columns:
            #print(f"Aviso: O arquivo {fpath} não contém a coluna 'history'.")
            continue

        valid_rows = 0
        for idx, history in enumerate(df['history']):
            if pd.notna(history):
                valid_rows += 1
                hist_list = (history.replace('\n', ' ')
                                    .replace("'", '')
                                    .replace("[", '')
                                    .replace("]", '')
                                    .strip()
                                    .split())
                histories.update(hist_list)

        #print(f"Linhas válidas processadas em {fpath}: {valid_rows}")

    if not histories:
        #print("\nAviso: Nenhum dado de histórico encontrado para gerar popularidade.")
        return

    # Obter os top_n mais populares
    most_common = histories.most_common(top_n)
    popular_items = [{"item_id": item, "views": count} for item, count in most_common]

    # Salvar os resultados em um arquivo JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(popular_items, f, ensure_ascii=False, indent=4)

    ##print(f"\nItens mais populares salvos em: {output_path}")
    #for item in popular_items:
        ##print(f"{item['item_id']}: {item['views']} visualizações")


if __name__ == "__main__":
    generate_popular(10)    