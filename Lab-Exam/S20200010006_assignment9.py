from random import gauss
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
class1_mean=[0,0]
class2_mean=[4,5]
class1_cov=[[1,0],[0,1]]
class2_cov=[[1,0],[0,1]]
def dataset_generator(mean,cov,size,classLabel):
    x= np.random.multivariate_normal(mean, cov, size)
    # print(x)
    dataset_class=[]
    for i in range(0,len(x)):
        a=list(x[i])
        a.append(classLabel)
        dataset_class.append(a);
    return x,dataset_class

x_Training_class1,training_class1=dataset_generator(class1_mean,class1_cov,50,1)
x_Training_class2,training_class2=dataset_generator(class2_mean,class2_cov,50,-1)
x_Test_class1,test_class1=dataset_generator(class1_mean,class1_cov,25,1)
x_Test_class2,test_class2=dataset_generator(class2_mean,class2_cov,25,-1)
# print(x_Training_class1)
training=[]
for i in range(50):
    training.append(training_class1[i])
    training.append(training_class2[i])

np.random.shuffle(training)

test=[]
for i in range(25):
    test.append(test_class1[i])
    test.append(test_class2[i])

np.random.shuffle(test)
# print(test)
# def linear_regression(Z,Y):
 
Z=[]
Y=[]
X=[]
for i in range(len(training)):
    x1=[]
    x1.append(1)
    X.append(training[i][0])
    x1.append(training[i][0])
    x1.append(training[i][1])   
    Z.append(x1)
    Y.append(training[i][2])
    

# print(training)
Y=np.vstack(Y)
Z=np.vstack(Z)
# print(Y)
def newTheta(theta,eta,Z,Y):
    a=np.transpose(Z)
    b=np.dot(Z,theta)
    c=np.subtract(b,Y)
    d=np.dot(a,c)
    d=2*eta*d;
    return np.subtract(theta,d)


theta=np.vstack([[0.0],[0.0],[0.0]]);

def gradientJ(theta,Z,Y):
    a=np.transpose(Z)
    b=np.dot(a,Z)
    c=np.dot(a,Y)
    d=np.dot(b,theta)
    gradient=2*d-2*c;
    return gradient;

eta=1e-4

for i in range(5000):
    # if(i<400):
    #     eta=1e-3
    theta=newTheta(theta=theta,eta=eta,Z=Z,Y=Y)
    f=gradientJ(theta=theta,Z=Z,Y=Y);
    det=f[0]-f[1]+f[2]
    det=abs(det)
    if(det<0.01):
        break;

# print(theta)
# print(X)
y=[]
for i in range(len(X)):
    sum=(-1)*theta[0]
    sum=sum-theta[1]*X[i]
    sum=sum/theta[2]
    y.append(sum)
    
# print(x_Training_class1)
plt.scatter(x_Training_class1[:,0],x_Training_class1[:,1],color="red")
plt.scatter(x_Training_class2[:,0],x_Training_class2[:,1],color="blue")
plt.plot(X,y,color="green")
plt.show()

# print(test)
def classifier(x1,x2):
    p=theta[0]+theta[1]*x1+theta[2]*x2;
    print(p)
    if(p<0):
        return -1
    else:
        return 1
        
error=0;
for i in range(len(test)):
    classifiedClass=classifier(test[i][0],test[i][1]);
    if(classifiedClass!=test[i][2]):
        error+=1

error=error/len(test);
print("Error: ",error)
    