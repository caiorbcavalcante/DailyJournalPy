from datetime import datetime

def checkDate(data_str, formato="%d/%m/%Y"):
    try:
        date = datetime.strptime(data_str, formato)
        return [date.year, date.month, date.day]  # Data válida
    except ValueError:
        return False  # Data inválida
    
dateArray = checkDate("25/04/2006")



