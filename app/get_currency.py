import requests
from bs4 import BeautifulSoup


def usd_rate(url: str, headers: dict) -> float:
    """Функция для считывания текущего курса доллара с сайта ЦБ."""

    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, features="xml")

    usd_node = soup.find("CharCode", string="USD")
    if usd_node is None:
        raise ValueError("Не найдена информация о долларе США")

    currency = usd_node.parent.find("Value").text
    if currency is None:
        raise ValueError("Не найден курс доллара США")

    return float(currency.replace(',', '.'))
