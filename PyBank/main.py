import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

#open path to budget_data csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    total_months = 0
    net_total = 0
    changes_list = []
    months_list = []

    csv_header = next(csvfile)

    #loop through the rows of the sheet
    for row in csvreader:
            total_months = total_months + 1
            net_total = int(row[1]) + net_total
            changes_list.append(int(row[1]))
            months_list.append(str(row[0]))

    profit_loss_changes = 0

    for num in changes_list:
          
    
          


 
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print("Total Months: " + str(total_months))
    print("Total: $" + str(net_total))
    #print(str(changes))