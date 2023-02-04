import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

host = os.environ.get('HOST')
user = os.environ.get('USERS')
password = os.environ.get('PASSWORD')
db = os.environ.get('DB')
conn = pymysql.Connect(host=host, user=user, password=password, db=db, port=3306, charset='utf8')
print("db 연결 완료")
cur = conn.cursor()

