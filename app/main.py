from pprint import pprint

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1GuhCZ86C8rDKig1A0zIS_qDP8BjnNYWfBwXMtyAjL8Q'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


# Пример чтения файла
column_s = "A"
column_e = "D"
startIndex = 1
range = column_s + str(startIndex) + ":" + column_e
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range=range,
    majorDimension='ROWS',
).execute()
pprint(values)
for row in values['values']:
    print(row)

