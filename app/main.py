"""Главный скрипт тестового задания.
Настроено логирование основных событий и ошибок.
Выполняется чтение переменных окружения и основная логика.
"""
import os
import logging
import time
from datetime import datetime

from dotenv import load_dotenv
import requests
from telegram import Bot

from get_currency import usd_rate
from read_values import read_range
from db_functions import get_db_connection, update_db_table
from send_tg_message import send_notification


logging.basicConfig(
    level=logging.INFO,
    filename='main.log',
    filemode='a',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

load_dotenv('../infra/.env')
RETRY_TIME = int(os.getenv('RETRY_TIME'))
url_path = os.getenv('CBR_URL')
url_path_today = url_path + str(datetime.now().strftime("%d/%m/%Y"))
headers = os.getenv('HEADERS')
bot_token = os.getenv('BOT_TOKEN')
user_id = os.getenv('TELEGRAM_USER_ID')
bot_name = os.getenv('BOT_NAME')

def check_url():
    """Проверка ссылки сайта ЦБ на корректность."""
    try:
        requests.get(url_path_today, headers={'User-Agent': headers})
        return True
    except requests.exceptions.InvalidSchema:
        return False

def update_db():
    """Основная логика работы скрипта."""

    if not check_url():
        logging.critical(f'Ссылка на сайт ЦБ неверна - {url_path_today}.')
        return

    while True:
        try:
            currency = usd_rate(url_path_today, {'User-Agent': headers})
            logging.info(f'Прочитан курс доллара - {currency}.')

            values = read_range()
            logging.info('Считаны данные из гугл-таблицы.')

            conn = get_db_connection()
            logging.info('Выполнено подключение к базе данных.')

            overdue_orders = update_db_table(conn, values, currency)
            logging.info('Перезаписаны данные в базе данных.')

            if overdue_orders:
                send_notification(bot_token, user_id, overdue_orders, bot_name)
                logging.info(f'Отправлено сообщение юзеру - {user_id}.')
        
        except ValueError as error:
            logging.error(error)

        except Exception as error:
            bot = Bot(token=bot_token)
            bot.send_message(user_id, error)

            logging.error(error)

        finally:
            time.sleep(RETRY_TIME)


if __name__ == "__main__":
    update_db()
