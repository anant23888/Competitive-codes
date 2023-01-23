from inspect import trace
import random


def discretdata(arr,row,col):
    a=[]
    for i in range(row):
        a1=[]
        for j in range(col):
            a1.append(round(arr[i][j]))
        a.append(a1)
    return a        

def splitdata(a):
    trainsize=int(len(a)*0.8)
    training_data=[]
    test_data=list(a)
    while len(training_data)<trainsize:
        i=random.randrange(len(test_data))
        j=test_data.pop(i)
        training_data.append(j)
    return [training_data,test_data]

def classseparated(a):
    a1={}
    for i in range(len(a)):
        c=a[i]
        if(c[4] not in a1):
            a1[c[4]]=[]
        a1[c[4]].append(c)
    return a1

def mean(number):
    p=sum(number)/len(number)
    return p               

def count(a3,j):
    a4={}
    for i in a3:
        c=i[j]
        if(c not in a4):
            a4[c]=0
        a4[c]+=1
    for i in a4:
        a4[i]=a4[i]/len(a3) 
    return a4        

f=open(r"iris.data",'r')
content1=f.read().split()
content=[eval(i) for i in content1]
arr=[]
rows,col=(150,5)
for i in range(rows):
   a=[]
   for j in range(col):
    a.append(content[col*i+j])
   arr.append(a)
a=[]
print(arr)
a=discretdata(arr,rows,col)  
training_data,test_data=splitdata(a)

a1=classseparated(training_data)
a2=[]
for i in range(3):
    for j in range(4):
        a4= count(a1[i+1],j)
        print(a4)
        a2.append(a4) 

a5=[]
for i in test_data:
    accuracy=1
    print("Probability of iris test data..",i)
    for j in range(len(i)-1):
        if i[4]==1:
            for k in a2[j]:
                if k==i[j]:
                 accuracy=accuracy*a2[j][i[j]]
        elif i[4]==2:
            for k in a2[j+4]:
                if k==i[j]:
                 accuracy=accuracy*a2[j+4][i[j]]
        else:
            for k in a2[j+8]:
                if k==i[j]:
                 accuracy=accuracy*a2[j+8][i[j]]
    print(accuracy)  
training_data,test_data=splitdata(arr)

ap=classseparated(training_data)
a2=[]
for i in range(3):
    for j in range(4):
        a4= count(ap[i+1],j)
        print(a4)
        a2.append(a4) 

a5=[]
for i in test_data:
    accuracy=1
    print("Probability of discrete iris test data..",i)
    for j in range(len(i)-1):
        if i[4]==1:
            for k in a2[j]:
                if k==i[j]:
                 accuracy=accuracy*a2[j][i[j]]
        elif i[4]==2:
            for k in a2[j+4]:
                if k==i[j]:
                 accuracy=accuracy*a2[j+4][i[j]]
        else:
            for k in a2[j+8]:
                if k==i[j]:
                 accuracy=accuracy*a2[j+8][i[j]]
    print(accuracy)  
f=open(r"pp_tes.dat",'r')
content2=f.read()
p=open(r"pp_tra.dat",'r')
content3=p.read()           

lines1=content3.split('\n')
arr2=[]
lines=content2.split('\n')  
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

t1=classseparated(arr2)
a7=[]
for i in range(9):
    for j in range(192):
        a4= count(a1[i+1],j)
        print(a4)
        a7.append(a4) 

for i in arr1:
    accuracy=1
    print("Probability of OCR test data..",i)
    for j in range(len(i)-1):
        if i[192]==1:
            for k in a2[j]:
                if k==i[j]:
                 accuracy=accuracy*a7[j][i[j]]
        elif i[192]==2:
            for k in a2[j+192]:
                if k==i[j]:
                 accuracy=accuracy*a7[j+192][i[j]]
        elif i[192]==3:
            for k in a2[j+192*2]:
                if k==i[j]:
                 accuracy=accuracy*a7[j+192*2][i[j]]
        elif i[192]==4:
            for k in a2[j+192*3]:
                if k==i[j]:
                 accuracy=accuracy*a7[j+192*3][i[j]]
        elif i[192]==5:
            for k in a2[j+192*4]:
                if k==i[j]:
                 accuracy=accuracy*a7[j+192*4][i[j]]
        elif i[192]==6:
            for k in a2[j+192*5]:
                if k==i[j]:
                 accuracy=accuracy*a7[j+192*5][i[j]]
        elif i[192]==7:
            for k in a2[j+192*6]:
                if k==i[j]:
                 accuracy=accuracy*a7[j+192*6][i[j]]
        elif i[192]==8:
            for k in a2[j+192*7]:
                if k==i[j]:
                 accuracy=accuracy*a7[j+192*7][i[j]]
        elif i[192]==9:
            for k in a2[j+192*8]:
                if k==i[j]:
                 accuracy=accuracy*a7[j+192*8][i[j]]                                                      

    print(accuracy)  

