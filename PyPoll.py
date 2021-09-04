import os
import csv

file_to_load = os.path.join('Resources', 'election_results.csv')

file_to_save = os.path.join('Resources', 'election_analysis.txt')

total_votes = 0

with open(file_to_load, 'r') as election_data:

    file_reader = csv.reader(election_data)

    header = next(file_reader)

    for row in file_reader:
        total_votes += 1

print(f"Total number of votes is {total_votes}")

# 1. The data we need to retrieve
# 2. A complete list candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.



