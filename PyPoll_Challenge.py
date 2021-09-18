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

#  Initialize a total vote counter.
total_votes = 0

# Candidate options and votes.
candidate_options = []
candidate_votes = {}

# County list and county votes dictionary
county_options = []
county_votes = {}

# Determine "winner" county based on vote turnout
winning_county = ""
county_winning_votes = 0
county_winning_percentage = 0

# Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
        # print county name from each row
        county_name = row [1]

        # if candidate does not match any existing ..
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # 2. Begin tracking candidate vote count.
            candidate_votes[candidate_name] = 0
        # add a vote to the candidates count
        candidate_votes[candidate_name] += 1

        # If county does not match and existing..
        if county_name not in county_options:
            # Add it to the list of counties
            county_options.append(county_name)
            # begin tracking county vote count.
            county_votes[county_name] = 0
        # Add a vote to that county's count
        county_votes[county_name] += 1

# print & save the results to our text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"--------------------\n"
        f"Total Votes: 369,711\n"
        f"--------------------\n"
        f"County votes\n"
        f"--------------------\n")

    print(election_results, end="")
        # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine percentage of votes by looping through county vote counts
    for county_name in county_votes:
        # Retrieve county vote count
        county_votes_total = county_votes[county_name]
        # Determine the percentage of votes per county
        county_vote_percentage = float(county_votes_total) / float(total_votes) * 100
        # Print county results to the terminal.
        county_results = (f"{county_name}: {county_vote_percentage:1f}% ({county_votes_total})\n")
        print(county_results)
        # Save county votes to text file
        txt_file.write(county_results)

        # Create if statement to retrieve winning county and vote count
        if (county_votes_total > county_winning_votes) and (county_vote_percentage > county_winning_percentage):
            # if true retrieve winning counts only
            county_winning_votes = county_votes_total
            county_winning_percentage = county_vote_percentage
            # print candidate as winning candidate
            winning_county = county_name

        # Print winning county to terminal
    winning_county_summary = (
    f"-----------------------\n\n"
    f"Largest County: {winning_county}\n"
    f"Largest County Vote Count: {county_winning_votes}\n"
    f"Largest county Vote Percentage: {county_winning_percentage:.1f}%\n"
    f"-----------------------\n\n"
    f"Candidate Votes\n"
    f"-----------------------\n")
    # print and save winning county summary to terminal
    print(winning_county_summary)
    txt_file.write(winning_county_summary)





# Determine the percentage of votes for each candidate by looping through counts
# 1. Iterate through the candidate list
# for candidate_name in candidate_votes:
     # 2. Retrieve vote count of a candidate
  #  votes = candidate_votes[candidate_name]
    # 3. calculate the percentage of votes
   # vote_percentage = float(votes) / float(total_votes) * 100



# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Format vote percentage to 1 decimal
        vote_percentage = round(vote_percentage, 1)

        # Print each candidate name and results.
        # candidate_results = (
           # f"{candidate_name}: {vote_percentage:,1f}% ({votes:,})\n")
        # Print candidate voter count and percentage.
       # print(candidate_results)
       # txt_file.write(candidate_results)

    # to do: print out each candidate's name, vote count, and percentage of votes
        # print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    # To do: print out winning candidate, vote count and percentage to terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If ture then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print winning candidates results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
# Save winning results to text file
    txt_file.write(winning_candidate_summary)

# Print candidate name and percent.
    # print(f"{candidate_name}: received {vote_percentage}% of the vote.")