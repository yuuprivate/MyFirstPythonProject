import schedule
import time
from .fetcher_job import job
from ..common.config import SCHEDULE_TIMES
from ..repairer.repair import repair_data
from ..common.timestamp import print_timestamp

def job_and_repair():
    data = job()
    if data and data != "None":
        repair_data(data)

def main():
    for time_str in SCHEDULE_TIMES:
        schedule.every().day.at(time_str).do(job_and_repair)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    print_timestamp("スケジュール開始")
    job_and_repair()
    main()
