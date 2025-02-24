from flask import Blueprint, request, jsonify
from app.recommender import NewsRecommender
import subprocess
import os
import json
import pandas as pd

app = Blueprint('api', __name__)

# Inicializar o recomendador
recommender = NewsRecommender()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'API is running'})

@app.route('/recommend', methods=['POST'])
def recommend():
    import pickle
    import pandas as pd

    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'error': 'user_id é obrigatório'}), 400

    try:
        # Carregar o modelo treinado
        model_path = './app/models/svd_model.pkl'
        with open(model_path, 'rb') as f:
            svd_model = pickle.load(f)

        # Carregar o arquivo validacao.csv para obter todos os itens
        validacao_path = './app/data/validacao.csv'
        validacao_df = pd.read_csv(validacao_path)

        # Extrair todos os itens únicos da coluna 'history' em validacao.csv
        all_items = set()
        for history in validacao_df['history']:
            if pd.notna(history):
                items = history.replace('\n', ' ').replace("'", '').replace("[", '').replace("]", '').strip().split()
                all_items.update(items)

        # Verificar se temos itens disponíveis
        if not all_items:
            return jsonify({'message': 'Nenhum item disponível em validacao.csv'}), 404

        # Gerar recomendações usando o modelo SVD
        recommendations = []
        for item in all_items:
            pred = svd_model.predict(user_id, item)
            recommendations.append({'item_id': item, 'estimated_rating': pred.est})

        # Ordenar por maior rating
        recommendations = sorted(recommendations, key=lambda x: x['estimated_rating'], reverse=True)[:10]

        return jsonify({'user_id': user_id, 'recommendations': recommendations}), 200

    except FileNotFoundError:
        return jsonify({'message': 'Modelo SVD ou validacao.csv não encontrado.'}), 404
    except Exception as e:
        return jsonify({'message': f'Erro ao gerar recomendações: {e}'}), 500

    
@app.route('/popular', methods=['GET'])
def popular():
    try:
        # Definir caminho absoluto para generate_popular.py
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts/generate_popular.py'))
        
        # Executar o script generate_popular.py
        result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True)
        
        # Carregar o arquivo JSON gerado
        popular_items_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../app/data/popular_items.json'))
        with open(popular_items_path, 'r', encoding='utf-8') as f:
            popular_items = json.load(f)
        
        # Retornar a lista de itens populares
        return jsonify({'popular_recommendations': popular_items}), 200

    except subprocess.CalledProcessError as e:
        return jsonify({'message': f'Erro ao executar generate_popular.py: {e.stderr}'}), 500
    except FileNotFoundError:
        return jsonify({'message': 'Arquivo popular_items.json não encontrado após execução do script.'}), 404
    except json.JSONDecodeError as e:
        return jsonify({'message': f'Erro ao ler o JSON de itens populares: {e}'}), 500
