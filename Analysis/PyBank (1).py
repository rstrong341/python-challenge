#!/usr/bin/env python
# coding: utf-8

# In[56]:


import os
import csv

PyBank_csv = os.path.join("budget_data.csv")
PyBank_csv_output = os.path.join("budget_analysis.txt")


# In[22]:


#Set up variables and lists
Total_Net = []
greatest_increase = ["", 0]
greatest_decrease = ["",9999999999]
dif_list = []
Month = []

#Open file with csv_reader
with open(PyBank_csv) as data:
    csv_reader = csv.reader(data)
    
    #Skip over and store header
    header = next(csv_reader)
    
    #Create Variable for skipping the first row.  
    Previous = next(csv_reader)
    Previous_Profit = int(Previous[1])
    
    #Create for loop
    for row in csv_reader:
        
        #Subtract the Column we mad without the first row from the original column
        net_change = int(row[1]) - Previous_Profit          
        Previous_Profit = int(row[1])
     
        #Create list to keep track of net change
        dif_list = dif_list + [net_change]
        #Create Variable for Months that correspond with net change
        Month = Month + [row[0]]

        #If profit/loss column is greater than 0, output the corresponding month and the net change
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        #If profit/loss column is less than 9999999999, output the corresponding month and the net change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change        


# In[23]:


#Create a list for the profit/loss column
Total_Net = []

with open(PyBank_csv) as data:
    csv_reader = csv.reader(data)
    header = next(csv_reader)
    
    for row in csv_reader:
        
        #Add profit/loss column to a list
        Profits = (int(row[1]))
        Total_Net.append(Profits)
#Add up the sum of the list        
Total = sum(Total_Net)


# In[24]:


#Create list to find the average change of months
diff_list = [] 

#use zip method to make two columns, one that skips the first row and one that does not.  Then subtract the variables use to represent the rows.
for x, y in zip(Total_Net[0:], Total_Net[1:]): 
    diff_list.append(y-x) 

#Divide the total by the length
AVG_Change = sum(diff_list) / len(diff_list)


# In[25]:


#Formating to remove brackets and quotes
reformated_decrease =  (''.join(greatest_decrease[0])) 
reformated_decrease_2 = greatest_decrease[1]

reformated_increase =  (''.join(greatest_increase[0])) 
reformated_increase_2 = greatest_increase[1]

#Formating to chose decimal points
avg_change = round(AVG_Change, 2)


# In[26]:


Total_months = len(Total_Net)


# In[19]:


print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(Total_months))
print("Total: $" + str(Total))
print("Average Change: $" + str(avg_change))
print("Greatest Increase In Profits: " + reformated_increase + " ($" + str(reformated_increase_2) + ")")
print("Greatest Decrease In Profits: " + reformated_decrease + " ($" + str(reformated_decrease_2) + ")")


# In[53]:


output = (
f"\nFinancial Analysis\n"
f"---------------------------------------------"
f"\nTotal Months: {Total_months}"
f"\nTotal: ${Total}"
f"\nAverage Change: ${avg_change} "
f"\nGreatest Increase in Profits: {reformated_increase} (${reformated_increase_2})"
f"\nGreatest Decrease in Profits: {reformated_decrease} (${reformated_decrease_2})"
)
print(output)


# In[57]:


with open(PyBank_csv_output, "w") as txt_file:
    txt_file.write(output)

