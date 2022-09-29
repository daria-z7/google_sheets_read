from pprint import pprint
import os

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv('../infra/.env')


CREDENTIALS_FILE = os.getenv('CREDENTIALS_FILE')
spreadsheet_id = os.getenv('spreadsheet_id')

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


# Пример чтения файла
def read_range():
    column_s = "A"
    column_e = "D"
    startIndex = 1
    range = column_s + str(startIndex) + ":" + column_e
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range,
        majorDimension='ROWS',
    ).execute()
    # pprint(values)
    # for row in values['values']:
    #     print(row)
    return values['values']
