#Open the pybank file
import os
import csv
# import pandas as pd

#empty dictionaries to hold values we will need
total_months = 0
# Total = dict()
# Average_Change = dict()
# Greatest Increase in Profits = dict()
# Greatest Decrease in Profits = dict()

#path to file from where code is in my folders
pybank_csv = os.path.join("Resources","budget_data.csv")

#open file for read
with open(pybank_csv,"r") as budget:
    csvreader = csv.reader(budget,delimiter=',')

#total months included in the dataset

#get rid of header and prints it
    csv_header = next(csvreader)
    #print(f"Header:{csv_header}")
    
    total_months = len(list(csvreader))
    print(total_months)

#get rid of header and prints it
    # csv_header = next(csvreader)
    # print(f"Header:{csv_header}")

# find total number of last row index for total # of months of data question

