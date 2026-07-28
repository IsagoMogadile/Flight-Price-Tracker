from datetime import date, timedelta

def get_next_30_days():
    today = date.today()
    return [today + timedelta(days=i) for i in range(1, 31)]