# scripts/train_svd.py
import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pickle
import os

def train_svd_model(data_path='./app/data/files/treino/', model_output='./app/models/svd_model.pkl'):
    # Ler os arquivos de treino
    files = os.listdir(data_path)
    dfs = []
    for file in files:
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join(data_path, file))
            dfs.append(df)

    # Combinar todos os DataFrames em um único DataFrame
    full_df = pd.concat(dfs, ignore_index=True)

    # Preparar dados: userId, itemId (history) e rating (implícito como 1)
    data = []
    for _, row in full_df.iterrows():
        user = row['userId']
        history = row['history']
        if pd.notna(history):
            items = history.replace('\n', ' ').replace("'", '').replace("[", '').replace("]", '').strip().split()
            for item in items:
                data.append([user, item, 1])  # Rating implícito como 1

    # Converter para DataFrame
    rating_df = pd.DataFrame(data, columns=['user', 'item', 'rating'])

    # Usar Surprise para treinar o modelo
    reader = Reader(rating_scale=(0, 1))
    dataset = Dataset.load_from_df(rating_df[['user', 'item', 'rating']], reader)

    trainset, _ = train_test_split(dataset, test_size=0.2, random_state=42)

    # Treinar o modelo SVD
    svd = SVD()
    svd.fit(trainset)

    # Salvar o modelo treinado
    os.makedirs(os.path.dirname(model_output), exist_ok=True)
    with open(model_output, 'wb') as f:
        pickle.dump(svd, f)

    print(f"Modelo SVD treinado e salvo em {model_output}")

if __name__ == "__main__":
    train_svd_model()
