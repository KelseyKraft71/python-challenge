import os
import csv

#set path to budget file
budget_csv = os.path.join("Resources", "budget_data.csv")

#open path to budget_data csv file
with open(budget_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")

        #initialize variables
        total_months = 0
        net_total = 0
        months_list = []
        profit_loss_list = []
        monthly_changes = []
        months_list_updated = []
        max_increase_month = []
        max_decrease_month = []
        greatest_increase = 0
        greatest_decrease = 0
        monthly_changes_total = 0

        #skip the header of the csv file
        csv_header = next(csvfile)

        #loop through the rows of the sheet
        for row in csvreader:
                #count every row in the sheet and update the total_months variable
                total_months = total_months + 1
                #update the net_total by adding each row value to the net_total variable
                net_total = int(row[1]) + net_total
                #make a list for the profits/losses values (as integers) in each row 
                profit_loss_list.append(int(row[1]))
                #make a list for the months in each row
                months_list.append(row[0])

        #https://codefather.tech/blog/get-every-other-element-python-list/
        #loop through a range from 2 to the row number of the end of the profit_loss_list
        for x in range(1, len(profit_loss_list)):
                #calculate the difference between the index value of the current row minus
                #  the index value of the previous row. Assign the calculation to the variable change
                change = profit_loss_list[x] - profit_loss_list[x-1]
                #add the calculated change variable to the end of the monthly_changes list
                monthly_changes.append(change)

        #loop through the monthly_changes list
        for x in monthly_changes:
                #update the monthly_changes_total variable to current row value plus 
                # the current monthly_changes_total
                monthly_changes_total = x + monthly_changes_total
        
        #calculate the average of the monthly_changes_total variable, rounding to 2 
        #  decimal places. Assign the calculation to a variable average_change
        average_change = round((monthly_changes_total)/(len(monthly_changes)), 2)

        #loop through a range from 2 to the row number of the end of the profit loss list
        for x in range(1, len(months_list)):
                #get the index value of the current row from the months_list list
                new_months = months_list[x]
                #add the new_months variable to the end of the months_list_updated list
                months_list_updated.append(new_months)

        #create a variable called keys and assign it the months_list_updated list
        keys = months_list_updated
        #create a variable called values and assign it the monthly_changes list
        values = monthly_changes
        #make a dictionary called combined_months_profits by zipping the keys and values variables
        #  This will give a dictionary with the profit/loss changes for every month and its corresponding month name
        combined_months_profits = dict(zip(keys, values))

        #had some help from ChatGPT here
        #loop through the keys and values of the combined_months_profits dictionary
        for key, value in combined_months_profits.items():
                #check if the profit change is greater than the greatest_increase variable:
                if value > greatest_increase:
                        #make the current value the new greatest_increase variable
                        greatest_increase = value
                        #add the profit change and its corresponding month to the max_increase_month dictionary
                        max_increase_month = {key: value}
                #otherwise, check if the profit change is less than the greatest_decrease variable:
                elif value < greatest_decrease:
                        #make the current value the new greatest_decrease variable
                        greatest_decrease = value
                        #add the profit change and its corresponding month to the ma_decrease_month dictionary
                        max_decrease_month = {key: value}

#specify output path for the new text file
output_path = os.path.join("output", "results.txt")

#https://www.pythontutorial.net/python-basics/python-write-text-file/
#open output path in write mode
with open(output_path, "w") as f:

        #https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
        #write lines to text file with line breaks for formatting
        f.write("Financial Analysis\n")
        f.write("-----------------------\n")
        f.write(f"Total Months: {total_months}\n")
        f.write(f"Net Total: ${net_total}\n")
        f.write(f"Average Change: ${average_change}\n")
        f.write(f"Greatest Increase in Profits: {max_increase_month}\n")
        f.write(f"Greatest Decrease in Profits: {max_decrease_month}")
    
#print results to console
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_increase_month}")
print(f"Greatest Decrease in Profits: {max_decrease_month}")