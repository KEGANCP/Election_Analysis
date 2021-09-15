# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Import the datetime from the dateline module.
import datetime as dt
# use the now() attribute on the datime class to get the present time.
now=dt.datetime.now()
# print the present time.
print("The time now is ", now)

# Assign a variable for the file to load and the path.
file_to_load='Resources/election_results.csv'
# open the election results and read the file.
with open(file_to_load) as election_data:

    # to do: perform analysis
    print(election_data)

# close the file
election_data.close()

