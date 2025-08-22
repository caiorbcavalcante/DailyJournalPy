from datetime import datetime

def checkDate(data_str, formato="%d/%m/%Y"):
    try:
        date = datetime.strptime(data_str, formato)
        return [date.year, date.month, date.day]  # Data válida
    except ValueError:
        return False  # Data inválida
    
date = checkDate("25/04/2006")

def getMonth(dateMonth):
    meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
             "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    if 1 <= dateMonth <= 12:
        return meses[dateMonth-1]
    return "Mês inválido"



