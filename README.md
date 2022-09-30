##  Проект "google_sheets_read"

### Описание проекта:

Скрипт выполняет следующие действия: 
- постоянное считывание данных из гугл-таблицы с помощью Google API;
- перезаписывание данных в базу данных;
- отправка сообщений через Telegram о заказах, дата доставки которых прошла;
- выполнено логирование основных событий - файл app/main.log.

### Технологии:

При реализации проекта были использованы следующие основные технологии, фреймворки и библиотеки:
- Python 3.10
- Google-API-Python-Client 2.63.0


### Как запустить проект:
Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone 'ссылка на репозиторий'
```

```
cd google_sheets_read
```

В папке infra cоздайте файл .env и заполните его следующими значениями:

```
CBR_URL=https://www.cbr.ru/scripts/XML_daily.asp?date_req=
spreadsheet_id=1GuhCZ86C8rDKig1A0zIS_qDP8BjnNYWfBwXMtyAjL8Q
CREDENTIALS_FILE =creds.json
RETRY_TIME=360 # время ожидания перед следующей проверкой
HEADERS=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
DATABASE_NAME=postgres
DB_USERNAME=postgres
DB_PASSWORD=postgres123
HOST=mypostgresdb # название сервиса (контейнера)
PORT=5432
BOT_TOKEN=5772558656:AAGuAK9YykrAkiT1Hi5bLJj5O6RVldAXOBg
TELEGRAM_USER_ID= #ваш user_id в Telegram (узнать у https://t.me/userinfobot)
BOT_NAME=@OverdueOrdersNotesBot
```

Перейдите в папку infra:

```
cd infra
```

Выполните сборку контейнеров с помощью команды:

```
sudo docker-compose up -d --build 
```

### Автор проекта:
- Зайцева Дарья
