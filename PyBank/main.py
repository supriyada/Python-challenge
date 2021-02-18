#import OS module
import os
#import CSV module
import csv

#Path to the data source file
budget_data_path=os.path.join("Resources","budget_data.csv")

month_list = []
profit_loss_list = []
monthly_Change_total_list = [0]

budget_zip =()

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
    
    # Read each row of data after the header
    for budget_row in csv_budget_read:
        
        #Increment counter for each row read to calculate number of months
        total_month += 1

        #Calculate the net total amount of "Profit/Losses" over the entire period
        net_total += int(budget_row[1]) 

        #Two list created with each column from dataset
        month_list.append(budget_row[0])
        profit_loss_list.append(budget_row[1])      

    #Calculate the changes in "Profit/Losses" over the entire period
    i=1
    for i in range(1,len(profit_loss_list)):
        monthly_diff= (int(profit_loss_list[i])) - (int(profit_loss_list[i-1]))
        monthly_Change_total = monthly_Change_total + monthly_diff

        #Third list with difference between months is created
        monthly_Change_total_list.append(monthly_diff)
    
    #Average of changes in profit/losses
    monthly_Change_average = round(monthly_Change_total/(total_month-1),2)   

    #zipped the lists[month_list],[profit_loss_list],[monthly_change_total_list]  
    budget_zip = zip(month_list,profit_loss_list,monthly_Change_total_list)
    for row in budget_zip:
        value = row[2]

        #Look up for greatest monthly increase in profits and its corresponding month
        if value > greatest_profit:
            greatest_profit = value
            greatest_profit_month = row[0]
        
        #Look up for greatest monthly decrease in profits(that is the Loss) and its corresponding month
        if value < greatest_loss:
            greatest_loss = value
            greatest_loss_month = row[0]
                      
    
    #Print Finanacial Analysis summary output to the terminal
    print(f'Financial Analysis')
    print(f'-'*30)
    print("Total Months: " + str(total_month))
    print("Total: $" +str(net_total))
    print("Average Change: $"+str(monthly_Change_average))
    print(f'Greatest Increase in Profits: {greatest_profit_month} (${str(greatest_profit)})')
    print(f'Greatest Decrease in Profits: {greatest_loss_month} (${str(greatest_loss)})')


#Path to the data output file
output_path = os.path.join( "Analysis", "Results_from_Analysis.txt")

# Open the file using "write" mode.
with open(output_path, 'w', newline='') as csv_budget_write:

    # Initialize csv.writer
    csvwriter = csv.writer(csv_budget_write)

    #Print Finanacial Analysis summary output to the File    
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------'])
    csvwriter.writerow(["Total Months: " + str(total_month)])
    csvwriter.writerow(["Total: $" +str(net_total)])
    csvwriter.writerow(["Average Change: $"+str(monthly_Change_average)])
    csvwriter.writerow(['Greatest Increase in Profits: ' + greatest_profit_month +' ($' + str(greatest_profit) + ')'])
    csvwriter.writerow(['Greatest Decrease in Profits: ' + greatest_loss_month + ' ($' + str(greatest_loss) + ')'])
    
    
