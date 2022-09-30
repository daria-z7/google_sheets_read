from telegram import Bot, TelegramError


def send_notification(bot_token: str, user_id: int, order_list: list, bot_name: str):
    """Функция для отправки сообщения по заказам, дата доставки по которым прошла."""
    try:
        bot = Bot(token=bot_token)
    except Exception as error:
        raise ValueError(f'Переменная BOT_TOKEN с ошибкой - {error}')
    text = "Обратите внимание на список заказов, дата доставки по которым прошла: "
    orders = ", ".join(x for x in order_list)
    err_message = f' Возможно вам стоит инициировать работу с ботом - {bot_name}.'
    try:
        bot.send_message(user_id, text + orders)
    except TelegramError as error:
        raise TelegramError(f'Не удалось отправить сообщение - {error}.' + err_message)
