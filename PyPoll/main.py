import os
import csv

myfile = os.path.join("/Users/krengasa/Documents/BootCamp/HomeWork/Python-Challenges/PyPoll/Resources/election_data.csv")

total = 0
votes = []
candidates =[]
khan = 0
correy= 0
li= 0
otooley = 0
winner = ""


with open(myfile) as csv_file:
    csvreader = csv.reader(csv_file)
    csv_header= next(csv_file)
    #print(f"Header:{csv_header}")

    for row in csvreader:
       # print(row)
        total = total+1
        #votes.append(cast_votes)
        candidate=(row[2])
        candidates.append(row[2])
    for candidate in candidates:
        if candidate == "Khan":
         khan= khan+1
        elif candidate == "correy":
            correy= correy+1
         
        elif candidate == "li":
         li= li+1
        elif candidate== "otooley":
         otooley= otooley+1
    
    khan_percentage = (khan/total)*100
    correy_percentage = (correy/total)*100
    li_percentage = (li/total)*100
    otooley_percentage = (otooley/total)*100


    if khan  > max(correy, li, otooley):
         winner = "khan"
    elif correy > max(khan, li, otooley):
            winner = "correy"
    elif li > max(khan, correy, otooley):
         winner = "li"
    else:
        winner = "otooley"
    
    

    analysis = (f" Election Results \n"
    f"--------------------------------\n"
    f" Total Votes: {total}\n"
    f"--------------------------------\n"
    f" Khan:{khan_percentage:.2f}% which is {khan} votes\n"
    f" Correy:{correy_percentage:.2f}% which is {correy} votes\n"
    f" li: {li_percentage:.2f}% which is {li} votes\n"
    f" OTooley: {otooley_percentage:.2f}% which is {otooley} votes\n"
    f"--------------------------------\n"
    f" Winner: {winner:}\n"
    f"--------------------------------\n")
    
    print(analysis)

    textfile = os.path.join("/Users/krengasa/Documents/BootCamp/HomeWork/Python-Challenges/PyPoll/analysis/election_analysis.txt")
    with open(textfile,'w') as txtfile:
        txtfile.write(analysis)

    
    

        

       

    
    

    
