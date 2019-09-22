import os
import csv

#intialize variables
total_votes = 0
khan = 0
# correy = candidate_list.count("Correy")
# li = candidate_list.count("Li")
# otooley = candidate_list.count("O'Tooley")

# Set path for file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Open the CSV
with open(csvpath, newline='') as csvfile:
    
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    row = next(csvreader)

    total_votes = total_votes + 1


    for row in csvreader:
        total_votes += 1
        if(row[2] == "Khan"):
            khan += 1
khan_percent = round(khan/total_votes * 100)

print(total_votes)
print(khan)
print(khan_percent)
