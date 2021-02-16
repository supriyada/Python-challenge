#import OS module
import os
#import CSV module
import csv

#Path to the data source file
budget_data_path=os.path.join("Resources","budget_data.csv")

month_list = []
profit_loss_list = []
monthly_Change_total_list = [0]

budget = {}

total_month = 0
net_total = 0
monthly_diff = 0
monthly_Change_total = 0
monthly_Change_average = 0.00
greatest_profit = 0
greatest_loss = 0

#Open the file budget_data
with open(budget_data_path) as input_data:

    # CSV reader specifies delimiter and variable that holds contents
    csv_budget_read = csv.reader(input_data, delimiter=',')

    # Read the header row first
    csv_budget_header = next(csv_budget_read)
    print(f"CSV Header: {csv_budget_header}")

    x=1
    # Read each row of data after the header
    for budget_row in csv_budget_read:
        
        #Increment counter for each row read
        total_month += 1

        #Calculate the net total amount of "Profit/Losses" over the entire period
        net_total += int(budget_row[1]) 

        month_list.append(budget_row[0])
        profit_loss_list.append(budget_row[1])      


    for x in range(1,len(profit_loss_list)):
        monthly_diff= (int(profit_loss_list[x])) - (int(profit_loss_list[x-1]))
        monthly_Change_total_list.append(monthly_diff)
        monthly_Change_total = monthly_Change_total + monthly_diff
        if monthly_diff > greatest_profit:
            greatest_profit = monthly_diff
    
    budget = {"Month":month_list,"Profits/Losses":profit_loss_list,"Monthly_change":monthly_Change_total_list}
    for row in budget:
        if greatest_profit > int(row["Monthly_change"]):
            greatest_profit = int(row["Monthly_change"])
    print(greatest_profit)
                   
    monthly_Change_average = round(monthly_Change_total/(total_month-1),2)
     
    print(f'Financial Analysis')
    print(f'-'*30)
    print("Total Months: " + str(total_month))
    print("Total: $" +str(net_total))
    print("Average Change: $"+str(monthly_Change_average))
    #print(f'Greatest Increase in Profits: {profit_month} (${str(greatest_profit)})')
    #print(f'Greatest Decrease in Profits: {loss_month} (${str(greatest_loss)})')

output_path = os.path.join( "Analysis", "Results_from_Analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csv_budget_write:

    # Initialize csv.writer
    csvwriter = csv.writer(csv_budget_write)

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------'])
    csvwriter.writerow(["Total Months: " + str(total_month)])
    csvwriter.writerow(["Total: $" +str(net_total)])
    csvwriter.writerow(["Average Change: $"+str(monthly_Change_average)])
    #csvwriter.writerow(['Greatest Increase in Profits: ' + profit_month +' ($' + str(greatest_profit) + ')'])
    #csvwriter.writerow(['Greatest Decrease in Profits: ' + loss_month + ' ($' + str(greatest_loss) + ')'])
    
    
