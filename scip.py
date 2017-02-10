from scipy import stats

from sklearn.naive_bayes import GaussianNB
import numpy as np
from scipy import stats
from sklearn.metrics import jaccard_similarity_score
from numpy import array
from sklearn.metrics import accuracy_score
#assigning predictor and target variables
import csv

reader = csv.DictReader(open('presidential_polls.csv', 'rU'))
myList =[]
myList1=[]
myList2=[]
for row in reader:
    if float(row['adjpoll_clinton']) > float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) > float(row['rawpoll_trump']):
        myList.append([1.00,0.00])
        myList1.append(1.00)
    elif float(row['adjpoll_clinton']) < float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) < float(row['rawpoll_trump']):
        myList.append([0.00, 1.00])
        myList1.append(0.00)
reader0 = csv.DictReader(open('presidential_polls.csv', 'rU'))
clinton99=0.00
trump99=0.00
for row in reader0:
    adjusted_clinton = float(row['poll_wt']) * float(row['adjpoll_clinton'])
    adjusted_trump = float(row['poll_wt']) * float(row['adjpoll_trump'])
    clinton99 = clinton99 + adjusted_clinton
    trump99 = trump99 + adjusted_trump
    a= clinton99/trump99
    if a>1:
        myList2.append(1)
    else:
        myList2.append(0)

z_stat, p_val = stats.ranksums(myList1, myList2)

print "Significance level and z-statistic values respectively =", p_val, z_stat