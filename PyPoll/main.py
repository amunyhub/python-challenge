#Open the pypoll file
import os
import csv

num_of_votes= 0
candidates = 0
#path to file from where code is in my folders
pypoll_csv = os.path.join("Resources","poll_data.csv")

#open file for read
with open(pypoll_csv,"r") as results:
    csv_reader = csv.reader(results,delimiter=',')

#gets rid of header  
    csv_header = next(results)

    for row in csv_reader:
#add up number of rows
        num_of_votes+= 1   
# prints all for every vote, need to make show up only once
    for i in csv_reader:
        candidates=row[2]
        if i in candidates != csv_reader[i+1]
        print(i)
        else:
            sv_reader[i] == csv_reader[i+1]
        break

 #only showeach name one time   


#Results
print("Election Results")
print("------------------")
print(f"Total Votes: {num_of_votes}") 
print("------------------")
print(candidates)
 