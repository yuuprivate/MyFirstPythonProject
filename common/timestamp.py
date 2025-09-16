import datetime
from ..logger.logger import log

def print_timestamp(text):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    printtext = now + " " + text
    print(printtext)
    log(printtext)