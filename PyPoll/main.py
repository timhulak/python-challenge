#import Dependencies/Modules
import os
import csv

#encoding path
pyPoll_path = os.path.join("resources","pyPoll.csv")

with open(pyPoll_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #The total number of votes cast
    total_votes = sum(tuple([1 for row in csvreader]))

    #A complete list of candidates who received votes
    canidate_list = tuple([row[2] for row in csvreader])
    unique_canidate_list = []
    for name in canidate_list:
        if name not in unique_canidate_list:
            unique_canidate_list.append(name)

    #The total number of votes each candidate won
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    for row in csvreader:
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        else:
            otooley += 1

    #The percentage of votes each candidate won
    khan_percent = (float(khan/total_votes)) * 100
    correy_percent = (float(correy/total_votes)) * 100
    li_percent = (float(li/total_votes)) * 100
    otooley_percent = (float(otooley/total_votes)) * 100


    #The winner of the election based on popular vote.
    results = {'khan': khan, 'correy': correy, 'li': li, 'otooley': otooley}
    winner = max(results, key=results.get)

    print('Election Results:')
    print('---------------------')
    print(f'Total Votes: {total_votes}')
    print('---------------------')
    print(f'Khan: {khan_percent}% ({khan})')
    print(f'Correy: {correy_percent}% ({correy})')
    print(f'Li:  {li_percent}% ({li})')
    print(f'O\'Tooley: {otooley_percent}% ({otooley})')
    print('---------------------')
    print(f'Winner: {winner}')
    print('---------------------')
