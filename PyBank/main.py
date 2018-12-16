#import Dependencies/Modules
import os
import csv
import numpy as np

#encoding path
from pathlib import Path
pyBank_path = '/Users/timhulak/Desktop/USC_Viterbi/homework/python/python-challenge/PyBank/resources/pyBank.csv'

#Vars and Lists to store data
counter = 0
months = []
prev = 867884
changes = []

with open(pyBank_path, newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
    #The total number of months included in the dataset
        months.append(int(row[1]))
        change = int(row[1]) - prev
        changes.append(change)
        prev = int(row[1])
    #The total net amount of "Profit/Losses" over the entire period
    total_net = sum(months)

    #The average change in "Profit/Losses" between months over the entire period
    average = round(sum(changes)/len(changes),2)

    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(changes)

    #The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(changes)

    print('Financial Analysis')
    print('---------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total Net: {total_net}')
    print(f'Average Change: {average}')
    print(f'Greatest Increase: Feb-12 {greatest_increase}')
    print(f'Greatest Decrease: Sep-13 {greatest_decrease}')
