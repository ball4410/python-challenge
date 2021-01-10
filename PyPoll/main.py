#Modules
import os
import csv
import pandas as pd

# Get data file needed for analysis
election_data_path = "./Resources/election_data.csv"


#Store data into a pandas data frame
election_file_df = pd.read_csv(election_data_path)

#Create variables to store values needed for summary
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0

#Get unique candidate names
candidates = [election_file_df["Candidate"].unique()]


# Open the file above and store contents 
with open(election_data_path) as pollfile:
    csvreader = csv.reader(pollfile, delimiter=",")
    
    #The file has a header row so store this seperately from the data
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_votes = total_votes + 1
        
        if row[2] == 'Khan':
            khan_votes = khan_votes + 1
        elif(row[2] == 'Correy'):
            correy_votes = correy_votes + 1
        elif(row[2] == 'Li'):
            li_votes = li_votes + 1
        elif(row[2] == "O'Tooley"):
            tooley_votes = tooley_votes + 1

#Store unique candidates and total votes in a new data frame
summary_df = pd.DataFrame({"Candidates": ["Khan", "Correy", "Li", "O'Tooley"],
                          "Total_Votes": [khan_votes, correy_votes, li_votes, tooley_votes]})

#Format percentages
khan_percentage = "{:.3%}".format(khan_votes/total_votes)
correy_percentage = "{:.3%}".format(correy_votes/total_votes)
li_percentage = "{:.3%}".format(li_votes/total_votes)
tooley_percentage = "{:.3%}".format(tooley_votes/total_votes)


#Find the max number of votes
most_votes = summary_df["Total_Votes"].max()

#Find the name of the candidate with the max votes
get_winner = summary_df.loc[summary_df["Total_Votes"] == most_votes, [
    "Candidates"]]
winner = get_winner["Candidates"]

#Print summary
print("Election Results")
print("-----------------")
print(f"Total Votes: {total_votes}")
print("-----------------")
print(f"Khan {khan_percentage} ({khan_votes})")
print(f"Correy {correy_percentage} ({correy_votes})")
print(f"Li {li_percentage} ({li_votes})")
print(f"O'Tooley {tooley_percentage} ({tooley_votes})")
print("-----------------")
print(f"Winner {winner}")