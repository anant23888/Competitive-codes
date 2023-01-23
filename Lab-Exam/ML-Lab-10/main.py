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

arr = np.arange(60., 300.)
rad_arr = np.radians(arr)
k = np.random.normal(0, 0.15, len(rad_arr))
y = []
for i in range(len(rad_arr)):
    y1 = np.sin(rad_arr[i])+k[i]
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
print(theta)
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
Y3=[]
Z3=[]
ax1 = plt.subplots(222) 
plt.scatter(rad_arr_nl,y,color="red")
for j in range(3, 16, 3):
 eta_new=1e-4
 if(j==15):
    eta_new=1e-8
 if(j==6):
    eta=1e-6
 if(j==9):
    eta_new=1e-5 
 if(j==12):
    eta_new=1e-6   
 kp=0   
 Z1 = []    
 for i in range(len(rad_arr)):
    x=[]
    x.append(1)
    for k in range(j):
     x.append(rad_arr_nl[i]**(k+1)) 
    Z1.append(x)   
 theta1 = [[0.0]]
 for k in range(j):
    theta1.append([0.0])
 Z1 = np.vstack(Z1)
 for p in range(100):
    theta1 = newtheta(theta1, eta_new, Y, Z1)
    f = jGradient(theta1, Z1, Y)
    det=0
    for k in range(j):
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
 print("Squared Error for degree ",j,":",sse)
 
 ax1.plot(rad_arr_nl, Y2, color=color1[kp])
#  ax1.xaxis.zoom(3)
 kp+=1
plt.show()
Lasso=[]
Ridge=[]
y=np.vstack(y)
jt=jtheta(Y3,y)
print(jt)
thetak=np.transpose(theta_use)
lambda1=[1e-10,1e-8,1e-4,1e-2,1,10,20]
for ele in lambda1:
    k2=theta_use**2
    # k3=np.abs(theta_use)
    # k1=np.add(jt,theta_use)
    # k4=np.add(jt,k3)
    # Lasso.append(k4)
    # Ridge.append(k3)
    Yk1=np.dot(Z3,jt)
    Yk2=np.dot(Z3,jt)
    plt.plot(rad_arr_nl,Yk1,color="red")
    plt.plot(rad_arr_nl,Yk2,colr="orange")
plt.show()
