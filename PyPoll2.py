import csv
import os
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_results.csv")

total_votes = 0

candidate_options = {}
candidate_votes = {}

with open(file_to_load) as election_date:
    file_reader = csv.reader(election_data)
    

    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

print(candidate_votes)

