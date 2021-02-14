#import OS module
import os
#import CSV module
import csv

#Path to the data source file
budget_data_path=os.path.join("Resources","budget_data.csv")

month_list = []
profit_loss_list = []

budget = {}

#Open the file budget_data
with open(budget_data_path) as input_data:

    # CSV reader specifies delimiter and variable that holds contents
    csv_budget_read = csv.reader(input_data, delimiter=',')

    # Read the header row first
    csv_budget_header = next(csv_budget_read)
    print(f"CSV Header: {csv_budget_header}")

    total_month = 0
    net_total = 0
    greatest_profit = 0
    greatest_loss = 0
    # Read each row of data after the header
    for budget_row in csv_budget_read:
        
        #Increment counter for each row read
        total_month += 1

        month_list.append(budget_row[0])
        profit_loss_list.append(budget_row[1])

        #Calculate the net total amount of "Profit/Losses" over the entire period
        net_total += int(budget_row[1])

        if int(budget_row[1]) > greatest_profit:
            greatest_profit = int(budget_row[1])
            profit_month = budget_row[0]

        if int(budget_row[1]) < greatest_loss:
            greatest_loss = int(budget_row[1])
            loss_month = budget_row[0]
        
    budget = {"Month": month_list,"Amount": profit_loss_list}
    initial_amount = int(budget["Amount"][0])
    final_amount = int(budget["Amount"][total_month-1])
    Change_profit_loss = round(((final_amount - initial_amount)/total_month),3)

    print(f'Financial Analysis')
    print(f'-'*30)
    print("Total Months: " + str(total_month))
    print("Total: " +str(net_total))
    print("Average Change: "+str(Change_profit_loss))
    print(f'Greatest Increase in Profits: {profit_month} (${str(greatest_profit)})')
    print(f'Greatest Decrease in Profits: {loss_month} (${str(greatest_loss)})')
    
