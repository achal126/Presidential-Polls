import csv
import matplotlib.pyplot as plt
import operator
from datetime import datetime
from sklearn.metrics import jaccard_similarity_score
from numpy import array
from sklearn.metrics import accuracy_score


clinton =0.00
trump = 0.00
clinton99=0.0
trump99=0.0

reader0 = csv.DictReader(open('presidential_polls.csv', 'rU'))

for row in reader0:
    adjusted_clinton = float(row['poll_wt']) * float(row['rawpoll_clinton'])
    adjusted_trump = float(row['poll_wt']) * float(row['rawpoll_trump'])
    clinton99 = clinton99 + adjusted_clinton
    trump99 = trump99 + adjusted_trump
#print clinton99
#print trump99



reader = csv.DictReader(open('presidential_polls.csv', 'rU'))

reader = sorted(reader, key=lambda row: row['poll_id'], reverse=False)



for row in reader:
    if  row['type'] == "polls-plus" and (row['grade'] == "A+" or row['grade'] =="A" ):
        #print row['poll_id']
        #print row['adjpoll_clinton']
        adjusted_clinton = float(row['poll_wt']) * float(row['rawpoll_clinton'])
        adjusted_trump = float(row['poll_wt']) * float(row['rawpoll_trump'])
        clinton = clinton + adjusted_clinton
        trump = trump + adjusted_trump
#print clinton
#print trump

clinton1 = 0.00
trump1 = 0.00
for row in reader:
    if  row['type'] == "now-cast" and (row['grade'] == "A+" or row['grade'] =="A" ):
        #print row['poll_id']
        #print row['adjpoll_clinton']
        adjusted_clinton = float(row['poll_wt']) * float(row['rawpoll_clinton'])
        adjusted_trump = float(row['poll_wt']) * float(row['rawpoll_trump'])
        clinton1 = clinton1 + adjusted_clinton
        trump1 = trump1 + adjusted_trump
#print clinton1
#print trump1

clinton2 = 0.00
trump2 = 0.00
for row in reader:
    if  row['type'] == "polls-only" and (row['grade'] == "A+" or row['grade'] =="A" ):
        #print row['poll_id']
        #print row['adjpoll_clinton']
        adjusted_clinton = float(row['poll_wt']) * float(row['rawpoll_clinton'])
        adjusted_trump = float(row['poll_wt']) * float(row['rawpoll_trump'])
        clinton2 = clinton1 + adjusted_clinton
        trump2 = trump1 + adjusted_trump
#print clinton2
#print trump2



clinton11 = 0.00
trump11 = 0.00
for row in reader:
    if  row['type'] == "polls-plus" and (row['grade'] == "A+" or row['grade'] =="A" ):
        #print row['poll_id']
        #print row['rawpoll_clinton']
        raw_clinton = float(row['poll_wt']) * float(row['rawpoll_clinton'])
        raw_trump = float(row['poll_wt']) * float(row['rawpoll_trump'])
        clinton11 = clinton + raw_clinton
        trump11 = trump + raw_trump
#print clinton11
#print trump11

clinton12 = 0.00
trump12 = 0.00
for row in reader:
    if row['type'] == "now-cast" and (row['grade'] == "A+" or row['grade'] =="A" ):
        #print row['poll_id']
        #print row['rawpoll_clinton']
        raw_clinton = float(row['poll_wt']) * float(row['rawpoll_clinton'])
        raw_trump = float(row['poll_wt']) * float(row['rawpoll_trump'])
        clinton12 = clinton1 + raw_clinton
        trump12 = trump1 + raw_trump
#print clinton12
#print trump12

clinton13 = 0.00
trump13 = 0.00
for row in reader:
    if row['type'] == "polls-only" and (row['grade'] == "A+" or row['grade'] =="A" ):
        #print row['poll_id']
        #print row['rawpoll_clinton']
        raw_clinton = float(row['poll_wt']) * float(row['rawpoll_clinton'])
        raw_trump = float(row['poll_wt']) * float(row['rawpoll_trump'])
        clinton13 = clinton1 + raw_clinton
        trump13 = trump1 + raw_trump
#print clinton13
#print trump13

print "IF value is greater than 1 Clinton wins"
print "Model M2"
a1= clinton99/trump99
print a1
print "Accuracy score"
print a1 -1
print "Model M2 1"
a2= clinton/trump
print a2
print "Accuracy score"
print a2-1
print
print "Model M2 2"
a3 = clinton1/trump1
print a3
print "Accuracy score"
print a3-1
print "Model M2 3"
a4= clinton11/trump11
print a4
print "Accuracy score"
print a4-1

print "Model M2 4"
a5 = clinton12/trump12
print a5
print "Accuracy score"

print "Model M2 5"
a6 = clinton13/trump13
print a6
print "Accuracy score"
print a6 -1

