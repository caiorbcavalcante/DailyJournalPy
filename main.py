from storage.file_manager import createDir, saveNote
from utils.date_utils import checkDate, getMonth
from datetime import datetime

print("A data deve ser inserida no padrão 'DD/MM/AAAA'")
inputDate = input("Digite a data da anotação: ")

try:
    date = checkDate(inputDate.strip())
    if not date:
        raise ValueError("Data inválida")
    caminho = createDir(date)
except ValueError as e:
    print(e)

messageInput = input(f"Digite o texto para o caminho({caminho})") + "\n"
print("Perfeito! anotação feita!")
titleInput = input("Digite o título para o texto: ")

saveNote(caminho, messageInput, titleInput.strip())

