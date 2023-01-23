from cmath import isclose
import csv
import random
from tkinter import Menu
import numpy as np

file=open('House Price.csv')
type(file)
csvreader=csv.reader(file)
rows=[]
for row in csvreader:
    rows.append(row)
    
    
dataSet_size=506
coloumn_no=12
dataSet=[[0 for i in range(coloumn_no)] for j in range(dataSet_size)]


for ele in range(0,len(rows)):
    for i in range(0,len(rows[ele])):
        dataSet[ele][i]=float(rows[ele][i])
        

np.random.shuffle(dataSet);
trainingSet_size=355
testSet_size=151
trainingSet=[]
testSet=[]
for ele in range(0,len(dataSet)):
    if(ele<trainingSet_size):
        trainingSet.append(dataSet[ele])
    else:
        testSet.append(dataSet[ele])
    
    
Y=[]
for ele in trainingSet:
    Y.append(ele[11])
    
Y=np.vstack(Y);


Z=[]
for ele in trainingSet:
    x=[1]
    for i in range(0,11):
        x.append(ele[i])
    Z.append(x)

Z=np.vstack(Z);
print(Z)
eta=1e-8


def newTheta(theta,eta):
    a=Z.transpose()
    b=np.dot(Z,theta)
    c=np.subtract(b,Y)
    d=np.dot(a,c)
    d=2*eta*d;
    return np.subtract(theta,d)

def jGradient(theta):
    b=np.dot(Z,theta)
    c=np.subtract(b,Y)
    d=np.dot(c.transpose(),c)
    return d[0][0]
    
theta=np.vstack([[0.045],[0.045],[0.045],[0.045],[0.045],[0.045],[0.045],[0.045],[0.045],[0.045],[0.045],[0.045]])
min_j=jGradient(theta)
desired_theta=theta
for i in range(100):
    if(i<7):
        eta=1e-6
    else:
        eta=1e-8
    theta=newTheta(theta,eta)
    if(jGradient(theta)<min_j):
        min_j=jGradient(theta)
        desired_theta=theta
        
theta=desired_theta
print("The Coefficients of the Optimized model :")
print(theta)

def calculatePredictedValue(data):
    sum=theta[0][0];
    for i in range(len(data)-1):
        sum=sum+data[i]*theta[i+1][0]
    return sum


meanSquareError=0;
mean=0;
yPredictedArray=[]
for ele in testSet:
    yPredicted=calculatePredictedValue(ele);
    yPredictedArray.append(yPredicted)
    mean=mean+calculatePredictedValue(ele);
    yActual=ele[11];
    mean=mean+yActual
    # print(yActual-yPredicted)
    diffSquare=(yActual-yPredicted)**2
    meanSquareError=meanSquareError+diffSquare

mean=mean/len(testSet)
SSres=meanSquareError
SStotal=0;
for ele in yPredictedArray:
    SStotal=SStotal+(ele-mean)**2

print("SSE: ",meanSquareError)

meanSquareError=meanSquareError/len(testSet)
print("Mean Square Error:",meanSquareError)

R2Score=1-(SSres/SStotal)
print("R2 score: ",R2Score)

