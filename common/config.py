# DB接続情報
DB_CONFIG_MYSQL = {
    'host': 'localhost',
    'port': '3306',
    'dbname': 'automation',
    'user': 'root',
    'password': 'ZAQ!2wsx',
    'charset': 'utf8mb4'
}
DB_CONFIG_Postgre = {
    'host': '10.168.11.41',
    'port': '5432',
    'dbname': 'sonus_db',
    'user': 'postgres',
    'password': ''
}

# SELECT文
SELECT_QUERY = "SELECT day,date_id FROM automation"

#UPDATE文
TARGETDATE_UPDATE = "UPDATE public.batch_date_control SET {column_name} = (%s) where date_id = (%s)"

#プログラムを実行させる時刻
SCHEDULE_TIMES = ["06:00","18:00"]