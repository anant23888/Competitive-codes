from cgi import test
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

def newtheta(theta,eta,m1,m):
    a=m.transpose()
    b=np.dot(m,theta)
    c=np.subtract(b,m1)
    d=np.dot(a,c)
    d=2*eta*d
    return np.subtract(theta,d)

def jGradient(theta,Z,Y):
    a=np.transpose(Z)
    b=np.dot(a,Z)
    c=np.dot(a,Y)
    d=np.dot(b,theta)
    gradient=2*d-2*c
    return gradient
# def jGradient(theta,Z,Y):
#     a=np.transpose(Y)
#     b=np.dot(a,Y)
#     c=np.dot(a,Z)
#     d=np.dot(b,theta)
#     gradient=2*d-2*c
#     return gradient

mean1=[0,0]
covariance1=[[1,0],[0,1]]
mean2=[4,5]
covariance2=[[1,0],[0,1]]
x1=np.random.multivariate_normal(mean1,covariance1,50)
x2=np.random.multivariate_normal(mean2,covariance2,50)
x_class1=[]
x_class2=[]
for ele in x1:
    v1=[-1,ele[0],ele[1]]
    x_class1.append(v1)

for ele in x2:
    v1=[1,ele[0],ele[1]]
    x_class2.append(v1)    

training_data=[]
for i in range(50):
    training_data.append(x_class1[i])
    training_data.append(x_class2[i])
np.random.shuffle(training_data)    
x3=np.random.multivariate_normal(mean1,covariance1,25)
x4=np.random.multivariate_normal(mean2,covariance2,25)
xt_class1=[]
xt_class2=[]

for ele in x3:
    v1=[-1,ele[0],ele[1]]
    xt_class1.append(v1)
for ele in x4:
    v1=[1,ele[0],ele[1]]
    xt_class2.append(v1)  
test_data=[]
for i in range(25):
    test_data.append(xt_class1[i])
    test_data.append(xt_class2[i])

np.random.shuffle(test_data)
theta=np.vstack([[0.0],[0.0],[0.0]])
eta=1e-4
Y=[]
Z=[]
i=0
for ele in training_data:
    x=[1,ele[1],ele[2]]
    Y.append(ele[0])     
    Z.append(x)  
Y=np.vstack(Y)
Z=np.vstack(Z)
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
for j in range(5000):
    theta=newtheta(theta,eta,Y,Z)
    f=jGradient(theta,Z,Y)
    det=f[0]-f[1]+f[2]
    det=abs(det)
    if(det<0.01):
        break
# print(theta)    
y1=[]
xk=[]
for i in range(len(training_data)):
    sum=-1*theta[0]
    sum=sum-theta[1]*training_data[i][1]
    xk.append(training_data[i][1])
    sum=sum/theta[2]
    y1.append(sum)   
plt.scatter(x1[:,0],x1[:,1],color="red")
plt.scatter(x2[:,0],x2[:,1],color="blue")
plt.plot(xk,y1,color="green")
plt.show()
error=0
for ele in test_data:
    sum=theta[0]+theta[1]*ele[1]+theta[2]*ele[2]
    print(sum)
    if(sum>0 and ele[0]==-1):
        error+=1
    elif (sum<0 and ele[0]==1) : 
      error+=1
error=error/len(test_data)
print("Error is...",error)        