import math
import numpy
from numpy import random
import matplotlib.pyplot as plt

mean_class1=[0,0]
cov_class1=[[1,0],[0,1]]

mean_class2=[0,2]
cov_class2=[[1,0],[0,1]]

def dataset_generator(mean,cov,size,classLabel):
    x= numpy.random.multivariate_normal(mean, cov, size)
    print(x)
    dataset_class=[]
    for i in range(0,len(x)):
        a=list(x[i])
        a.append(classLabel)
        dataset_class.append(a);
    return dataset_class
    
dataset_class1=dataset_generator(mean_class1,cov_class1,100,0)
print(dataset_class1)

dataset_class2=dataset_generator(mean_class2,cov_class2,100,1)



numpy.random.shuffle(dataset_class1)
numpy.random.shuffle(dataset_class2)
test_dataset=[]
for i in range(0,50):
    test_dataset.append(dataset_class1[i])
    test_dataset.append(dataset_class2[i])

p_class1=0.5
p_class2=0.5


    



def knn1(training,test_ele):
    knnArray=[]
    for i in range(0,len(training)):
        x1=abs(training[i][0]-test_ele[0])**2
        x2=abs(training[i][1]-test_ele[1])**2
        knnArray.append([(x1+x2)**(1/2),training[i][2]]);
    
    knnArray.sort(key=lambda y: y[0])
    return knnArray[0][1];

def bayes_theorem(test_ele):
    x_array=numpy.array([test_ele[0],test_ele[1]])
    mean_class1_array=numpy.array([0,0])
    mean_class2_array=numpy.array([0,2])
    a3=numpy.subtract(x_array,mean_class1_array)
    a4=a3.transpose();
    a5=numpy.subtract(x_array,mean_class2_array)
    a6=a5.transpose()
    res1=numpy.dot(a3,a4)
    res2=numpy.dot(a5,a6);
    p_class1_x=(math.exp(-0.5*res1))
    p_class2_x=(math.exp(-0.5*res2))
    if(p_class1_x>p_class2_x):
        return 0
    else:
        return 1
    
def array_split(arr, k):
    length = int(len(arr)/k) 
    folds = []
    for i in range(k-1):
        folds += [arr[i*length:(i+1)*length]]
    folds += [arr[(k-1)*length:len(arr)]]
    return folds

bias_array=[]
variance_array=[]
for k in range(100,1001,100):
    class1_dataset=dataset_generator(mean_class1,cov_class1,k,0)
    class2_dataset=dataset_generator(mean_class2,cov_class2,k,1)
    numpy.random.shuffle(class1_dataset)
    numpy.random.shuffle(class2_dataset)

    combined_dataset=[]

    for i in range(0,int(k/2)):
        combined_dataset.append(class1_dataset[i])
        combined_dataset.append(class2_dataset[i])

    numpy.random.shuffle(combined_dataset)
        
    bias=0;
    varience=0;
    for j in range(0,len(test_dataset)):
        ten_datasets=array_split(combined_dataset,10)

        y_array=[]
        for ele in ten_datasets:
            y_array.append(knn1(ele,test_dataset[j]));

        class1_count=0;
        class2_count=0;
        for ele in y_array:
            if(ele==0):
                class1_count+=1;
            else:
                class2_count+=1;

        if(class1_count>class2_count):
            ym=0;
        else:
            ym=1;

        yStar=bayes_theorem(test_dataset[j])
        
        if(ym!=yStar):
            bias+=1;

        varience_sum=0
        for ele in y_array:
            if(ele!=ym):
                varience_sum+=1;
        
        varience+=varience_sum/10;
        
    bias_array.append(bias/len(test_dataset))
    variance_array.append(varience/len(test_dataset))
    

print(bias_array)
print(variance_array)
n_array=[100,200,300,400,500,600,700,800,900,1000]
plt.plot(n_array,bias_array)
plt.plot(n_array,variance_array)
plt.show()