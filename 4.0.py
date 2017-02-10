from sklearn.naive_bayes import GaussianNB
import numpy as np

#assigning predictor and target variables
import csv

reader = csv.DictReader(open('presidential_polls.csv', 'rU'))
myList =[]
myList1=[]
for row in reader:
    if float(row['adjpoll_clinton']) > float(row['adjpoll_trump']):
        myList.append([1,0])
        myList1.append([1])
    else:
        myList.append([0,1])
        myList1.append([0])

print myList
print myList1

model = GaussianNB()
model.fit(myList,myList1)
predicted = model.predict([[1,0],[0,1]])
print predicted


