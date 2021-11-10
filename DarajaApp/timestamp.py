from datetime import datetime

def format_time():
    unformated_datetime=datetime.now()
    formated_datetime = unformated_datetime.strftime("%Y%m%d%H%M%S") #Formats the datetime i a format the safaricom expects
    return formated_datetime
