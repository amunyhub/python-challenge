#Open the pybank file
import os
import csv

#empty variables
num_of_rows = 0
total = 0
olderprofitloss = 0
newprofitloss = 0
change = 0
total_change = 0
numchanges = 0
greatestincrease = 0
greatestchange_date = 0
greatestdecrease = 0
greatestdecrease_date = 0
#path to file from where code is in my folders
pybank_csv = os.path.join("Resources","budget_data.csv")

#open file for read
with open(pybank_csv,"r") as budget:
    csv_reader = csv.reader(budget,delimiter=',')

#gets rid of header 
    csv_header = next(budget)

#find total number of months last row index for total # of months of data question-HELP HERE won't add
# def convert_tolist(csv_reader):
#     csv_reader_delim = csv_reader.split("n") 
#     csv_reader=list(csv_reader(csv_reader_delim))

    for row in csv_reader:
#converting values to int 
        # date_num= row[1]
        # date_num=int(date_num)
        # row[1]=date_num
#add up total values, total value of the profits and losses column
        # date_num= row[1]
        num_of_rows += 1
        newprofitloss=int(row[1])
        total += newprofitloss

#takes care of the first month that has no previous month
        if olderprofitloss != 0 :
            change = newprofitloss - olderprofitloss
            total_change += change
            numchanges += 1
        olderprofitloss = newprofitloss
# look for the greatest increase and compares as it loops
        if change > greatestincrease:
            greatestincrease = change
            greatestincrease_date = row [0]
# look for the greatest decrease and compares as it loops
        if change < greatestdecrease:
            greatestdecrease = change
            greatestdecrease_date = row [0]

# print all items to terminal
Financial_Analysis= f"""

Financial Analysis
------------------
Total Months: {num_of_rows}
Total: ${total}
Average Change: ${total_change/numchanges:.2f}
Greatest Increase in Profits:{greatestincrease_date} (${(greatestincrease)})
Greatest Decrease in Profits:{greatestdecrease_date} (${(greatestdecrease)})
"""
#write all prints to output text file in  analysis folder
output_path = os.path.join("Analysis","Financial_Analysis_Output.txt")

print(Financial_Analysis)

with open('Financial_Analysis_Output.txt', 'w') as outputFile:
    outputFile.write(Financial_Analysis)

