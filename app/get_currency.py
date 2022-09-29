import requests
from bs4 import BeautifulSoup


def usd_rate(url: str, headers: dict) -> float:
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, features="xml")
    usd_node = soup.find("CharCode", string="USD")
    currency = usd_node.parent.find("Value").text
    return float(currency.replace(',', '.'))
