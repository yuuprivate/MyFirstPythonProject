import subprocess
from ..common.timestamp import print_timestamp

def sonus_repair():
    script_path = r'D:\Project\Project_files\backend_code\data_archive\controllers\cron\sonus_outbund_cron.js'
    try:
        result = subprocess.run(['node', script_path], capture_output=True, text=True, check=True)
        print_timestamp(result.stdout)
    except subprocess.CalledProcessError as e:
        print_timestamp(f"SONUS修復スクリプト実行エラー:{e.stderr}")
