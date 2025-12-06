# DB接続情報
DB_CONFIG_MYSQL = {
    'host': '',
    'port': '',
    'dbname': '',
    'user': '',
    'password': '',
    'charset': ''
}
DB_CONFIG_Postgre = {
    'host': '',
    'port': '',
    'dbname': '',
    'user': '',
    'password': ''
}

# SELECT文
SELECT_QUERY = "SELECT day,date_id FROM table"

#UPDATE文
TARGETDATE_UPDATE = "UPDATE table SET {column_name} = (%s) where date_id = (%s)"

#プログラムを実行させる時刻
SCHEDULE_TIMES = ["06:00","18:00"]
