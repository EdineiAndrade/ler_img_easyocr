# Usa uma imagem oficial do Python
FROM python:3.12

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8080 (ou outra que você usar)
EXPOSE 8080

# Comando para rodar o app
CMD ["python", "api/app.py"]
