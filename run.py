import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
# 2.Validate the data provided
#CSV COMMA SEPARATED VALUES
#ASK USER TO SEND IN DATA

def get_sales_data():
    """ 
    Get sales figures input from the user
    """
    while True:
        print("Please enter sales data from the last market.")
        print("data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n") #Add the backslash and "n" to have space between the sections

        data_str = input("Enter your data here.")
      #Create input area for data entry
      #Printout the data in terminal
      #The data provided always comes in string format hence the variable "data_str" used

      #Validate the data provided

        sales_data = data_str.split(",")
    
     # Use the split method to break it up at the commas,this will remove the commas from the string.
     #values is the sales data list in the parameter.

        if validate_data(sales_data):
            print("Data is valid")
            break   #This validation part checks if the data enetered is true,and return True if it is and the while loop will end at the break key work,but if the wrong values are entered,the while loop will keep goin and ask for new data.
    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises valueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    print(values)
    try:
        [int(value) for value in values] #our try statement converts values to integers
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False #If there is an error in the data,so an error will be printed an the user asked to enter new data.
    
    return True #If no error is found when entering data,so this will also be the condition to end our while loop.

def update_sales_worksheet(data):
    """
    Update  sales worksheet, add new row with the list data provided
    """ 
    print("Updating sales worksheet...\n")  
    sales_worksheet = SHEET.worksheet('sales') 
    sales_worksheet.append_row(data) #append_row adds a new row at the end of the sheet.
    print("Sales worksheet updated successfully.\n ")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracte from the stock:
     -positive surplus inicates waste
     -Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet('stock').get_all_values() #This gets the last data of the stock sheet at tyhe bottom
    pprint(stock) #Makes data easier to read wen printed to terminal,this is used instead of "print" but needs to be also imported at the top.
    stock_row = stock[-1] #Accessing the last row of the spreadsheet
    print(f"stock row: {stock_row}")
    print(f"sales row: {sales_row}")
    
    surplus_data = [] #This is where we shall push the results from our calculation using the append method
    for stock, sales in zip(stock_row, sales_row): #The zip method allows us to unpack the data.
        surplus = int(stock) - sales #You have the int on the stock values to convert it to integers
        surplus_data.append(surplus)

    return surplus_data

def update_surplus_worksheet(data):
    """
    Update  surplus worksheet, add new row with the list data provided
    """ 
    print("Updating surplus worksheet...\n")  
    surplus_worksheet = SHEET.worksheet('surplus') 
    surplus_worksheet.append_row(data) #append_row adds a new row at the end of the sheet.
    print("Surplus worksheet updated successfully.\n ")




def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data] #We assign the result from the list comprehension to a new variable named sales_data
    update_sales_worksheet(sales_data)# we call the function n pass the sales_data _list
    new_surplus_data = calculate_surplus_data(sales_data)
    print(new_surplus_data)
    update_surplus_worksheet(new_surplus_data) #This will update the surplus worksheet

print("Welcome to Love Sanwiches Data Automation") # So wehn you run the system,this message will be printed first before the others
main()



# ['12','3','12','10','12','13']