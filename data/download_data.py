import gdown

# ID do arquivo do Google Drive (entre "/d/" e "/view")
file_id = "1ABcDxxxxxx7qU9P2Vbxxxxxx"
url = f"https://drive.google.com/uc?id={file_id}"

# Nome do arquivo de saída
output = "IMDB Dataset.csv"

# Baixa o arquivo
gdown.download(url, output, quiet=False)
