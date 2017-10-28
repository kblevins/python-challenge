import os
import csv

fn = input("Enter filename (no extension): ")

fin = "".join(fn + ".csv")

fout =  "".join("output/" + fn + "_summary.txt")

voter_csv = os.path.join("raw_data", fin)

# Lists to store data
voter = []
county = []
candidate = []

with open(voter_csv) as voter_data:
    reader = csv.DictReader(voter_data)
    for row in reader:
        voter.append(row["Voter ID"])

        county.append(row["County"])

        candidate.append(row["Candidate"])

# store total number of votes cast
tot_votes = len(voter)

# store a list of candidates who received votes
un_cand = list(set(candidate))

cand_vote = [0 for i in un_cand]

# store the total number of votes each candidate won
for i in candidate:
    for j in range(0, len(un_cand)):
        if i == un_cand[j]:
            cand_vote[j] = cand_vote[j] + 1

# create empty list to store candidate percentages
cand_pct = []
# store the percentage of votes each candidate won
for i in cand_vote:
    pct = (i/tot_votes)*100
    pct = round(pct, 1)
    cand_pct.append(pct)

# store the winner of the election
winner = un_cand[cand_vote.index(max(cand_vote))]

# create empty string to add candidate summary text lines to
cand_sum = ""
# create a summary text line for each candidate with the name, percentage of vote & total votes
for i in range(0, len(un_cand)):
    cand_sum = "".join(cand_sum + un_cand[i] + ": " + str(cand_pct[i]) + "% (" + str(cand_vote[i]) + ")\n")

# create overall summary text
summary = '''Election Results
-------------------------
Total Votes: {}
-------------------------
{}
-------------------------
Winner: {}
-------------------------
'''.format(tot_votes, cand_sum, winner)

# print summary text
print(summary)

# write summary text to txt file
f = open(fout, 'w+')
f.write(summary)
f.close()