from cmath import sin
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
def newtheta(theta, eta, m1, m):
    a = m.transpose()
    b = np.dot(m, theta)
    c = np.subtract(b, m1)
    d = np.dot(a, c)
    d = 2*eta*d
    return np.subtract(theta, d)

def jGradient(theta, Z, Y):
    a = np.transpose(Z)
    b = np.dot(a, Z)
    c = np.dot(a, Y)
    d = np.dot(b, theta)
    gradient = 2*d-2*c
    return gradient

def jtheta(Z,Y):
    b=np.subtract(Z,Y)
    d=b**2
    return d

arr = np.arange(60., 360.)
rad_arr = np.radians(arr)
k = np.random.normal(0.5, 0.15, len(rad_arr))
y = []
for i in range(len(rad_arr)):
    y1 = np.sin(rad_arr[i])+np.cos(rad_arr[i])+k[i]*k[i]
    y.append(y1)
# np.random.shuffle(y)
theta = np.vstack([[0.0], [0.0]])
eta = 1e-4
Y = []
Z = []
i = 0
for i in range(len(rad_arr)):
    x = [1, rad_arr[i]]
    Y.append(y[i])
    Z.append(x)
Y = np.vstack(Y)
Z = np.vstack(Z)
for j in range(5000):
    theta = newtheta(theta, eta, Y, Z)
    f = jGradient(theta, Z, Y)
    det = f[0]-f[1]
    det = abs(det)
    if(det < 0.01):
        break
print("Value of optimised Theta is",theta)
color1=[]
color1.append("green")
color1.append("blue")
color1.append("orange")
color1.append("violet")
color1.append("yellow")

Y = []
for i in range(len(rad_arr)):
    y1 = theta[0]+theta[1]*rad_arr[i]
    Y.append(y1)
plt.scatter(rad_arr,y,color="red")
plt.plot(rad_arr, Y, color="green")
plt.show()
mean_nl = np.mean(rad_arr)
standard_nl = np.std(rad_arr)
rad_arr_nl = (rad_arr-mean_nl)/standard_nl
theta_use=[]
error=0
sse=0
for i in range(len(rad_arr)):
    sse=sse+(Y[i]-rad_arr[i])**2
print("SSE is :",sse)
Y3=[]
Z3=[]
 
plt.scatter(rad_arr_nl,y,color="red")

#for non-linear regresion (1)
eta_new1=1e-4
kp=0
Z1=[]
for i in range(len(rad_arr)):
    x=[]
    x.append(1)
    for k in range(1):
     x.append(rad_arr_nl[i]**(k+1)) 
    Z1.append(x)   
theta1 = [[0.0]]
for k in range(1):
    theta1.append([0.0])
Z1 = np.vstack(Z1)
for p in range(1000):
    theta1 = newtheta(theta1, eta_new1, Y, Z1)
    f = jGradient(theta1, Z1, Y)
    det=0
    for k in range(1):
      if(k%2!=0):
        det-=f[k]
      else:
        det+=f[k]  
    det = abs(det)
    if(det < 0.01):
        break
print(theta1)
Y2 = np.dot(Z1,theta1)
sse=0
for l in range(len(rad_arr_nl)):
    sse=sse+(Y2[l]-y[l])**2
if(j==15):
    theta_use=theta
    error=sse  
    Y3=Y2 
    Z3=Z1
Yp=[]   
print("Squared Error for degree ",1,":",sse)
 
plt.plot(rad_arr_nl, Y2, color='green')

plt.show()


plt.scatter(rad_arr_nl,y,color="red")
# for non-linear regression (3)
eta_new1=1e-4
kp=0
Z1=[]
for i in range(len(rad_arr)):
    x=[]
    x.append(1)
    for k in range(3):
     x.append(rad_arr_nl[i]**(k+1)) 
    Z1.append(x)   
theta1 = [[0.0]]
for k in range(3):
    theta1.append([0.0])
Z1 = np.vstack(Z1)
for p in range(1000):
    theta1 = newtheta(theta1, eta_new1, Y, Z1)
    f = jGradient(theta1, Z1, Y)
    det=0
    for k in range(3):
      if(k%2!=0):
        det-=f[k]
      else:
        det+=f[k]  
    det = abs(det)
    if(det < 0.01):
        break
print(theta1)
Y2 = np.dot(Z1,theta1)
sse=0
for l in range(len(rad_arr_nl)):
    sse=sse+(Y2[l]-y[l])**2
if(j==15):
    theta_use=theta
    error=sse  
    Y3=Y2 
    Z3=Z1
Yp=[]   
#  for ele in Y2:   
#     if(ele>1):
#       ele=1
#     Yp.append(ele)  
print("Squared Error for degree ",3,":",sse)
 
plt.plot(rad_arr_nl, Y2, color='green')

plt.show()

