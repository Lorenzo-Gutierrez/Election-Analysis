# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to save file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize and set total vote counter variable to zero
total_votes = 0
# Declare list to contain candidate names
candidate_options = []
# Create dictionary to store votes per candidate
candidate_votes = {}
# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load, encoding='UTF-8') as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0
        # Add to candidate vote count
        candidate_votes[candidate_name] += 1
# Save results to a txt file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Save final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print candidate name, vote count, percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        #Save final vote count to the text file.
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # and set the winning_candidate equal to the candidates name.
            winning_candidate = candidate_name

    # Print the winning candidate name, vote count, and percentage.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
