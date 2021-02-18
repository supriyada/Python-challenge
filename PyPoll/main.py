#import OS module
import os
#import CSV module
import csv

candidates_list = []
vote_count = []
vote_percent = []
total_votes = 0
percent_calc = 0.00


def create_candidate_list(election_row):
    if election_row[2] not in candidates_list:
            candidates_list.append(election_row[2])
            vote_count.append('1')
        
    else:
            position = candidates_list.index(election_row[2])
            vote_count[position] = int(vote_count[position]) + 1
    return

def calc_percent_vote_winner(vote_count):
    winner = 0
    for vote in range(len(vote_count)):
        percent_calc = round((int(vote_count[vote])/total_votes)*100,2)
        vote_percent.append(percent_calc)
        if vote_count[vote] > winner:
            winner = vote_count[vote]
            winning_candidate = candidates_list[vote]
    return winning_candidate

#Path to the data source file
election_data_path=os.path.join("Resources","election_data.csv")

#Open the file election_data
with open(election_data_path) as input_data:

    # CSV reader specifies delimiter and variable that holds contents
    csv_election_read = csv.reader(input_data, delimiter=',')

    # Read the header row first
    csv_election_header = next(csv_election_read)

    # Read each row of data after the header
    for election_row in csv_election_read:

        total_votes +=1
        
        #Calling function to create 2 lists: candidate list and their corresponding voting count
        create_candidate_list(election_row)

    #Calling function to calculate %of vote received by each candidate and to lookup for winning candidate       
    winning_candidate =  calc_percent_vote_winner(vote_count)  
   
    #Print the results to the terminal
    print("-"*30)
    print(f'Election Results')
    print("*"*16 + '\n')
    print(f'Total Votes: {str(total_votes)}')
    print("-"*30)
    for vote in range(len(vote_count)):
        print(candidates_list[vote] + ": " + str(vote_percent[vote]) + "%  (" +str(vote_count[vote]) + ")")
    print("-"*30)
    print("The Winner is: " + winning_candidate.title())
    print("-"*30)

