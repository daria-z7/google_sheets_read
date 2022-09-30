# Инициация подключения к бд и создания таблицы с необходимыми полями
import os

import psycopg2
from dotenv import load_dotenv


load_dotenv('../infra/.env')
host=os.getenv('HOST')
database=os.getenv('DATABASE_NAME')
user=os.getenv('DB_USERNAME')
password=os.getenv('DB_PASSWORD')

conn = psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS orders;')
cur.execute('CREATE TABLE orders (id serial PRIMARY KEY,'
                                 'order_id integer NOT NULL,'
                                 'order_number integer NOT NULL,'
                                 'amount_usd integer NOT NULL,'
                                 'delivery_date date NOT NULL,'
                                 'amount_rub decimal NOT NULL);'
                                 )

conn.commit()
cur.close()
conn.close()
