#Open the pybank file
import os
import csv

#empty dictionaries to hold values we will need
num_of_rows = 0
total = 0

#path to file from where code is in my folders
pybank_csv = os.path.join("Resources","budget_data.csv")
# df=pybank_csv
#open file for read
with open(pybank_csv,"r") as budget:
    csv_reader = csv.reader(budget,delimiter=',')

#get rid of header and prints it 
    csv_header = next(budget)

#find total number of months last row index for total # of months of data question-HELP HERE won't add
# def convert_tolist(csv_reader):
#     csv_reader_delim = csv_reader.split("n") 
#     csv_reader=list(csv_reader(csv_reader_delim))

    for row in csv_reader:
#converting values to int 
        date_num= row[1]
        date_num=int(date_num)
        row[1]=date_num
#add up total values, total value of the profits and losses column
        date_num= row[1]
        total += date_num
#add up number of rows
       num_of_rows+= 1   
# calculate average
        if 
print(f"Total Months: {num_of_rows}") 
print(f"Total: {total}")
 
    




# total # of months

       