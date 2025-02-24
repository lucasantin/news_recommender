#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict, Counter
import glob
import pandas as pd
import sys
import json


def generate_topk(user_id=None, k=10):
    histories = defaultdict(Counter)

    # Ler arquivos de treino
    for fpath in glob.glob('./data/files/treino/*.csv'):
        df = pd.read_csv(fpath)
        for _, row in df.iterrows():
            user = row['userId']
            hist = row['history']
            hist = (hist.replace('\n', ' ')
                        .replace("'", ' ')
                        .replace("[", ' ')
                        .replace("]", ' ')
                        .strip().split())
            histories[user].update(hist)

    # Ler conjunto de validação
    df_test = pd.read_csv('./data/validacao.csv')

    recommendations = {}
    users_to_process = [user_id] if user_id else set(df_test['userId'])

    for user in users_to_process:
        topk = histories[user].most_common(k)
        # Corrigir vírgulas e espaços extras
        recommendations[user.strip()] = [item[0].strip().rstrip(',') for item in topk]

    # Garantir que apenas JSON puro seja impresso
    print(json.dumps(recommendations))


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        user_id = sys.argv[1]
        k = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        generate_topk(user_id, k)
    else:
        generate_topk()