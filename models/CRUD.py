# models/read.py

from googleapiclient.discovery import build
from google.oauth2 import service_account

SPREADSHEET_ID= "1pNgXiMG54vmF84jBBhtccclQGZwItYU2LeuP4oMNCWE"
RANGE_NAME_= "ExcelWorkPode!"
RANGE_NAME_MAIN= RANGE_NAME_+"A2:K"
RANGE_NAME_ROW=  RANGE_NAME_+"A:K"
MENU = "menuList"
RANGE_MENU = "!A2:B"
RANGE_MENUROW = "!A:B"


CREDS = None
try:
    CREDS = service_account.Credentials.from_service_account_file(
        './credentials.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    print(CREDS)
except Exception as ex:
  print('************************** Error **************************')
  print('Error', ex)

# Create and return the service object
service = build('sheets', 'v4', credentials=CREDS).spreadsheets()

def read_data():
      result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME_MAIN).execute()
      return result

def create_data(body):
      print('SPREADSHEET_ID : ',SPREADSHEET_ID)
      print("RANGE_NAME_ROW : ",RANGE_NAME_ROW)
      print('body : ',body)
      result = service.values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME_ROW,valueInputOption='RAW', body=body).execute()
      return result

def Menu_update_data(range_name,body):
      result = service.values().update(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME_+range_name,valueInputOption='RAW', body=body).execute()
      return result
    
def delete_data(range_name):
    result = service.values().clear(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME_+range_name).execute()
    return result

# Update Menu List

def Menu_read_data(i):
      result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=MENU+i+RANGE_MENU).execute()
      return result

def Menu_create_data(body,i):
      result = service.values().append(spreadsheetId=SPREADSHEET_ID, range=MENU+i+RANGE_MENUROW,valueInputOption='RAW', body=body).execute()
      return result

def Menu_update_data(i,range_name,body):
      result = service.values().update(spreadsheetId=SPREADSHEET_ID, range=MENU+i+'!'+range_name,valueInputOption='RAW', body=body).execute()
      return result
    
def Menu_delete_data(i,range_name):
    result = service.values().clear(spreadsheetId=SPREADSHEET_ID, range=MENU+i+'!'+range_name).execute()
    return result