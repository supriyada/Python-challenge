#import OS module
import os
#import CSV module
import csv

"""
Dictionary to store the candidate name and their total votes received.
After creating dictionary, the values are used in calculating percentage of votes received and then find the winner!!!
"""
candidates_vote_dict = {}

total_votes = 0
winner = 0.00

#Path to the data source file
election_data_path=os.path.join("Resources","election_data.csv")

#Path to the data output file
output_path = os.path.join( "Analysis", "Results_from_Analysis.txt")

#Open the file `election_data.csv` as input_data
with open(election_data_path) as input_data:

    # CSV reader specifies delimiter and variable that holds contents
    csv_election_read = csv.reader(input_data, delimiter=',')

    # Stores the header row
    csv_election_header = next(csv_election_read)

    for election_row in csv_election_read:

        total_votes +=1

        #Creating candidate entries and accumulating vote count in the dictionary    
        if election_row[2] not in candidates_vote_dict:
            candidates_vote_dict.update({election_row[2]:1})
        else:
            previous_vote_count =  candidates_vote_dict.get(election_row[2])
            vote_count = int(previous_vote_count)+1
            candidates_vote_dict.update({election_row[2]:vote_count})

    # Open the output file in "write" mode.
    with open(output_path, 'w', newline='') as csv_poll_write:

        # Initialize csv.writer
        csvwriter = csv.writer(csv_poll_write)

        #Print the results to terminal and write it to a file
        csvwriter.writerow(['Election Results'])
        csvwriter.writerow(["*"*16])
        csvwriter.writerow(["Total Votes: "+str(total_votes)])
        csvwriter.writerow(["-"*30])
        print("-"*30)
        print(f'Election Results')
        print("*"*16 + '\n')
        print(f'Total Votes: {str(total_votes)}')
        print("-"*30)

        #Calculate the percentage of votes received and lookup for the winning candidate      
        for key,value in candidates_vote_dict.items():
            percent_calc = round((int(value)/total_votes)*100,2)
            print(f'{key} : {str(percent_calc)}% ({str(value)})')
            csvwriter.writerow([key + ":" + str(percent_calc) +  "% (" + str(value) + ")"])
            
            if percent_calc > winner:
                winner = percent_calc
                winning_candidate = key
        print("-"*30)
        print("The Winner is: " + winning_candidate.title())
        print("-"*30)
        csvwriter.writerow(["-"*30])
        csvwriter.writerow(["The Winner is: " + winning_candidate.title()])
        csvwriter.writerow(["-"*30]) 

