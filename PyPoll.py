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

    # Read the header row.
    headers = next(file_reader)

    # print each row in the CSV file
    for row in file_reader:
        # add total vote count
        total_votes += 1

        # print candidate name for each row
        candidate_name = row[2]

        # if candidate does not match any existing ..
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # 2. Begin tracking candidate vote count.
            candidate_votes[candidate_name] = 0
        # add a vote to the candidates count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through counts
# 1. Iterate through the candidate list
for candidate_name in candidate_votes:
     # 2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # 3. calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

# Print candidate name and percent.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")