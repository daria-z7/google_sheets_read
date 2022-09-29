import os
import time
from datetime import datetime

from dotenv import load_dotenv

from get_currency import usd_rate
from read_values import read_range


load_dotenv('../infra/.env')



RETRY_TIME = int(os.getenv('RETRY_TIME'))
url_path = os.getenv('URL')
url_path_today = url_path + str(datetime.now().strftime("%d/%m/%Y"))
headers = os.getenv('HEADERS')

def update_db():
    """Прочитать новые файлы к обработке."""
    while True:
        currency = usd_rate(url_path_today, {'User-Agent':headers})
        print(currency)
        print(read_range())

        time.sleep(RETRY_TIME)


if __name__ == "__main__":
    update_db()
