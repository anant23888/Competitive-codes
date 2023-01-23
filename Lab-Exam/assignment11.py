import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.svm import SVC

file=open('Data_SVM.csv')
type(file)
csvreader=csv.reader(file)
rows=[]
for row in csvreader:
    rows.append(row)
    
    
training=[[0 for i in range(3)] for j in range(20)]
x_train=[]
y_train=[]
for ele in range(0,20):
    for i in range(0,3):
        training[ele][i]=float(rows[ele][i])

class1_X1=[]
class1_X2=[]
class2_X1=[]
class2_X2=[]
for i in range(len(training)):
    if(training[i][2]==1.0):
        class1_X1.append(training[i][0])
        class1_X2.append(training[i][1])
        
    else:
        class2_X1.append(training[i][0])
        class2_X2.append(training[i][1])
    
    arr=[]
    arr.append(training[i][0])
    arr.append(training[i][1])
    x_train.append(arr)
    y_train.append(training[i][2])
    
        
        
        
plt.scatter(class1_X1,class1_X2,color="red")
plt.scatter(class2_X1,class2_X2,color="blue")

X_train=np.vstack(x_train)

svc_model = SVC(kernel='linear', random_state=32)
svc_model.fit(X_train, y_train)

w = svc_model.coef_[0]     


b = svc_model.intercept_[0]      
x_points = np.linspace(-1, 20)    
y_points = -(w[0] / w[1]) * x_points - b / w[1]  

bounday_margin = 1 / np.sqrt(np.sum(svc_model.coef_[0] ** 2))

w_dis = svc_model.coef_[0] / (np.sqrt(np.sum(svc_model.coef_[0] ** 2)))
boundary_points = np.array(list(zip(x_points, y_points)))
points_of_line_left = boundary_points + w_dis * bounday_margin
points_of_line_right = boundary_points - w_dis * bounday_margin
plt.plot(x_points, y_points, c='green');
plt.plot(points_of_line_left[:, 0], 
         points_of_line_left[:, 1], 
         'y--', 
         linewidth=2)
plt.plot(points_of_line_right[:, 0], 
         points_of_line_right[:, 1], 
         'y--',
         linewidth=2)

x_test=[[8,15],[7,4]]
x_test=np.vstack(x_test)

for i in range(0,len(x_test)):
    line_value=x_test[i][1]+(w[0]/w[1])*x_test[i][0]+b/w[1]
    print("value of",x_test[i]," : ",line_value)
    if(line_value>0):
        print(x_test[i]," class is: ",-1)
    else:
        print(x_test[i]," class is: ",1)   
        
    if(i==0):
        plt.scatter(x_test[i][0],x_test[i][1],color="cyan")
    else:
        plt.scatter(x_test[i][0],x_test[i][1],color="purple")
        
    print() 
            
plt.legend(["class 1","class -1","SVM line","support margin","support margin","[8,15]","[7,4]"])
plt.show()