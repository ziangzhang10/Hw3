import os
import sys
import csv

# code to analyse the election data
election_data = os.path.join(".", "election_data.csv")
election_analysis = os.path.join(".", "election_analysis.txt")

# define a function to check if a name is in the candidate list
def checkCandidate(name, candidate_list):
    for i in range(len(candidate_list)):
        if name == candidate_list[i]["name"]:
            index = i
            break # must break out of loop, else it'll keep checking!
        else:
            index = -9999
    return index

# generate a list to keep track of all candidates
candidate_list = []
with open (election_data, "r", newline="") as filehandle:
    # skip first line
    next(filehandle)
    # read csv file
    csvreader = csv.reader(filehandle)
    total_votes = 0
    # loop through all rows
    for row in csvreader:
        total_votes += 1
        name = row[2]
        # if it's the first candidate to be recorded
        if len(candidate_list) == 0:
            candidate = {
                "name":name,
                "votes":1
                }
            candidate_list.append(candidate)
        # if it's not the first
        else:
            # check if this candidate is in our list
            index = checkCandidate(name, candidate_list)
            # if not
            if index == -9999:
                candidate = {
                    "name":name,
                    "votes":1
                    }
                candidate_list.append(candidate)
            # if this is candidate is already in our list
            else:
                candidate_list[index]["votes"] += 1
 
# generate file for analysis
with open (election_analysis, "w+") as filehandle:
    # keep a profile for winner
    winner = {
        "name":"null",
        "votes":0
        }
    filehandle.write("Election results\n")
    filehandle.write("-"*32 +"\n")
    filehandle.write(f"Total Votes: {total_votes}\n")
    # loop through all counted candidates
    for candidate in candidate_list:
        name = candidate["name"]
        votes = candidate["votes"]
        percentage = votes/total_votes
        filehandle.write(f"{name}: {percentage: .3%} ({votes})\n")
        # check if said candidate is winner
        if candidate["votes"] > winner["votes"]:
            winner["name"] = candidate["name"]
            winner["votes"] = candidate["votes"]
    filehandle.write("-"*32 +"\n")
    filehandle.write(f"Winner: {winner['name']}\n")
    filehandle.write("-"*32 +"\n")


# print to screen as well
with open (election_analysis, "r") as filehandle:
    print(filehandle.read())
