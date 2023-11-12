import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = []
candidates_votes = []
candidates_votes_prct = []
total_votes = 0
total_votes_counter_0 = 0
total_votes_counter_1 = 0
total_votes_counter_2 = 0

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile)

    for row in csvreader:
        total_votes = total_votes + 1 
        candidate_name = row[2]
        #had some help from ChatGPT here
        if candidate_name not in candidates:
            candidates.append(row[2])
        if candidate_name in candidates[0]:
            total_votes_counter_0 += 1
        elif candidate_name in candidates[1]:
            total_votes_counter_1 += 1
        elif candidate_name in candidates[2]:
            total_votes_counter_2 += 1
        
    candidates_votes.append(int(total_votes_counter_0))
    candidates_votes.append(int(total_votes_counter_1))
    candidates_votes.append(int(total_votes_counter_2))

percentage_0 = round((candidates_votes[0] / total_votes) * 100, 3)
percentage_1 = round((candidates_votes[1] / total_votes) * 100, 3)
percentage_2 = round((candidates_votes[2] / total_votes) * 100, 3)
candidates_votes_prct.append(percentage_0)
candidates_votes_prct.append(percentage_1)
candidates_votes_prct.append(percentage_2)

output_path = os.path.join("output", "results.txt")

#https://www.pythontutorial.net/python-basics/python-write-text-file/
#https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
with open(output_path, "w") as f:

    f.write("Election Results\n")
    f.write("-----------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-----------------------\n")
    f.write(f"{candidates[0]}: {candidates_votes_prct[0]}% ({candidates_votes[0]})\n")
    f.write(f"{candidates[1]}: {candidates_votes_prct[1]}% ({candidates_votes[1]})\n")
    f.write(f"{candidates[2]}: {candidates_votes_prct[2]}% ({candidates_votes[2]})\n")
    f.write("-----------------------\n")
    f.write(f"Winner: {candidates[1]}\n")

print("Election Results")
print("-----------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------")
print(f"{candidates[0]}: {candidates_votes_prct[0]}% ({candidates_votes[0]})")
print(f"{candidates[1]}: {candidates_votes_prct[1]}% ({candidates_votes[1]})")
print(f"{candidates[2]}: {candidates_votes_prct[2]}% ({candidates_votes[2]})")
print("-----------------------")
print(f"Winner: {candidates[1]}")