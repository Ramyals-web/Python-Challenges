import os
import csv

myfile = os.path.join("Python-Challenges/PyPoll/Resources/election_data.csv")

total = 0
votes = []
candidates = []
khan = 0
correy= 0
li= 0
otooley = 0
max_value=0
winner = ""
poll = []

with open(myfile) as csv_file:
    csvreader = csv.reader(csv_file)
    csv_header= next(csv_file)
    print(f"Header:{csv_header}")

    for row in csvreader:
       # print(row)
        total = total+1
        votes.append(row[0])
        candidates.append(row[2])
    if row[2]== "Khan":
        khan = khan+1
    elif row[2] == "correy":
        correy= correy+1
    elif row[2] == "li":
        li= li+1
    elif row[2] == "otooley":
        otooley= otooley+1
    
    khan_percentage = (khan/total)*100
    correy_percentage = (correy/total)*100
    li_percentage = (li/total)*100
    otooley_percentage = (otooley/total)*100

    
    for i in poll:
        votes=poll[i]
    if votes > max_value:
        max_value = votes
        winner = i
        print('--------------------------------')
        print(f'Winner:         {i}')
        print('--------------------------------')


    


    analysis = (f"'Election Results \n"
    f"--------------------------\n"
    f" Total Votes: {total}\n'"
    f"--------------------------\n"
    f" Khan:{khan_percentage},({khan})\n"
    f" Correy:{correy_percentage},({correy})\n"
    f" li: {li_percentage},({li})\n"
    f" OTooley: {otooley_percentage},({otooley})\n"
    f"--------------------------\n'")
    print(analysis)

    textfile = os.path.join("Python-Challenges/PyPoll/Analysis")
    with open(textfile,'w') as txtfile:
        txtfile.write(analysis)

    
    

        

       

    
    

    