#for non-linear regression (13)
plt.scatter(rad_arr_nl,y,color="red")
eta_new1=1e-8
kp=0
Z1=[]
for i in range(len(rad_arr)):
    x=[]
    x.append(1)
    for k in range(13):
     x.append(rad_arr_nl[i]**(k+1)) 
    Z1.append(x)   
theta1 = [[0.0]]
for k in range(13):
    theta1.append([0.0])
Z1 = np.vstack(Z1)
for p in range(1000):
    theta1 = newtheta(theta1, eta_new1, Y, Z1)
    f = jGradient(theta1, Z1, Y)
    det=0
    for k in range(13):
      if(k%2!=0):
        det-=f[k]
      else:
        det+=f[k]  
    det = abs(det)
    if(det < 0.01):
        break
print(theta1)
Y2 = np.dot(Z1,theta1)
sse=0
for l in range(len(rad_arr_nl)):
    sse=sse+(Y2[l]-y[l])**2
if(j==15):
    theta_use=theta
    error=sse  
    Y3=Y2 
    Z3=Z1
Yp=[]   
  
print("Squared Error for degree ",13,":",sse)
 
plt.plot(rad_arr_nl, Y2, color='green')

plt.show()

#for non-linear regression (15)
plt.scatter(rad_arr_nl,y,color="red")
eta_new1=1e-8
kp=0
Z1=[]
for i in range(len(rad_arr)):
    x=[]
    x.append(1)
    for k in range(15):
     x.append(rad_arr_nl[i]**(k+1)) 
    Z1.append(x)   
theta1 = [[0.0]]
for k in range(15):
    theta1.append([0.0])
Z1 = np.vstack(Z1)
Zk=Z1
for p in range(100):
    theta1 = newtheta(theta1, eta_new1, Y, Z1)
    f = jGradient(theta1, Z1, Y)
    det=0
    for k in range(15):
      if(k%2!=0):
        det-=f[k]
      else:
        det+=f[k]  
    det = abs(det)
    if(det < 0.01):
        break
print(theta1)
ps1=theta1
Y2 = np.dot(Z1,theta1)
sse=0
for l in range(len(rad_arr_nl)):
    sse=sse+(Y2[l]-y[l])**2
if(j==15):
    theta_use=theta
    error=sse  
    Y3=Y2 
    Z3=Z1
Yp=[]   
  
print("Squared Error for degree ",15,":",sse)
 
plt.plot(rad_arr_nl, Y2, color='green')

plt.show()
#for non-linear regression (19)
plt.scatter(rad_arr_nl,y,color="red")
eta_new1=1e-13
kp=0
Z1=[]
for i in range(len(rad_arr)):
    x=[]
    x.append(1)
    for k in range(19):
     x.append(rad_arr_nl[i]**(k+1)) 
    Z1.append(x)   
theta1 = [[0.0]]
for k in range(19):
    theta1.append([0.0])
Z1 = np.vstack(Z1)
for p in range(500):
    theta1 = newtheta(theta1, eta_new1, Y, Z1)
    f = jGradient(theta1, Z1, Y)
    det=0
    for k in range(19):
      if(k%2!=0):
        det-=f[k]
      else:
        det+=f[k]  
    det = abs(det)
    if(det < 0.01):
        break
print(theta1)
ps2=theta1
Y2 = np.dot(Z1,theta1)
print("Prediction Test Set: ",Y2)
sse=0
for l in range(len(rad_arr_nl)):
    sse=sse+(Y2[l]-y[l])**2
if(j==15):
    theta_use=theta
    error=sse  
    Y3=Y2 
    Z3=Z1
Yp=[]   
  
print("Squared Error for degree ",19,":",sse)
 
plt.plot(rad_arr_nl, Y2, color='green')

plt.show()



Lasso=[]
Ridge=[]
# y=np.vstack(y)
# jt=jtheta(Y3,y)
# print(jt)
# thetak=np.transpose(theta_use)
plt.scatter(rad_arr_nl,y,color="red")
lambda1=[1e-10,1e-5]
for i in range(len(lambda1)):
  thetagp=np.add(ps2,lambda1[i]*ps2)
  Yp=np.dot(Z1,thetagp)
  print("Test Prediction for 19th deg : ",Yp)
  if(i==0):
   plt.plot(rad_arr_nl, Yp, color='blue')
  if(i==1): 
    plt.plot(rad_arr_nl, Yp, color='green')
plt.show()  


plt.scatter(rad_arr_nl,y,color="red")
lambda1=[1e-10,1e-5]
for i in range(len(lambda1)):
  thetagp=np.add(ps1,lambda1[i]*ps1)
  Yp=np.dot(Zk,thetagp)
  print("Test Prediction for 15th deg : ",Yp)
  print("\n")
  if(i==0):
   plt.plot(rad_arr_nl, Yp, color='blue')
  if(i==1): 
    plt.plot(rad_arr_nl, Yp, color='green')
plt.show()  