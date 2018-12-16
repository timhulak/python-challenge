#import Dependencies/Modules
import os
import csv
import numpy as np

#encoding path
from pathlib import Path
pyPoll_path = '/Users/timhulak/Desktop/USC_Viterbi/homework/python/python-challenge/PyPoll/resources/pyPoll.csv'

#Vars and Lists to store data
votes = []


with open(pyPoll_path, newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
    #The total number of votes cast
        votes.append(int(row[0]))

    total_votes = sum(votes)
    #A complete list of candidates who received votes


    #The percentage of votes each candidate won


    #The total number of votes each candidate won


    #The winner of the election based on popular vote.


    print('Election Results')
    print('---------------------')
    print(f'Total Votes: {total_votes}')
    print('---------------------')
    #print(f'Khan: {khan}')
    #print(f'Correy: {correy}')
    #print(f'Li:  {li}')
    #print(f'O\'Tooley: {otooley}')
    #print('---------------------')
    #print(f'Winner: {winner}')
    #print('---------------------')
