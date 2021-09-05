# Election-Analysis
(Election analysis software written in Python)

## Project Analysis
A Colarado Elections Board employee was given a task to complete the audit of a recent election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candodate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular votes.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.5

## Summary

The analysis of the election show that:
- There were 369,711 votes cast in this election.
- The candidates were:

    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane 

- The counties where votes were cast:
    - Jefferson
    - Denver
    - Arapahoe

- The candidate results were:
    
    - Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
    - Diana DeGette received 73.8% of the votes and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.

- The total votes that were cast in each county:
    - Jefferson accounted for 10.5% of the votes and 38,855 number of votes.
    - Denver: accounted for 82.8% of the votes and 306,055 number of votes.
    - Arapahoe: accounted for 6.7% of the votes and 24,801 number of votes.

- The winner of the election was Diana DeGette who received 73.8% of the votes and 272,892 number of votes.

The script was written with flexibility in mind and it can be used for the election audit of any city as long as the csv file
is written in the same order.

The section of the code that saves the result of the analysis doesn't assume what the number of the counties or the candidates are,
that is information is found after the code iterates through each line in the data file provided.

```
1    # Save the final candidate vote count to the text file.
2    for candidate_name in candidate_votes:
3
4        # Retrieve vote count and percentage
5        votes = candidate_votes.get(candidate_name)
6        vote_percentage = float(votes) / float(total_votes) * 100
7        election_results = (
8            f"\n{candidate_name}: "
9            f"{vote_percentage:.1f}% "
10           f"({votes:,})\n"
11           )
```
Each candidate's name and votes are stored the candidate_vote **Dict**. 
The output variable *election_results* (Line 7) stores the output for each candidate found in the dictionary object.
