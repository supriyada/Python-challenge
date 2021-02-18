#import OS module
import os
#import CSV module
import csv

#Path to the data source file
budget_data_path=os.path.join("Resources","budget_data.csv")

total_month = 0
net_total = 0
monthly_diff = 0
monthly_Change_total = 0
monthly_Change_average = 0.00
greatest_profit = 0
greatest_loss = 0
profit_loss = 0

#Open the file budget_data
with open(budget_data_path) as input_data:

    # CSV reader specifies delimiter and variable that holds contents
    csv_budget_read = csv.reader(input_data, delimiter=',')

    # Stores the header row
    csv_budget_header = next(csv_budget_read)

    csv_budget_first_row = next(csv_budget_read)
    profit_loss = csv_budget_first_row[1]
    total_month += 1
    net_total += int(csv_budget_first_row[1]) 
    
    # Read each row of data after the header
    for budget_row in csv_budget_read:
        
        #Increment counter for each row read to calculate number of months
        total_month += 1

        #Calculate the net total amount of "Profit/Losses" over the entire period
        net_total += int(budget_row[1]) 

        #Calculate the monthly change and the its sum over the period
        monthly_diff = int(budget_row[1]) - int(profit_loss)
        profit_loss = int(budget_row[1])
        monthly_Change_total = monthly_Change_total + monthly_diff
                
        #Look up for greatest monthly increase in profits and its corresponding month
        if monthly_diff > greatest_profit:
            greatest_profit = monthly_diff
            greatest_profit_month = budget_row[0]
        
        #Look up for greatest monthly decrease in profits(that is the Loss) and its corresponding month
        if monthly_diff < greatest_loss:
            greatest_loss = monthly_diff
            greatest_loss_month = budget_row[0]
       
    #Average of changes in profit/losses
    monthly_Change_average = round(monthly_Change_total/(total_month-1),2)   
     
    #Print Finanacial Analysis summary output to the terminal
    print(f'Financial Analysis')
    print(f'-'*30)
    print("Total Months: " + str(total_month))
    print("Total: $" +str(net_total))
    print("Average Change: $"+str(monthly_Change_average))
    print(f'Greatest Increase in Profits: {greatest_profit_month} (${str(greatest_profit)})')
    print(f'Greatest Decrease in Profits: {greatest_loss_month} (${str(greatest_loss)})')
   
