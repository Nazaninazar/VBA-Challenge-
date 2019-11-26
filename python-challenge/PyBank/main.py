#Create a Dir/Folder called python-challenge
#mkdir python-challenge 
 # cd ppython-challenge 
   # mkdir PyBank
      #cd PyBank 
       # touch main.py 
    #cd 
    #  cd Pypoll
    #  Mkdir Pypoll 
         #cd Pypoll
    # touch main.py       
#PyBank
#open main.py 
   
#import file

#create file paths across operating systems
import os
import csv
#path to the csvfile
csvpath = os.path.join('Resources', 'budget_data.csv')

#lists to add csv data 
month_count=[]s
changes =[]
date_count = []

 # open CSV file 
with open(csvpath, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    
for row in csvreader:
    month_count.append(row[0])
        
        
#iterate through the values and add them to the empty list 
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
#evaluate the max and min from the list made
increase = max(change_profit)
decrease = min(change_profit)

#using the index, 
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      

output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")
    
    
# Just another practice     
#Your task is to create a Python script that analyzes the records to calculate each of the following:
	
#initializing the variables 

#The total number of months included in the dataset
#total_months = 0
#The net total amount of "Profit/Losses" over the entire period
#total_revenue =0
#The average of the changes in "Profit/Losses" over the entire period
#changes =[]
#The greatest increase in profits (date and amount) over the entire period

#date_count = []
#greatest_inc = 0
#greatest_inc_month = 0
#greatest_dec = 0
#greatest_dec_month = 0

# calculating the total number of months and total revenue
 
#previous_profit = int(row[1])
#total_months = total_months + 1
#total_revenue = total_revenue + int(row[1])
#greatest_inc = int(row[1])
#greatest_inc_month = row[0]
    
# calculating the total number of months and total revenue



   