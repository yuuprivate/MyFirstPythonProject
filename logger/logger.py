import os
from datetime import datetime, timedelta

logpath = r"D:\IPSP\ipsp_billing\backend_code\client\logger"

def get_week_start(date):
    return date - timedelta(days=date.weekday())

def log(text):
    now = datetime.now()
    week_start = get_week_start(now)
    week_end = week_start + timedelta(days=6)

    filename = f"log_since{week_start.strftime('%Y-%m-%d')}_until{week_end.strftime('%Y-%m-%d')}.txt"
    filepath = os.path.join(logpath,filename)

    os.makedirs(logpath, exist_ok=True)

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(text +'\n')