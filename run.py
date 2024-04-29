import os
import time
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
SHEET = GSPREAD_CLIENT.open('voting_app')

def clear():
    """
    This clears the print messsages when the program starts running.
    """
    os.system("cls")

def voter_choice(candidate_data):
    """
    This condition checks to see what the voter has chosen, either A or B.
    This prints the total number of expected voters
    """
   
    print("Please use either A symbol for candidate A or B for candidate B")
    print("Do not use both 'A and B' to vote as this will be invalid vote")
    print("You are only allowed to vote once...\n")
   
    if len(candidate_data) == 12:
        print("Voting is now closed...")
        votes_cast()
        return 
  

    choice_user = input("Please submit your vote here: ").upper()
    clear()

    global voter_choice 
    voter_choice = choice_user
    time.sleep(1)
    
    if voter_choice == 'A' :
        print(f"You voted for candidate A")
        input("press enter to continue")
        clear()
        update_candidate_votes([1,0],candidate_data)
     
    elif voter_choice == 'B' :
        print(f"You voted for candidate B")
        input("press enter to continue")
        clear()
        update_candidate_votes([0,1],candidate_data)
       
    else:
        print(f"{voter_choice} chosen is not a valid character, use A OR B")
        
        return voter_choice

        
def update_candidate_votes(voter_choice, candidate_data):
    """
    This will update the votes for candidate A and B in the spreadsheet and also retrieve the values from the spreadsheet
    """
  
    print("updating candidate A tally...\n")
    time.sleep(2)
    candidate_worksheet = SHEET.worksheet('candidate')
    candidate_worksheet.append_row(voter_choice)
    clear()
    print("Candidate A worksheet updated successfully \n")
   
    time.sleep(2)
    clear()  
    print(candidate_data)
    time.sleep(1)
    print('The voter choice is', voter_choice)

def votes_cast():
    """
    This function adds up the values from each candidate and gives a total, the candidate with the most votes being the winner.
    """
    # Get the worksheet
    worksheet = SHEET.worksheet('candidate')

    #Get the data from the worksheet
    candidate_worksheet = SHEET.worksheet('candidate')
    candidate_data = candidate_worksheet.get_all_records()
    print(len(candidate_data))

    #variables for each candidate
    total_votes_A = 0
    total_votes_B = 0

    i = 2
    while i < len(candidate_data):
          
          # Get the value of cell at row 2, column 1
          cell1_value = worksheet.cell(i,1).value 
          total_votes_A += int(cell1_value)

          # Get the value of cell at row 2, column 2
          cell2_value = worksheet.cell(i,2).value 
          total_votes_B += int(cell2_value)
          i += 1
          

    print(f"Candidate A has {total_votes_A} votes and Candidate B has {total_votes_B} votes")

    if total_votes_A > total_votes_B:
        print("Candidate A won the election")
    elif total_votes_B > total_votes_A:
        print("Candidate B won the election")
    else: 
        print("Its a tie!")
  
clear()


def main():
    """
    This function gets called called when the application starts running.
    """
    candidate_worksheet = SHEET.worksheet('candidate')
    candidate_data = candidate_worksheet.get_all_records()
    voter_choice(candidate_data)
     
print("Welcome to the Uganja voting app")
main()







    




    

