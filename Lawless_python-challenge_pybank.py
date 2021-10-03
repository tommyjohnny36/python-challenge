#  Your task is to create a Python script that analyzes the records to calculate each of the following:    
 
#  The total number of months included in the dataset    
 
#  The net total amount of "Profit/Losses" over the entire period    
 
#  Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes    
 
#  The greatest increase in profits (date and amount) over the entire period    
 
#  The greatest decrease in profits (date and amount) over the entire period 

import csv

# Define file path for program to go get data
csvpath = r"E:\Georgia Tech\02-Homework\03-Python\python-challenge\Instructions\PyBank\Resources\budget_data.csv"

total_months = []
total_profit = []
monthly_change = []


with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
   
    # Iterate through the rows in csv file
    for row in csvreader:

    # Telling the file where to look for the values in table 
    # The total number of months included in the dataset
    # The total profit and calculations will be pulled from this variable
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Storing the current total profit in the variable i
    # then adding current total to the next month's value (i+1)
    for i in range(len(total_profit)-1):

        # Append the monthly change variable with the total profit calculation    
        monthly_change.append(total_profit[i+1]-total_profit[i])

# Get the max and min value for profit
max_profit_value = max(monthly_change)
min_profit_value = min(monthly_change)

# Get the months associated with the max and min value for profit
max_profit_month = monthly_change.index(max(monthly_change)) + 1
min_profit_month = monthly_change.index(min(monthly_change)) + 1


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_profit_month]} (${(str(max_profit_value))})")
print(f"Greatest Decrease in Profits: {total_months[min_profit_month]} (${(str(min_profit_value))})")
    
