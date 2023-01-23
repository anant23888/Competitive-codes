from math import exp, pi, sqrt
import math
import numpy as np
import matplotlib.pyplot as plt
# from numpy import random
def knn(training_data,x):
    c=0
    l=len(training_data)
    p=[training_data[0][0],training_data[0][1]]
    q=[x[0],x[1]]
    k1=training_data[0][2]
    k=math.dist(p,q)
    for i in range(l):
      p=[training_data[i][0],training_data[i][1]]
      q=[x[0],x[1]]
      p1=math.dist(p,q)
      if p1<k:
         k=p1
         k1=training_data[i][2]
    return k1  

def bayes(test_data):
    a1=np.array([test_data[0],test_data[1]])
    p1=np.array([0,0])
    p2=np.array([0,2])
    p3=np.subtract(a1,p1)
    p4=p3.transpose()
    p5=np.subtract(a1,p2)
    p6=p5.transpose()
    res1=np.dot(p3,p4)
    res2=np.dot(p5,p6)
    x=math.exp(-0.5*res1)
    y=math.exp(-0.5*res2)
    if(x>y):
        return 0
    else:
       return 1   

def splitarr(arr,k):
    length = int(len(arr)/k) 
    folds = []
    for i in range(k-1):
      folds += [arr[i*length:(i+1)*length]]
    folds += [arr[(k-1)*length:len(arr)]] 
    return folds 
meanclass1=[0,0]
meanclass2=[0,2]
covarianceclass1=[[1,0],[0,1]]
covarianceclass2=[[1,0],[0,1]]
x = np.random.multivariate_normal(meanclass1,covarianceclass1,100)
y=np.random.multivariate_normal(meanclass2,covarianceclass2,100)
x1=[]
x2=[]
for i in range(len(x)):
    a=list(x[i]) 
    a.append(0)
    x1.append(a)
for i in range(len(y)):
    a=list(y[i])
    a.append(1)
    x2.append(a)

np.random.shuffle(x1)
np.random.shuffle(x2)
datasettest=[]

for i in range(0,50):
    datasettest.append(x1[i])
    datasettest.append(x2[i])
leng=len(datasettest)    
bias_arr=[]
variance_arr=[]
for k in range(100,1001,100):
 x3=np.random.multivariate_normal(meanclass1,covarianceclass1,k)
 y1=np.random.multivariate_normal(meanclass2,covarianceclass2,k)
 x1=[]
 x2=[]
 for i in range(len(x3)):
    a=list(x3[i])
    a.append(0)
    x1.append(a)
 for i in range(len(y1)):
    a=list(y1[i])
    a.append(1)
    x2.append(a)

 np.random.shuffle(x1)
 np.random.shuffle(x2)
 datasettrain=[]
 for i in range(0,int(k/2)):
    datasettrain.append(x1[i])
    datasettrain.append(x2[i])
 np.random.shuffle(datasettrain)
 bias=0
 gp=0
 l=len(datasettrain)
 class1=0.5
 class2=0.5

 for j in range(len(datasettest)):
    splitdata=splitarr(datasettrain,10)
    arr=[]
    for ele in splitdata:
        arr.append(knn(ele,datasettrain[j]))
    c1=0
    c2=0    
    for ele in arr:
        if(ele==0):
          c1+=1
        else:
          c2+=1
    if(c1>c2):
        y=0
    else:
        y=1

    yst=bayes(datasettest[j])

    if(y!=yst):
        bias+=1
    sum=0
    for ele in arr:
        if(ele!=y):
            sum+=1
    variance=sum/10
 bias_arr.append(bias/leng)
 variance_arr.append(variance/leng)
n=[100,200,300,400,500,600,700,800,900,1000]
print(bias_arr)
print(variance_arr)
plt.plot(n,bias_arr)
plt.plot(n,variance_arr)
plt.show()

