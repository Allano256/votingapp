import time
import subprocess
import platform
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
TS = 60*2 + time.time() 

def clear():

    """
    This clears the the screen for both windows and OS users.
    """
    if platform.system() =="Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True)
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else:
        print("\033c", end="")

def get_voter_choice(candidate_data):
    """
    This condition checks to see what the voter has chosen, either A or B.
    This prints the total number of expected voters
    """  
    if time.time() >= TS:
      
        print("Voting is now closed...")
        votes_cast()
        return 
    
    print("Please use either A symbol for candidate A or B for candidate B")
    print("Do not use both 'A and B' to vote as this will be invalid vote")
    print("You are only allowed to vote once...\n")
   
    choice_user = input("Please submit your vote here: ").upper()
    clear()

    global voter_choice 
    voter_choice = choice_user
    time.sleep(1)
    
    if voter_choice == 'A' :
        print(f"You voted for candidate A")
        input("press enter to continue")
        clear()
        comfirm_selection([1,0],candidate_data)
           
    elif voter_choice == 'B':
        print(f"You voted for candidate B")
        input("press enter to continue")
        clear()
        comfirm_selection([0,1],candidate_data)
             
    else:
        print(f"{voter_choice} chosen is not a valid character, use A OR B")
        get_voter_choice(candidate_data)
        
        return voter_choice
    
def comfirm_selection(choice,candidate_data):
    """
    This will request the user to comfirm their choice or make changes.
    """
    print("Would you like to comfirm?")
    comfirmation = input()

    if comfirmation == "yes":
        update_candidate_votes(choice, candidate_data)

    else:
            
        get_voter_choice(candidate_data)
              
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
    get_voter_choice(candidate_data) 
    time.sleep(2)
    clear()   
    time.sleep(1)
   
def votes_cast():
    """
    This function adds up the values from each candidate and gives a total, the candidate with the most votes being the winner.
    """
    # Get the worksheet
    worksheet = SHEET.worksheet('candidate')

    #Get the data from the worksheet
    candidate_worksheet = SHEET.worksheet('candidate')
    candidate_data = candidate_worksheet.get_all_records()
  
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
    get_voter_choice(candidate_data)
     
print("Welcome to the  voting app")
main()







    




    

