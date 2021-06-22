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
        candidate=(row[2])
        candidates.append(row[2])
    
    for candidate in candidates:

        if candidate == "Khan":
            khan= khan+1
        elif candidate == "Correy":
            correy= correy+1
        elif candidate == "Li":
            li= li+1
        elif candidate== "O'Tooley":
            otooley= otooley+1
    
    khan_percentage = (khan/total)*100
    correy_percentage = (correy/total)*100
    li_percentage = (li/total)*100
    otooley_percentage = (otooley/total)*100


    if khan  > max(correy, li, otooley):
        winner = "Khan"
    elif correy > max(khan, li, otooley):
        winner = "Correy"
    elif li > max(khan, correy, otooley):
         winner = "Li"
    else:
        winner = "O'Tooley"
    
    

    analysis = (f" Election Results \n"
    f"--------------------------------\n"
    f" Total Votes: {total}\n"
    f"--------------------------------\n"
    f" Khan:{khan_percentage:.2f}% which is {khan} votes\n"
    f" Correy:{correy_percentage:.2f}% which is {correy} votes\n"
    f" Li: {li_percentage:.2f}% which is {li} votes\n"
    f" O'Tooley: {otooley_percentage:.2f}% which is {otooley} votes\n"
    f"--------------------------------\n"
    f" Winner: {winner:}\n"
    f"--------------------------------\n")
    
    print(analysis)

    textfile = os.path.join("/Users/krengasa/Documents/BootCamp/HomeWork/Python-Challenges/PyPoll/analysis/election_analysis.txt")
    with open(textfile,'w') as txtfile:
        txtfile.write(analysis)

    
    

        

       

    
    

    
