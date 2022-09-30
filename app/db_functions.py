import os
from datetime import datetime

import psycopg2
from dotenv import load_dotenv


load_dotenv('../infra/.env')
host=os.getenv('HOST')
database=os.getenv('DATABASE_NAME')
user=os.getenv('DB_USERNAME')
password=os.getenv('DB_PASSWORD')

def update_db_table(conn: str, values: list, currency: float) -> list:
    """Функция для перезаписи данных в таблице."""
    overdue_orders = []
    cur = conn.cursor()
    cur.execute('DELETE FROM orders')
    for row in values:
        order_date = datetime.strptime(row[3].replace('.', '/'), '%d/%m/%Y')
        if order_date < datetime.now():
            overdue_orders.append(row[1])
        cur.execute('INSERT INTO orders (order_id, order_number, amount_usd, delivery_date, amount_rub)'
                    'VALUES (%s, %s, %s, %s, %s)',
                    (
                        int(row[0]),
                        int(row[1]),
                        int(row[2]),
                        order_date,
                        round(int(row[2])/currency, 4)
                    ))
    conn.commit()
    cur.close()
    conn.close()
    return overdue_orders

def get_db_connection() -> str:
    """Функция для создания подключения к бд."""
    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=password)
    return conn
