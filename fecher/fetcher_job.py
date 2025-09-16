from ..common.config import DB_CONFIG_Postgre, SELECT_QUERY
import psycopg2
from ..common.timestamp import print_timestamp

def job():
    print_timestamp("定期確認実行中")
    data = fetch_data()
    if data:
        print_timestamp(f"差異が{len(data)}日見つかりました")
        return data #差異データを返す
    else:
        print_timestamp("差異はありませんでした")
        return "None"
    
def fetch_data():
    try:
        with psycopg2.connect(**DB_CONFIG_Postgre) as conn:
            with conn.cursor() as cur:
                cur.execute(SELECT_QUERY)
                rows = cur.fetchall()
                return rows
    except Exception as e:
        print_timestamp(f"Error while fetching data: {e}")
        return []