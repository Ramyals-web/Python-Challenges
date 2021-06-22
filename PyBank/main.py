#importing 
import os
import csv

# Getting Data from Resources file
myfile = os.path.join("/Users/krengasa/Documents/BootCamp/HomeWork/Python-Challenges/PyBank/Resources/budget_data.csv")

# Declaring Variables
total=0
profit_and_loss=0
counter=0
total_months = []
profit_change =[]
profit=[]
increase_profit=0
decrease_profit=0
avg_profit_change=0
month=[]

# Opening and reading a file
with open(myfile) as csv_file:
    csvreader = csv.reader(csv_file)
    
    # read and skips the header row
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    # Read entire data
    for row in csvreader:
        #print(row)

        #Print the total
        total = total+1
        profit_and_loss = profit_and_loss + int(row[1]) 
        profit.append(int(row[1]))
        month.append(row[0])
    #print (len(profit))
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])
          
        #Finding the increase and decrease change in profit/loss
    increase_profit = max(profit_change)
    decrease_profit = min(profit_change)
    highest_month = profit_change.index(increase_profit) +1
    lowest_month = profit_change.index(decrease_profit) +1
            
        #Assign the values
    Greatest_increase = month[highest_month]
    Greatest_decrease = month[lowest_month]
        
        # finding the average change
    avg_profit_change = round(sum(profit_change)/len(profit_change),2)
    avr_change = profit_and_loss/total

    #Storing all the results in Analysis

    analysis = (f"--------------------------\n"
    f"Financial Analysis \n"
    f"--------------------------\n"
    f" Total Months: {total}\n"
    f" Total profit and loss: {profit_and_loss}\n"
    f" Average Change:{avg_profit_change}\n"
    f" Greatest Increase in Profits: {(Greatest_increase)},({increase_profit})\n"
    f" Greatest Decrease in Profits: {(Greatest_decrease)},({decrease_profit})\n")

# Printing the Analysis in Terminal
print(analysis)

# Creating and Writing a text file in Analysis folder.
textfile = os.path.join("/Users/krengasa/Documents/BootCamp/HomeWork/Python-Challenges/PyBank/analysis/Budget_analysis.txt")
with open(textfile,'w') as txtfile:
    txtfile.write(analysis)

