import gspread
from google.oauth2.service_account import Credentials
#Import here pprint but deleted before deployment

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('votingapp.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('voting_app')



def voter_choice():
    """
    This condition checks to see what the voter has chosen, either y,x,both or none.
    """
    print("Please use either '1' symbol for candidate A or '2' for candidate B")
    print("Do not use both '1,2' to vote as this will be invalid vote")
    print("You are only allowed to vote once...")
    choice = int(input("Please submit your vote here: "))
    if choice == 1:
        print(f"You voted for candidate A")
    else:
        print(f"You voted for candidate B ")

voter_choice()
