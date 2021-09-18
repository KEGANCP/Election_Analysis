# Election_Analysis

## Audit Overview
Tom and Steve, representatives of the Colorado Board of Elections, requested assistance to accumulate results of a recent congressional election. After gathering results to display the total number of votes cast, including total votes for each candidate, we were able to quantify these as percentages for each candidate and determine a winner of the election by popular vote. With further coding we were also able to include data specific to each counties voter turnout.

## Election Data Resources
Utilizing the [election_results](https://github.com/KEGANCP/Election_Analysis/blob/main/Resources/election_results.csv) data set within Python 3.8 along with Visual Studio Code 1.60 we were able to consolidate these requested results as shown below.

## Summary of Election Analysis
Using our raw data set, we were able to identify our total number of votes of 369,711. We grew off of this finding to further our analysis and determine all of the candidates involved, as well as their total votes received and what percentage of total votes they received in this election. Once we identified all this data we were able to conclude our over all election winner, based on popular vote.
### 
The below image will prove a visual of these findings. This analysis is confirming 369,711 total votes were cast with the most votes (306,055), 82.8% of votes coming out of Denver, 10.5% from Jefferson, and 6.7% from Arapahoe.
We were also able to consolidate the candidate data which resulted in Diana DeGette receiving the most votes with 272,892 and 73.8% of votes cast. Charles Casper Stockman received the second most votes at 85,213 and 23% of votes cast, and Raymon Anthony getting the least total votes at 11,606 and 3.1% of votes cast.
![This is an image](https://github.com/KEGANCP/Election_Analysis/blob/main/Resources/Election_results.png)

### Sample code
Below is an example of code that was created to identify the winner of the election by breaking down votes per each candidate, as well percentage of votes per candidate.
![This is an image](https://github.com/KEGANCP/Election_Analysis/blob/main/Resources/sample_code_winning_candidate.png)

## Election Audit-Summary
To conclude this analysis, it has become apparent that this script can be used for many future elections. Some modifications that can easily be generated to process other elections include replacing our current "county" column to other required categories that better fit the type of the election. This feature can become broader for larger elections. This script can also be utilized to quantify and show specific voter participation within each county. This would help candidates determine where to focus more of their funding and energy in campaigning for future elections. 
