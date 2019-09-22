import os
import csv

#intialize variables
total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

# Set path for file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Open the CSV
with open(csvpath, newline='') as csvfile:
    
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    row = next(csvreader)

    total_votes = total_votes + 1

    #iterate
    for row in csvreader:
        total_votes += 1
        if(row[2] == "Khan"):
            khan += 1
        elif(row[2] == "Correy"):
            correy += 1
        elif(row[2] == "Li"):
            li += 1
        elif(row[2] == "O'Tooley"):
            otooley += 1    
    #divide the votes per candidate by total votes to find percentage
    khan_percent = round(khan/total_votes * 100)
    correy_percent = round(correy/total_votes * 100)
    li_percent = round(li/total_votes * 100)
    otooley_percent = round(otooley/total_votes * 100)

    
    
   
    
    


print("Election Results")
print(f"Total Votes: {total_votes}")
print("--------")
print(f"Khan: {khan_percent}% ({khan})")
print(f"Correy: {correy_percent}% ({correy})")
print(f"Li: {li_percent}% ({li})")
print(f"O'Tooley: {otooley_percent}% ({otooley})")
print("--------")


# Specify the file to write to
output_path = os.path.join("..", "output", "new_poll.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
