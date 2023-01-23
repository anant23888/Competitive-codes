import csv
import math
import random

def KNN(training_data,test_data,k,p):
    
    accuracyCount=0
    for i in range(len(test_data)):
        arrNN=[]
        for j in range(len(training_data)):
            dis=distance(i,j,training_data,test_data,p)
            Dis=dis
            DisIndex=j
            pair=(Dis,DisIndex)
            arrNN.append(pair)
            
        arrNN.sort(key=lambda y: y[0])
        
        countClass=0
        for z in range(0,k):
            if(training_data[arrNN[z][1]][192]==test_data[i][192]):
                countClass=countClass+1; 
        
        
        if(countClass>=int(i/2+1)):
            accuracyCount=accuracyCount+1
        
    size=int(len(test_data))
    if(size!=0):
     accuracy=(accuracyCount/size)*100
     return accuracy


    
    

def distance(i,j,training_data,test_data,p):
    sum=0.0
    for k in range(0,192):
     sum=sum+(float(test_data[i][k])-float(training_data[j][k]))**2   
    return (sum)**(1./p)    



f=open(r"pp_tes.dat",'r')
content1=f.read()
p=open(r"pp_tra.dat",'r')
content2=p.read()

lines1=content2.split('\n')
arr2=[]
lines=content1.split('\n')  
arr1=[]
for i in lines:
   value=i.split()
   l=len(value)-1
   for j in range(0,l):
    value[j]=(value[j])
   arr1.append(value)
for i in lines1:
   value=i.split()
   l=len(value)-1
   for j in range(0,l):
    value[j]=(value[j])
   arr2.append(value) 


# Validation=[[0 for i in range(3)] for j in range(9*3)]
print("length of test_data case\n",len(arr1))
print("column length",len(arr2[0]))  
print(arr2[6666][192]) 
print("length of training_data case\n",len(arr2))   
print("Test data\n",arr1)
print("Training_data data\n",arr2)
Validation=[[0 for i in range(6)] for j in range(9*3)]
random.shuffle(arr2)
k=3
maxp=2 
length = int(len(arr2)/k) 
folds = []
for i in range(2):
    folds += [arr2[i*length:(i+1)*length]]
folds += [arr2[(k-1)*length:len(arr2)]]

# test_data=[]
# training_data_data=[]
# for i in range(0,3):       
#     j=i
#     test_data=folds[i]
#     for j in range(0,3):
#         if(j!=i):
#             training_data_data=training_data_data+folds[i]
#     for l in range(0,9):
#         for p in range(1,5):  
#             Validation[l][1]=p+1
#             Validation[l][0]=l+2
#             Validation[l][i+1]=KNN(training_data_data,test_data,l+2,p+1)   
    
#     for z in range(0,9):
#         avg=0.0
#         sum=0.0
#         for h in range(1,k+1):
#             sum=sum+Validation[z][h]
        
#         avg=sum/k
#         Validation[z][k+1]=avg  
# max=Validation[0][k+1]
# flag=0
# for i in range(0,len(Validation)):
#     if(Validation[i][k+1]>max):
#         max=Validation[i][k+1]
#         flag=i  

# for i in Validation:
#     print(i)
maxk=5

# maxa=Validation[0][k+2]    
# for i in range(0,len(Validation)):
#     if(Validation[i][k+2]>maxa):
#         maxa=Validation[i][k+2]
#         maxp=Validation[i][1]
#         maxk=Validation[i][1]

print("Best K :",maxk," best P: ",maxp);    