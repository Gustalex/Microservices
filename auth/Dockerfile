# auth_service/Dockerfile

FROM python:3.13.1-slim

# Configuracoes

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Dependencias

COPY requirements.txt .
RUN pip install __nocache-dir -r requirements.txt

# copiar arquivos
COPY . .

# Runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]