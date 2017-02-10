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
VL=[]
VL1=[]
V2L =[]
V2L1=[]
V3L1=[]
V3L=[]
V4L=[]
V4L1=[]
V5L1=[]
V5L =[]



for row in reader:
    if row['grade']=="A+" or row['grade']=="A":
        if float(row['adjpoll_clinton']) > float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) > float(row['rawpoll_trump']):
            VL.append([1.00,0.00])
            VL1.append(1.00)
        elif float(row['adjpoll_clinton']) < float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) < float(row['rawpoll_trump']):
            VL.append([0.00, 1.00])
            VL1.append(0.00)




x1= array(VL)
z1= array(VL1)
y1 = z1.flat

model1 = GaussianNB()
model1.fit(x1,y1)

predicted1 = model1.predict([[0,0],[0,1],[1,1],[1,0]])
print "Cross Validation Model M1 1"
print " If more the number of 1, the clinton will win"
print predicted1
print "The accuracy score is"
print accuracy_score([0,0,0,0],predicted1)
print "Jacard similarity with truth data is"
print jaccard_similarity_score([0,0,0,0],predicted1)
print "The mean error is:"
print stats.sem(VL, axis=None, ddof=0)