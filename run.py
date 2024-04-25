import gspread
from google.oauth2.service_account import Credentials


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
    This condition checks to see what the voter has chosen, either A or B.
    """
   
    print("Please use either A symbol for candidate A or B for candidate B")
    print("Do not use both 'A and B' to vote as this will be invalid vote")
    print("You are only allowed to vote once...\n")
    
    choice_user = (input("Please submit your vote here: "))

    global voter_choice 
    voter_choice = choice_user
    
    if voter_choice == 'A' :
        print(f"You voted for candidate A")
        update_candidate_A_votes([1,0])
     
    elif voter_choice == 'B' :
        print(f"You voted for candidate B")
        update_candidate_A_votes([0,1])
       
    else:
        print(f"{voter_choice} chosen is not a valid character")
        
        return voter_choice

      
        
    
def update_candidate_A_votes(voter_choice):
    """
    This will update the votes for candidate A and B in the spreadsheet and also retrieve the values from the spreadsheet
            """

    print("updating candidate A tally...\n")
    candidate_worksheet = SHEET.worksheet('candidate')
    candidate_worksheet.append_row(voter_choice)
    print("Candidate A worksheet updated successfully \n")
    candidate_worksheet = SHEET.worksheet('candidate')
    candidate_data = candidate_worksheet.get_all_records()
        
    print(candidate_data)
    print('The voter choice is', voter_choice)
   


data = voter_choice()



   


    




    

