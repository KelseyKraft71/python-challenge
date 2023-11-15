#import libraries needed
import os
import csv

#specify file to read from 
election_csv = os.path.join("Resources", "election_data.csv")

#declare starting values of variables and lists
total_votes = 0
candidates = []
candidates_votes = []
candidates_votes_prct = []
total_votes = 0
total_votes_counter_0 = 0
total_votes_counter_1 = 0
total_votes_counter_2 = 0

#open file and read as csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip the header row
    csv_header = next(csvfile)

    #loop through the rows of the sheet
    for row in csvreader:
        #increase total votes counter for every row (every row is one vote)
        total_votes = total_votes + 1 
        #declare column 3 as variable candidate_name
        candidate_name = row[2]
        #check if current row value is not in the candidates name list
        if candidate_name not in candidates: #had some help from ChatGPT here
            #name is not already in list, add it
            candidates.append(row[2])
        #check if current row value matches value of candidate at index 0
        if candidate_name in candidates[0]:
            #it does, increase index 0 vote counter by 1
            total_votes_counter_0 += 1
        #check if current row value matches value of candidate at index 1
        elif candidate_name in candidates[1]:
            #it does, increase index 1 vote counter by 1
            total_votes_counter_1 += 1
        #check if current row value matches value of candidate at index 2
        elif candidate_name in candidates[2]:
            #it does, increase index 2 vote counter by 1
            total_votes_counter_2 += 1
        
    #append vote counters for each candidate to candidates votes list
    candidates_votes.append(int(total_votes_counter_0))
    candidates_votes.append(int(total_votes_counter_1))
    candidates_votes.append(int(total_votes_counter_2))

#calculate candidates' vote percentages and round to 3 decimal places
percentage_0 = round((candidates_votes[0] / total_votes) * 100, 3)
percentage_1 = round((candidates_votes[1] / total_votes) * 100, 3)
percentage_2 = round((candidates_votes[2] / total_votes) * 100, 3)
#append percentages for each candidate to candidates votes percentages list
candidates_votes_prct.append(percentage_0)
candidates_votes_prct.append(percentage_1)
candidates_votes_prct.append(percentage_2)

#specify output path for new text file
output_path = os.path.join("output", "results.txt")

#https://www.pythontutorial.net/python-basics/python-write-text-file/
#open output path in write mode
with open(output_path, "w") as f:

    #https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
    #write lines to text file with line breaks for formatting
    f.write("Election Results\n")
    f.write("-----------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-----------------------\n")
    f.write(f"{candidates[0]}: {candidates_votes_prct[0]}% ({candidates_votes[0]})\n")
    f.write(f"{candidates[1]}: {candidates_votes_prct[1]}% ({candidates_votes[1]})\n")
    f.write(f"{candidates[2]}: {candidates_votes_prct[2]}% ({candidates_votes[2]})\n")
    f.write("-----------------------\n")
    f.write(f"Winner: {candidates[1]}")

#print results to console
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------")
print(f"{candidates[0]}: {candidates_votes_prct[0]}% ({candidates_votes[0]})")
print(f"{candidates[1]}: {candidates_votes_prct[1]}% ({candidates_votes[1]})")
print(f"{candidates[2]}: {candidates_votes_prct[2]}% ({candidates_votes[2]})")
print("-----------------------")
print(f"Winner: {candidates[1]}")