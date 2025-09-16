import psycopg2
from ..common.config import DB_CONFIG_Postgre,TARGETDATE_UPDATE
from ..common.column_control import ColumnSelector
from .cdr_repair import cdr_repair
from .sonus_repair import sonus_repair
from ..checker.check import check_data
from ..common.timestamp import print_timestamp
import datetime

column_key: str
    
def repair_data(data):
    date = []
    try:
        column = ColumnSelector.get_column(column_key)
        query = TARGETDATE_UPDATE.format(column_name=column)


        with psycopg2.connect(**DB_CONFIG_Postgre) as conn:
            with conn.cursor() as cur:
                for i in data.length():
                    date.append(data[i][0])
                    cur.execute(query,(data[i][0],data[i][1]))
                    print_timestamp(f"date_id:{data[i][1]}が{data[i][0]}に更新されました")
                    if data[i][0] == 3 or data[i][0] == 4:
                        repair = cdr_repair(data)
                        if "失敗" in repair:
                            print("CDR修復に失敗しました")
                            return []
                    elif data[i][0] == 2:
                        sonus_repair(data)
                        repair = sonus_repair(data)
                        if "失敗" in repair:
                            print_timestamp("Sonus修復に失敗しました")
                            return []
                    else:
                        print("不正な日付データが含まれています")
                now = datetime.date.today()
                today = now.strftime("%Y-%m-%d 00:00:00")
                cur.execute(query,(2,today))
                cur.execute(query,(3,today))
                cur.execute(query,(4,today))
            check_data(date) # 修復後のデータ確認
        conn.comimit()
    except Exception as e:
        print_timestamp(f"バッチ実行中にエラー発生:{e}")
        return []