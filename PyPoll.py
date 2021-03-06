import os
import csv

file_to_load = os.path.join('Resources', 'election_results.csv')

file_to_save = os.path.join('Resources', 'election_analysis.txt')

total_votes = 0

candidate_option = []

candidates_votes = {}

winning_count = 0
winning_candidate = ''
winning_percentage = 0

#Read the data from the csv file
with open(file_to_load, 'r') as election_data:

    file_reader = csv.reader(election_data)

    header = next(file_reader)

    for row in file_reader:
        total_votes += 1
        candidate = row[2]
        
        # store the candidate's name once for tracking
        if candidate not in candidate_option:
            candidate_option.append(candidate)
            
            # start tracking the candidate's vote count
            candidates_votes[candidate] = 0

        # increment the count for each voter
        candidates_votes[candidate] += 1

print(f"Total number of votes is {total_votes:,}\n")
#print(candidate_option)
#print(candidates_votes)

#Calculate the winning votes
for candidates_name in candidates_votes:

    votes = candidates_votes[candidates_name]
    percentage = (votes/total_votes) * 100
    print(f"{candidates_name}: {percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (percentage > winning_percentage):
        winning_count = votes
        winning_percentage = percentage
        winning_candidate = candidates_name

#Prepare and format the output data
line = "-----------------------------"

election_results = (
    f"\n{line}\n"
    f"Election Results\n"
    f"{line}\n"
    f"Total Votes: {total_votes:,}\n"
    f""
    )
print(election_results, end="")

winning_summary = (
    f"{line}\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"{line}\n"
    )

#Save output data to text file
with open(file_to_save, 'w') as txt_file:

    txt_file.write(election_results)
    txt_file.write(winning_summary)



#print(f"The winner of the election is {winning_candidate}")

#print(winning_summary)
    



