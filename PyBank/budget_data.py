import os, csv
from pathlib import Path
# Assign file location with the pathlib library
csv_file_path = os.path.join("Resources","budget_data.csv")
#Initialize variables
mcount = 0
total = 0
reValue = 0
Diff = 0
DiffMax = 0
DiffMin = 0
#Open and read CSV file
with open(csv_file_path, newline='') as budget:
    csvreader = csv.reader(budget, delimiter=',')
    csv_header = next(csvreader)
    print(f'Financial Analysis'+'\n')
    print(f'----------------------------'+'\n')
    for i in csvreader:
        month = i[0]
        Amount = i[1]
        iAmount = int(Amount)
        Diff =  iAmount - reValue
        #Placeholder to track greatest increase in profits (financial analysis)
        if DiffMax < Diff:
           DiffMax = Diff
           DiffMaxDate = month
        #Placeholder to track greatest decrease in profits (financial analysis)
        if DiffMin > Diff:
           DiffMin = Diff
           DiffMinDate = month
        PreValue = iAmount
        # Get total months (financial analysis)
        mcount = mcount + 1
        total += int(Amount)
## Display Results ##
#The total number of months included in the dataset
print(f'Total Months : {mcount}')
#The total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {total}')
# Greatest increase in profit
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')







