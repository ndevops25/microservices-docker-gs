# Dockerfile para o Microserviço de Produtos
FROM python:3.10-slim

# Define o diretório de trabalho na imagem
WORKDIR /app

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py

# Instala as dependências
RUN pip install --no-cache-dir flask gunicorn

# Copia o código fonte para o diretório de trabalho
COPY app.py .

# Informa em qual porta o container estará escutando
<<<<<<< HEAD
EXPOSE 9001

# Comando para iniciar o aplicativo quando o container for executado
CMD ["gunicorn", "--bind", "0.0.0.0:9001", "app:app"]
=======
<<<<<<<< HEAD:microservices/fornecedores-service/Dockerfile
EXPOSE 8001

# Comando para iniciar o aplicativo quando o container for executado
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "app:app"]
========
EXPOSE 6002

# Comando para iniciar o aplicativo quando o container for executado
CMD ["gunicorn", "--bind", "0.0.0.0:6004", "app:app"]
>>>>>>>> 8d3659a8010fbd7e2bb99ec8c2dcd1fc76e8cc46:microservices/produtos-service/Dockerfile
>>>>>>> 8d3659a8010fbd7e2bb99ec8c2dcd1fc76e8cc46
