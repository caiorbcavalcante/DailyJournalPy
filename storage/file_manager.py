import os
from utils.date_utils import getMonth

root_directory = "DailyJournalPy"

os.makedirs(root_directory, exist_ok=True)

def createDir(data, root_directory="DailyJournalPy"):
    year = data.year
    month = data.month
    day = data.day

    month_name = getMonth(month)
    # Monta o caminho completo
    caminho = os.path.join(root_directory, str(year), month_name, f"{day:02}")
    os.makedirs(caminho, exist_ok=True)

    return caminho

def saveNote(path, message, filename="nota.md"):
    """
    Cria um arquivo .md dentro do caminho especificado e escreve a mensagem.
    
    path: caminho da pasta onde o arquivo será salvo
    message: texto da anotação
    filename: nome do arquivo (padrão 'nota.md')
    """
    # Monta o caminho completo do arquivo
    file_path = os.path.join(path, filename)
    
    # Cria/escreve o arquivo
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(message)
    
    print(f"Anotação salva em: {file_path}")


