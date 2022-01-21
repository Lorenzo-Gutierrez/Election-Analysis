# Election-Analysis

## Overview
The purpose of this project was to analyze the results of a congressional election for one precinct in Colorado. I was asked to take a raw csv file containing all of the votes cast and to calculate the following:
- Total votes cast in the election
- Number of votes cast in each county, and percentage of total votes for each county
- County with the highest number of votes
- Number of votes cast for each candidate, and percentage of total votes for each candidate
- Which candidate won the election, and with what vote count and percentage of total vote

Additionally, this info was required to be written to a text file to be provided to the election commission.

## Results
The results of the analysis were:
- 369,711 total votes cast in the election
- Number of votes cast in each county, and percentage of total votes for each county:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- Denver County had the highest number of votes with 306,055
- Number of votes cast for each candidate, and percentage of total votes for each candidate:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
- Which candidate won the election, and with what vote count and percentage of total vote
    - Winner: Diana DeGette
    - Winning Vote Count: 272,892
    - Winning Percentage: 73.8%

## Summary

As you can see, my code was able to quickly and effectively provide an analysis of the election results. This code could immediately be used in other congressional elections, as long as the data file format was the same. In fact, with some modifications it could be used in larger elections or to provide deeper analysis. Examples of such modifications are:
- Modifying the file reader code to read other file formats
- Adding code to expand analysis to the state level and not just county
- Add code to pull in voter registration in order to calculate percentage of registered voters that participated
- Add code that would calculate electoral college votes based on county and state results, in the case of a presidential election
