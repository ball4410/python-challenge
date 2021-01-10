#Modules
import os
import csv

# Get data file needed for analysis
budget_path = "./Resources/budget_data.csv"

#Create array to store months and loss/profits for our summary
number_of_months = []
net_total = []
changes = []

# Open the file above and store contents 
with open(budget_path) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    #print(csvreader)
    
    #The file has a header row so store this seperately from the data
    csv_header = next(csvreader)
    
    for row in csvreader:
        number_of_months.append(row[0])
        net_total.append(int(row[1]))
        #print(row[1])
        
#Verify results
len(number_of_months)
sum(net_total)

#Store the difference for loss/profits into an array called changes
changes = [net_total[i+1] - net_total[i] for i in range(len(number_of_months) - 1)] 

#Verify Result
#sum(changes)/len(changes)
#changes

#Find greatest increase profit
max_change = max(changes)

#Find greatest descrease loss
min_change = min(changes)

#Find month for greatest increase and decrease

index = 1
greatest_increase_month = 'Feb-2012'
greatest_decrease_month = 'Feb-2012'

for change in changes:
    if(change == max_change):
        #print(number_of_months[index])
        greatest_increase_month = number_of_months[index]
        
    else:
        index = index+ 1
        
index = 1      
for change in changes:
    if(change == min_change):
        #print(number_of_months[index])
        greatest_decrease_month = number_of_months[index]
        
    else:
        index = index+ 1
        
#Print summary
print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(number_of_months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: {sum(changes)/len(changes)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${max_change})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${min_change})")