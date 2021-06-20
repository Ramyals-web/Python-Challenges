import os
import csv

myfile = os.path.join("/Users/krengasa/Documents/BootCamp/HomeWork/Python-Challenges/Instructions/PyPoll/Resources/election_data.csv")

with open(myfile) as csv_file:
    csvreader = csv.reader(csv_file)
    csv_header= next(csv_file)
    print(csv_header)

    total = 0
    totalvotes = []
    candidates = []
    applicant = 0
    number_votes=0

    for row in csvreader:
        total = total+1
    if row[2] in totalvotes:
        totalvotes[row[2]] = totalvotes+1
    else:
        totalvotes[row[2]]=1

    
    

        

       

    
    

    
