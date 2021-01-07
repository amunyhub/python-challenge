#Open the pypoll file
import os
import csv

#variables
num_of_votes= 0
candidates = 0
all_candidates = 0
totalvotes = 0
votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0
vote_totals = 0
most_votes = 0
#path to file from where code is in my folders
pypoll_csv = os.path.join("Resources","poll_data.csv")

#open file for read
with open(pypoll_csv,"r") as results:
    csv_reader = csv.reader(results,delimiter=',')

#gets rid of header  
    csv_header = next(results)
    all_candidates=[]
    vote_totals=[]

    for row in csv_reader:
#add up number of rows
            num_of_votes+= 1
            x=row[2]
# getting individual candidate names
            if x not in all_candidates:
                 all_candidates.append(x)
#find of votes each candidate got
            if row[2]== "Khan":
                votes_khan += 1
            if row[2]== "Correy":
                votes_correy += 1
            if row[2]== "Li":
                votes_li += 1
            if row[2]== "O'Tooley":
                votes_otooley += 1

#find winner dict for candidates and votes
dict_election_results= {
    "Khan": votes_khan,
    "Correy": votes_correy,
    "Li": votes_li,
    "O'Tooley": votes_otooley
}

for candidate, votes in dict_election_results.items():
    if votes > most_votes:
        most_votes = votes
        winner= candidate

#Results

Election_Results= f"""
Election Results
------------------
Total Votes: {num_of_votes}
------------------
{all_candidates[0]}: {(votes_khan/num_of_votes)*100:.3f}% ({votes_khan})
{all_candidates[1]}: {(votes_correy/num_of_votes)*100:.3f}% ({votes_correy})
{all_candidates[2]}: {(votes_li/num_of_votes)*100:.3f}% ({votes_li})
{all_candidates[3]}: {(votes_otooley/num_of_votes)*100:.3f}% ({votes_correy})         
------------------
Winner: {winner}
------------------
"""

#write all prints to output text file in  analysis folder
output_path = os.path.join("..","Pypoll","Analysis","Election_Results_Output.txt")

print(Election_Results)

with open(output_path, 'w') as outputFile:
    outputFile.write(Election_Results)

