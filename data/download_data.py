# Script para fazer o Download do dataset diretamento do Google Drive Público
import gdown
import os

# Cria a pasta data/raw se ela não existir
os.makedirs("data/raw", exist_ok=True)

# ID do arquivo do Google Drive
file_id = "1w4hMHY2zCsoYQjHE3DCnTmFYRWyBBxmf"
url = f"https://drive.google.com/uc?id={file_id}"

# Caminho de saída na pasta data/raw
output = "data/raw/IMDB_Dataset.csv"

# Faz o download
gdown.download(url, output, quiet=False)
print(f"Arquivo salvo em '{output}'")
