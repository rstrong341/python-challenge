#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import Tools
import os
import csv
import collections
from collections import OrderedDict
import operator


# In[3]:


PyRoll_csv = os.path.join("election_data.csv")
PyRoll_csv_output = os.path.join("election_analysis.txt")


# In[4]:


#Create list for candidates
candidates_list = [] 

#Open CSV File
with open(PyRoll_csv) as data: 
    reader = csv.reader(data)
    
    #Skip the first row and store that row as "header"
    header = next(reader)
    
    #Create for loop
    for row in reader:
        
        #Create a varibale for the column we want and add it to the list we created
        name = row[2]
        candidates_list.append(name)

#Use Counter to count frequencies and place frequencies in a dictionary
ctr = collections.Counter(candidates_list)


# In[5]:


key_max = max(ctr.keys(), key=(lambda k: ctr[k]))
key_min = min(ctr.keys(), key=(lambda k: ctr[k]))

#Create Variable for winner name or value
winner_value = ctr[key_max]
winner_name = max(ctr.items(), key=operator.itemgetter(1))[0]


# In[6]:


#Create a list for the voters found in the Counter
Khan_Votes = ctr['Khan']
Correy_Votes = ctr['Correy']
Li_Votes = ctr['Li']
OTooley_Votes = ctr["O'Tooley"]

Voters_list = [Khan_Votes, Correy_Votes, Li_Votes, OTooley_Votes]

#Find the sum of the votes
Total_Votes = sum(Voters_list)

#Find the percentage of the votes each candidate received
Khan = Khan_Votes / sum(Voters_list)
Correy = Correy_Votes / sum(Voters_list)
Li = Li_Votes / sum(Voters_list)
OTooley = OTooley_Votes / sum(Voters_list)


# In[7]:


#Format the percentages
Khan_Percentage = "{:.3%}".format(Khan)
Correy_Percentage = "{:.3%}".format(Correy)
Li_Percentage = "{:.3%}".format(Li)
OTooley_Percentage = "{:.3%}".format(OTooley)


# In[8]:


print("Election Results")
print("-----------------------")
print("Total Votes: " + str(Total_Votes))
print("-----------------------")
print("Khan: " + str(Khan_Percentage) + "(" + str(Khan_Votes) + ")") 
print("Correy: " + str(Correy_Percentage) + "(" + str(Correy_Votes) + ")") 
print("Li: " + str(Li_Percentage) + "(" + str(Li_Votes) + ")") 
print("O'Tooley: " + str(OTooley_Percentage) + "(" + str(OTooley_Votes) + ")") 
print("-----------------------")
print("Winner: " + winner_name)
print("-----------------------")


# In[16]:


output = (
f"\nElection Results\n"
f"----------------------------"
f"\nTotal Votes: {Total_Votes}\n"
f"----------------------------"
f"\nKhan: {Khan_Percentage} ({Khan_Votes})\n"
f"Correy: {Correy_Percentage} ({Correy_Votes})\n"
f"Li: {Li_Percentage} ({Li_Votes})\n"
f"O'Tooley: {OTooley_Percentage} ({OTooley_Votes})\n"
f"----------------------------"
f"\nWinner: {winner_name} \n"
f"----------------------------"


)
print(output)


# In[18]:


with open(PyRoll_csv_output, "w") as txt_file:
    txt_file.write(output)

