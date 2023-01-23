import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
from sklearn.svm import SVC
f=open("Data_SVM.csv")
type(f)
csvreader=csv.reader(f)
rows=[]
for row in csvreader:
    k=[]
    for j in row:
        k.append(float(j))
    rows.append(k)
x1=[]
y1=[]
z1=[]
x2=[]
y2=[]
z2=[]
xtrain=[]
ytrain=[]
for row in rows:
    k=[]
    if(row[2]==-1.0):
     x1.append(row[0])
     y1.append(row[1])
     z1.append(row[2])
    if(row[2]==1.0):
     x2.append(row[0])
     y2.append(row[1])
     z2.append(row[2])
    k.append(row[0])
    k.append(row[1])
    xtrain.append(k)
    ytrain.append(row[2])  

fig = plt.figure()
ax = plt.axes()
 
ax.scatter(x1, y1,color = "red",label='class -1')
ax.scatter(x2, y2,color = "blue",label='class 1')

plt.title("simple 2D scatter plot")
xtrain=np.vstack(xtrain)
# ytrain=np.vstack(ytrain)
print(xtrain)
print(ytrain)
svc_model = SVC(kernel='linear', random_state=32)
svc_model.fit(xtrain, ytrain)
w=svc_model.coef_[0]
b = svc_model.intercept_[0]      
x_points = np.linspace(-1, 20)    
y_points = -(w[0] / w[1]) * x_points - b / w[1]
plt.plot(x_points, y_points, c='r',label='SVM Line or Decision Boundary')
wtop = svc_model.coef_[0] / (np.sqrt(np.sum(svc_model.coef_[0] ** 2)))
margin = 1 / np.sqrt(np.sum(svc_model.coef_[0] ** 2))
decisionboundary = np.array(list(zip(x_points, y_points)))
pointsabove = decisionboundary + wtop * margin
pointsbelow = decisionboundary- wtop * margin
plt.plot(pointsabove[:, 0], pointsabove[:, 1], 'b--', linewidth=1.5,label='support-vector')

plt.plot(pointsbelow[:, 0], pointsbelow[:, 1], 'g--',linewidth=1.5,label='support-vector')   
check=[[8,15],[7,4]]
for row in check:
    l="test-point " + str(row)
    plt.scatter(row[0],row[1],color='magenta',label=l)
    k=-(w[0] / w[1]) * row[0] - b / w[1]
    k1=row[1]-k
    print(k1)
    if(k1>0):
        print("class of ",row," is",-1)
    if(k1<0):
        print("class of ",row," is",1) 
plt.legend()
plt.show()      