import csv
import re
from datetime import datetime
import statistics as stats

# Lists to store data
date = []
rev = []

# store filenames to read in & to output
fn = input("Input a filename for a csv in the raw_data folder, not including file extension: ")
fin = "".join("raw_data/" + fn + ".csv")
fout =  "".join("output/" + fn + "_summary.txt")

# read in lines to data lists
with open(fin) as csvfile:
    csvreader= csv.DictReader(csvfile)
    for row in csvreader:
        # Add Date
        date.append(row["Date"])

        # Add revenue
        rev.append(int(row["Revenue"]))

# create empty list to fill with re-formatted dates
date2 = []

# reformat dates based on their original format
for row in date:
    if re.match("\w{3}-\d{2}$", row) != None:
        nd = [datetime.strptime(row, '%b-%y')]
    elif re.match("\w{3}-\d{4}", row) !=None:
        nd = [datetime.strptime(row, "%b-%Y")]

    date2.append(nd)

# sum the revenues
revenue = sum(rev)

# zip the dates & revenues together
df = zip(date2, rev)
# sort by date to order chronologically 
df_sort = sorted(df)

# unpack the sorted zip object
df_unzip = list(zip(*df_sort))

# store the sorted dates
date_sorted = df_unzip[0]

# store the sorted revenues
rev_sorted = df_unzip[1]

# create empty list to store revenue changes
rev_chg = []
# calculate revenue changes
for row in range(1, len(rev_sorted)):
    rev_chg.append(rev_sorted[row] - rev_sorted[row-1])

# store max revenue change
max_chg = max(rev_chg)
# store greatest negative (min) revenue change
min_chg = min(rev_chg)

# store the date of the max revenue change
max_mo = date_sorted[rev_chg.index(max_chg) + 1]
# store the date of the min revenue change
min_mo = date_sorted[rev_chg.index(min_chg) + 1]


summary = ('''Financial Analysis
-----------------------------------------
Total Months: {} 
Total Revenue: {}
Average Revenue Change: {}
Greatest Increase in Revenue: {} ({})
Greatest Decrease in Revenue: {} ({}) 
''').format(len(date2), revenue, stats.mean(rev_chg), max_mo[0].strftime("%b-%Y"), 
max_chg, min_mo[0].strftime("%b-%Y"), (min_chg))


print(summary)

f = open(fout, 'w+')
f.write(summary)
f.close()

