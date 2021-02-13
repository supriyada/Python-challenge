#import OS module
import os
#import CSV module
import csv

#Path to the data source file
budget_data_path=os.path.join("Resources","budget_data.csv")

month_list=[]

#Open the file budget_data
with open(budget_data_path) as input_data:

    # CSV reader specifies delimiter and variable that holds contents
    csv_budget_read = csv.reader(input_data, delimiter=',')

    # Read the header row first
    csv_budget_header = next(csv_budget_read)
    #--print(f"CSV Header: {csv_budget_header}")

    # Read each row of data after the header
    for budget_row in csv_budget_read:
        #The first row is split with delimiter '-' and the value in first position is added to the list
        month=budget_row[0].split("-")
        month_list.append(month[0])

    print("The number of months is: " + str(len(month_list)))
    
