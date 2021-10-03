
# The total number of votes cast 
# A complete list of candidates who received votes 
# The percentage of votes each candidate won 
# The total number of votes each candidate won 
# The winner of the election based on popular vote



import csv


# Assign file location with the pathlib library
csvpath = r"E:\Georgia Tech\02-Homework\03-Python\python-challenge\Instructions\PyPoll\Resources\election_data.csv"


# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv in default read mode with context manager
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
   
    # Iterate through the rows in csv file
    for row in csvreader:

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")