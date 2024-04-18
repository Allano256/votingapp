import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# 1.Get sales from the user
#CSV COMMA SEPARATED VALUES
#ASK USER TO SEND IN DATA

def get_sales_data():
    """ 
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n") #Add the backslash and "n" to have space between the sections

    data_str = input("Enter your data here.") #Create input area for data entry
    print(f"The data provide is {data_str}") #Printout the data in terminal

get_sales_data()
