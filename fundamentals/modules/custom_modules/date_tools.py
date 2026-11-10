# Module date_tools.py functions

from datetime import datetime

def calculate_age(y, m, d):
    birth = datetime(y, m, d)
    now = datetime.now()

    age = now.year - birth.year

    if (now.month, now.day) < (birth.month, birth.day):
        age -= 1

    return age

def days_left(y, m, d):
    date = datetime(y, m, d)
    now = datetime.now()
    today = datetime(now.year, now.month, now.day)
    
    total_days = (date - today).days

    if total_days < 0:
        return 0
    return total_days

def get_weekday(y, m, d):
    target_date = datetime(y, m, d)
    return target_date.strftime("%A")