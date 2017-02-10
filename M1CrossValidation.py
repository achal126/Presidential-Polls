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
    if float(row['adjpoll_clinton']) > float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) > float(row['rawpoll_trump']):
        myList.append([1.00,0.00])
        myList1.append(1.00)
    elif float(row['adjpoll_clinton']) < float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) < float(row['rawpoll_trump']):
        myList.append([0.00, 1.00])
        myList1.append(0.00)



x= array(myList)
z= array(myList1)

y = z.flat
print type(y)
print y
model = GaussianNB()
model.fit(x,y)
predicted = model.predict([[0,0],[0,1],[1,1],[1,0]])

print predicted

print accuracy_score([0,0,0,0],predicted)
print jaccard_similarity_score([0,0,0,0],predicted)
print "The mean error is:"
print stats.sem(myList, axis=None, ddof=0)

for row in reader:
    if row['grade']=="A+" or row['grade']=="A":

        if float(row['adjpoll_clinton']) > float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) > float(row['rawpoll_trump']):
            VL.append([1.00,0.00])
            VL1.append(1.00)
        elif float(row['adjpoll_clinton']) < float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) < float(row['rawpoll_trump']):
            VL.append([0.00, 1.00])
            VL1.append(0.00)


print VL
print VL1

x1= array(VL)
z1= array(VL1)
y1 = z1.flat

model1 = GaussianNB()
model1.fit(x,y)

predicted1 = model1.predict([[0,0],[0,1],[1,1],[1,0]])

print predicted1

print accuracy_score([0,0,0,0],predicted1)
print jaccard_similarity_score([0,0,0,0],predicted1)
print "The mean error is:"
print stats.sem(VL, axis=None, ddof=0)


for row in reader:
    if row['grade']=="A-" or row['grade']=="B+":

        if float(row['adjpoll_clinton']) > float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) > float(row['rawpoll_trump']):
            V2L.append([1.00,0.00])
            V2L1.append(1.00)
        elif float(row['adjpoll_clinton']) < float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) < float(row['rawpoll_trump']):
            V2L.append([0.00, 1.00])
            V2L1.append(0.00)




x2= array(V2L)
z2= array(V2L1)
y2 = z2.flat

model2 = GaussianNB()
model2.fit(x2,y2)
predicted2 = model2.predict([[0,0],[0,1],[1,1],[1,0]])

print predicted2

print accuracy_score([0,0,0,0],predicted2)
print jaccard_similarity_score([0,0,0,0],predicted2)
print "The mean error is:"
print stats.sem(V2L, axis=None, ddof=0)

for row in reader:
    if row['grade']=="B" or row['grade']=="B-":

        if float(row['adjpoll_clinton']) > float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) > float(row['rawpoll_trump']):
            V3L.append([1.00,0.00])
            V3L1.append(1.00)
        elif float(row['adjpoll_clinton']) < float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) < float(row['rawpoll_trump']):
            V3L.append([0.00, 1.00])
            V3L1.append(0.00)




x3= array(V3L)
z3= array(V3L1)
y3 = z3.flat

model3 = GaussianNB()
model3.fit(x3,y3)
predicted3 = model3.predict([[0,0],[0,1],[1,1],[1,0]])

print predicted3

print accuracy_score([0,0,0,0],predicted3)
print jaccard_similarity_score([0,0,0,0],predicted3)
print "The mean error is:"
print stats.sem(V3L, axis=None, ddof=0)

for row in reader:
    if row['grade']=="C+" or row['grade']=="C":

        if float(row['adjpoll_clinton']) > float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) > float(row['rawpoll_trump']):
            V4L.append([1.00,0.00])
            V4L1.append(1.00)
        elif float(row['adjpoll_clinton']) < float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) < float(row['rawpoll_trump']):
            V4L.append([0.00, 1.00])
            V4L1.append(0.00)




x4= array(V4L)
z4= array(V4L1)
y4 = z4.flat

model4 = GaussianNB()
model4.fit(x4,y4)
predicted4 = model4.predict([[0,0],[0,1],[1,1],[1,0]])

print predicted4

print accuracy_score([0,0,0,0],predicted4)
print jaccard_similarity_score([0,0,0,0],predicted4)
print "The mean error is:"
print stats.sem(V4L, axis=None, ddof=0)

for row in reader:
    if row['grade']=="C-" or row['grade']=="":

        if float(row['adjpoll_clinton']) > float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) > float(row['rawpoll_trump']):
            V5L.append([1.00,0.00])
            V5L1.append(1.00)
        elif float(row['adjpoll_clinton']) < float(row['adjpoll_trump']) and float(row['rawpoll_clinton']) < float(row['rawpoll_trump']):
            V5L.append([0.00, 1.00])
            V5L1.append(0.00)




x5= array(V5L)
z5= array(V5L1)
y5 = z5.flat

model5 = GaussianNB()
model5.fit(x5,y5)
predicted5 = model5.predict([[0,0],[0,1],[1,1],[1,0]])

print predicted5

print accuracy_score([0,0,0,0],predicted5)
print jaccard_similarity_score([0,0,0,0],predicted5)
print "The mean error is:"
print stats.sem(V5L, axis=None, ddof=0)