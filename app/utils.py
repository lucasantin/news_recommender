import pandas as pd

def preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df