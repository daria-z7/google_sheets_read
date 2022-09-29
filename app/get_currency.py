from datetime import datetime
import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv('../infra/.env')

url_path = os.getenv('URL')
print(url_path)
url_path_today = url_path + str(datetime.now().strftime("%d/%m/%Y"))
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def usd_rate(url: str, headers: dict) -> float:
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, features="xml")
    usd_node = soup.find("CharCode", string="USD")
    currency = usd_node.parent.find("Value").text
    return float(currency.replace(',', '.'))

print(usd_rate(url_path_today, headers))