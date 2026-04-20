# Usa uma imagem oficial do Python, versão leve (slim)
FROM python:3.10-slim

# Define qual será a pasta de trabalho lá dentro do container
WORKDIR /app

# Copia o arquivo de dependências para dentro da imagem
COPY requirements.txt .

# Atualiza o Linux interno e instala o Tkinter e o "monitor virtual" (Xvfb)
RUN apt-get update && apt-get install -y python3-tk xvfb

# Instala o CustomTkinter, PyInstaller, etc.
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do seu computador para dentro do container
COPY . .

# Comando mágico: Roda o Python dentro do monitor virtual (-a acha uma tela livre automaticamente)
CMD ["xvfb-run", "-a", "python", "calculadora.py"]