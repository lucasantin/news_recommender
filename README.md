# 📚 Sistema de Recomendação de Notícias

Este projeto tem como objetivo desenvolver um sistema de recomendação de notícias personalizado para o portal notícias. Ele utiliza técnicas de **Filtragem Colaborativa** com o algoritmo **SVD** (Singular Value Decomposition) para prever quais notícias um usuário provavelmente leria em sua próxima sessão.

---

## 🚀 Tecnologias Utilizadas

- **Python**
- **Flask** — API para servir as recomendações
- **scikit-surprise** — Implementação do algoritmo SVD
- **Pandas & NumPy** — Manipulação e análise de dados
- **Docker & Docker Compose** — Empacotamento e deploy
- **pytest** — Testes unitários e de integração

---

## 📂 Estrutura do Projeto

news-recommender/ │ ├── app/ │ ├── init.py │ ├── api.py │ ├── recommender.py │ ├── utils.py │ ├── models/ │ │ └── svd_model.pkl │ ├── data_processing.py │ └── data/ │ ├── files/ │ │ ├── treino/ │ │ └── itens/ │ ├── validacao.csv │ └── popular_items.json │ ├── scripts/ │ ├── train_svd.py │ ├── generate_popular.py │ └── etl_pipeline.py │ ├── notebooks/ │ └── eda.ipynb │ ├── tests/ │ ├── test_api.py │ └── test_recommender.py │ ├── Dockerfile ├── docker-compose.yml ├── requirements.txt ├── README.md └── run.py

---

## ⚙️ Configuração do Ambiente

### 1️⃣ **Clone o Repositório**
```bash
git clone https://github.com/lucasantin/news_recommender
cd news-recommender

2️⃣ Crie um Ambiente Virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows

3️⃣ Instale as Dependências

pip install -r requirements.txt
🏗️ Executando o Projeto
💻 1. Rodar a API Localmente

python run.py
A API Flask estará disponível em:
http://localhost:5000

📡 Endpoints da API
🔹 /recommend — Recomendação Personalizada
Método: POST
Descrição: Retorna uma lista de notícias recomendadas para um usuário específico.
Exemplo de Request:
curl -X POST http://localhost:5000/recommend \\
-H "Content-Type: application/json" \\
-d '{"user_id": "12345"}'

Exemplo de Resposta:
json
Copiar
Editar
{
  "user_id": "12345",
  "recommendations": [
    "noticia_1",
    "noticia_2",
    "noticia_3"
  ]
}
🔹 /popular — Notícias Mais Populares
Método: GET
Descrição: Retorna as notícias mais populares no geral (sem personalização).
Exemplo de Request:
curl http://localhost:5000/popular
Exemplo de Resposta:
json

{
  "popular_recommendations": [
    "noticia_10",
    "noticia_5",
    "noticia_3"
  ]
}
📊 Treinando o Modelo SVD
1. Executar o Script de Treinamento

python scripts/train_svd.py
📈 Gerando Notícias Populares
1. Executar o Script generate_popular.py


python scripts/generate_popular.py
🧪 Executando os Testes
1. Rodar Testes Unitários e de Integração

pytest tests/
🐳 Docker
1. Construir a Imagem Docker
docker build -t news-recommender .

2. Rodar o Container
docker run -p 5000:5000 news-recommender


📋 Conclusão
Este projeto apresenta um sistema de recomendação funcional, capaz de sugerir notícias personalizadas aos usuários com base em seu histórico de leitura.

💻 Desenvolvido por: Lucas Vicentini Santin
📅 Data: [02/2025]
🚀 Desafio: Sistema de Recomendação de Notícias """