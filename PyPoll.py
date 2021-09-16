# Data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load= os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. initialize a total vote counter.
total_votes = 0

# Candidate options and votes.
candidate_options = []
candidate_votes = {}


# open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header now.
    headers = next(file_reader)

    # print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

    # print the candidate name from each row
    candidate_name = row[2]

    # if the candidate does not match any existing candidate..
    if candidate_name not in candidate_options:

        # Add it to the list of candidates
        candidate_options.append(candidate_name)

        # Track candidates voter count.
        candidate_votes[candidate_name] = 0

    # Add a vote to the candidates count
    candidate_votes[candidate_name] += 1

print(candidate_votes)