
# Add our dependencies
import csv
import os

# Assign a variable to load a file from the path.
# file_to_load= os.path.join('Resources','election_results.csv')

# Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes=0

# 2. Candidate Options and candidate votes
candidate_options=[]
candidate_votes={}

# Winning Candidate and Winning Count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file
with open("Resources/election_results.csv") as election_data:
    file_reader=csv.reader(election_data)
 
    # Read the header row.
    headers=next(file_reader)
    
    #print each row in the csv file.
    for row in file_reader:
        # Add to total vote count.
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name=row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in  candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
            #begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0
            
        #Add a vote to that candidate's count.
        candidate_votes[candidate_name]+=1

# Save the results to our text filel
with open(file_to_save, "w") as txt_file:
    #Print the final count to the terminal.
    election_results=(
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
            
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes=candidate_votes[candidate_name]
        # Calculate the % of votes.
        vote_percentage=float(votes)/float(total_votes)*100
        candidate_results=(
            f"{candidate_name}:{vote_percentage:.1f} % ({votes:,})\n")
            

        """ Print each Candidate'name vote count and percentage of 
        votes to the terminal."""
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        #Determine winning vote count, winning percentage,winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate=candidate_name
            winning_percentage = vote_percentage
        # Print the winning candidate's results to the terminal.
            winning_candidate_summary = (
                f"----------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"----------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidates's results to the text file.
        txt_file.write(winning_candidate_summary)
            
            
            
   

