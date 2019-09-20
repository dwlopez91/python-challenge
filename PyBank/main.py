import os
import csv

#intialize variables
total_months = 0
total_revenue = 0

# Set path for file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Open the CSV
with open(csvpath, newline='') as csvfile:
    
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    row = next(csvreader)

    #set our ititial variables
    total_months = total_months + 1 
    total_revenue += int(row[1])
   
   
    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])



print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue}")

output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
