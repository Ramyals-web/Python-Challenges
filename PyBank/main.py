import os
import csv

myfile = os.path.join("/Users/krengasa/Documents/BootCamp/HomeWork/Python-Challenges/Instructions/PyBank/Resources/budget_data.csv")
total=0
profit_and_loss=0
counter=0
total_months = []
profit_change =[]
profit=[]
increase_profit=0
decrease_profit=0
avg_profit_change=0
with open(myfile) as csv_file:
    csvreader = csv.reader(csv_file)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csvreader:
        print(row)
        total = total+1
 #       if counter!=0:
        profit_and_loss = profit_and_loss + int(row[1])
 #       counter = counter + 1
        
        profit.append(int(row[1]))
       # profit_change.append(int(row[1]))
    print (len(profit))
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])
        increase_profit = max(profit_change)
        decrease_profit = min(profit_change)
        
    avg_profit_change = round(sum(profit_change)/len(profit_change),2)
    avr_change = profit_and_loss/total
    analysis = (f"'Financial Analysis \n"
    f"--------------------------\n"
    f" Total Months: {total}\n"
    f" Total profit and loss: {profit_and_loss}\n"
    f"Average Change:{avg_profit_change}\n"
    f"Greatest Increase in Profits:{increase_profit}\n"
    f"Greatest Decrease in Profits:{decrease_profit}\n'") 

print(analysis)

textfile = os.path.join("/Users/krengasa/Documents/BootCamp/HomeWork/Python-Challenges/Instructions/PyBank/analysis/Budget_ananlysis.txt")
with open(textfile,'w') as txtfile:
    txtfile.write(analysis)

