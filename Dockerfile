# Usando imagem oficial do Python
FROM python:3.9-slim

# Definindo variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho dentro do container
WORKDIR /app

# Instalando dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiando arquivos de dependências
COPY requirements.txt .

# Instalando dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiando o restante do projeto
COPY . .

# Expondo a porta para o Flask
EXPOSE 5000

# Comando para iniciar a API Flask
CMD ["python", "run.py"]
