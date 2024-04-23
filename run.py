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
    This condition checks to see what the voter has chosen, either 1,2. Also ensure that the voter does not reload the page everytime they enter a wrong character but instead loads automatically using the while loop created.
    """
   
    print("Please use either '1' symbol for candidate A or '2' for candidate B")
    print("Do not use both '1,2' to vote as this will be invalid vote")
    print("You are only allowed to vote once...\n")
    
    choice_user = str(input("Please submit your vote here: "))
    global voter_choice
    voter_choice = choice_user
       
    if voter_choice == "1" :
        print(f"You voted for candidate A")
    elif voter_choice == "2" :
        print(f"You voted for candidate B")
    else:
        print(f"{voter_choice} chosen is not a valid character")
        return voter_choice

      
        
    
def update_candidate_A_votes(voter_choice):
    """
    This will update the votes for candidate A.
    """
   
    print("updating candidate A tally...\n")
    candidate_worksheet = SHEET.worksheet('candidate')
    candidate_worksheet.append_row(voter_choice)
    print("Candidate A worksheet updated successfully \n")

    candidate_data = candidate_worksheet.get_all_records()
    print(candidate_data)
    print('The voter choice is', voter_choice)
    candidate_worksheet.append_row(voter_choice)


data = voter_choice()
update_candidate_A_votes(data)


   


    




    

