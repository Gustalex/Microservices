# auth_service/Dockerfile

FROM python:3.13.1-slim

# Configuracoes

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Cria o diretorio para o sqlite3
RUN mkdir -p /app/data

# Dependencias

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copiar arquivos
COPY . .

# Runserver
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]