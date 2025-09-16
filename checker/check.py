import subprocess
from ..common.timestamp import print_timestamp

def check_data():
    script_path = r'D:\IPSP\ipsp_billing\backend_code\data_archive\controllers\cron\check_cron.js'
    try:
        result = subprocess.run(['node', script_path ], capture_output=True, text=True, check=True)
        print_timestamp("チェック完了" + result.stdout)
    except subprocess.CalledProcessError as e:
        print_timestamp(f"データチェックスクリプト実行エラー:{e.stderr}")
