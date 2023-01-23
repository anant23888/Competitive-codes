from array import array
import numpy as np
def calculate(m,theta,x,y):
    theta1=[]
    lst=[]
    for k in range(len(x)):
        sum=0
        v1=np.multiply(theta,x)
        v2=-np.subtract(y,v1)
        v4=np.multiply(v2,2)
        lst.append(v4)
        theta1.append(lst)
        lst=[]
    return theta1     

def calculate(data):
    sum=theta[0][0]
    for i in range(len(data)-1):
        k=data[i]*theta[i+1][0]
        sum=sum+k
    return sum

def splitdata(a):
    trainsize=int(len(a)*0.7)
    testsize=int(len(a)*0.3)+1
    training_data=[]
    test_data=[]
    i=0
    j=0
    while i<trainsize:
        training_data.append(a[i])
        i+=1
    while j<testsize:
        test_data.append(a[i])
        i+=1
        j+=1
    return [training_data,test_data]

def newtheta(theta,eta,m):
    a=m.transpose()
    b=np.dot(m,theta)
    c=np.subtract(b,m)
    d=np.dot(a,c)
    d=2*eta*d
    return np.subtract(theta,d)

def jGradient(theta,m1,m):
    b=np.dot(m,theta)
    c=np.subtract(b,m1)
    d=np.dot(c.transpose(),c)
    return d[0][0]

f=open(r"House Price.csv",'r')
content1=f.read().split()
content=[eval(i) for i in content1]
arr=[]
rows,col=(506,12)
for i in range(rows):
   a=[]
   for j in range(col):
     a.append(content[col*i+j])
   arr.append(a) 
training_data,test_data=splitdata(arr)
for i in range(len(training_data)):
    training_data[i].insert(0,1)
print(len(test_data))
m=[]
for i in range(len(training_data)):
    x=[1]
    for j in range(11):
        x.append(training_data[i][j])
    m.append(x)
x=np.vstack(m)
m1=[]
for i in range(len(training_data)):
    m1.append(training_data[i][11])
m1=np.vstack(m1)    
theta=[]
m=np.array(m)
m1=np.array(m1)

eta=1e-6
theta=np.vstack([[0.05],[0.05],[0.05],[0.05],[0.05],[0.041],[0.045],[0.045],[0.045],[0.045],[0.045],[0.05]])
min_j=jGradient(theta,m1,m)
optheta=theta
for i in range(100):
    if(i<20):
        eta=1e-6
    else:
        eta=1e-8
    theta=newtheta(theta,eta,m)
    if(jGradient(theta,m1,m)<min_j):
        min_j=jGradient(theta)
        optheta=theta
theta=optheta
print("Coefficient  of the Optimized model is",optheta)
meanSquareError=0
mean=0
yPredictedArray=[]
for ele in test_data:
    yPredicted=calculate(ele)
    yPredictedArray.append(yPredicted)
    mean=mean+calculate(ele)
    yActual=ele[11]
    mean=mean+yActual
    diffSquare=(yActual-yPredicted)**2
    meanSquareError=meanSquareError+diffSquare

mean=mean/len(test_data)
SSres=meanSquareError
SStotal=0
for ele in yPredictedArray:
    SStotal=SStotal+(ele-mean)**2

print("SSE is: ",meanSquareError)

meanSquareError=meanSquareError/len(test_data)
print("Mean Square Error is:",meanSquareError)

r2=1-SSres/SStotal
print("R2 error is:",r2)