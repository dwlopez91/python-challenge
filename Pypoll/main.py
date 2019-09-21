import os
import csv

#intialize variables
total_votes = 0
candidate_list = []

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

print(total_votes)
