import subprocess
from ..common.timestamp import print_timestamp

def cdr_repair():
    script_path = r'D:\Project\Project_files\backend_code\data_archive\controllers\cron\kickback_cron.js'
    try:
        result = subprocess.run(['node', script_path], capture_output=True, text=True, check=True)
        print_timestamp(result.stdout)
        return "成功"
    except subprocess.CalledProcessError as e:
        print_timestamp(f"CDR修復スクリプト実行エラー:{e.stderr}")
        return "失敗"
