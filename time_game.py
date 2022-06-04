from datetime import date
from datetime import datetime

def day_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today_is = date.today()
    current_day = today_is.strftime("%b-%d-%Y")
    print(f'Tuday is {current_day}  {current_time}\n')

