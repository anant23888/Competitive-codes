from curses import KEY_F4
import math
import random

#1-NNC implementation
def length1NN(trainig_data,x,c):
   l=len(trainig_data)
   p=[trainig_data[0][0],trainig_data[0][1],trainig_data[0][2],trainig_data[0][3]]
   q=[x[0],x[1],x[2],x[3]]
   k1=trainig_data[0][4]
   k=math.dist(p,q)
   for i in range(l):
      p=[trainig_data[i][0],trainig_data[i][1],trainig_data[i][2],trainig_data[i][3]]
      q=[x[0],x[1],x[2],x[3]]
      p1=math.dist(p,q)
      if p1<k:
         k=p1
         k1=trainig_data[i][4]
   if k1==x[4]:
    c+=1    
   return c   

#3-NNC implementation
def length3NN(trainig_data,x,c1):
   l=len(trainig_data)
   p=[trainig_data[0][0],trainig_data[0][1],trainig_data[0][2],trainig_data[0][3]]
   q=[x[0],x[1],x[2],x[3]]
   k1=trainig_data[0][4]
   k4=trainig_data[0][4]
   k5=trainig_data[0][4]
   k=math.dist(p,q)
   k2=math.dist(p,q)
   k3=math.dist(p,q)
   p1=[]
   for i in range(l):
      p=[trainig_data[i][0],trainig_data[i][1],trainig_data[i][2],trainig_data[i][3]]
      q=[x[0],x[1],x[2],x[3]]
      pair=(math.dist(p,q),trainig_data[i][4])
      p1.append(pair)

   p1.sort(key= lambda y:y[0])
   count=0
   if p1[0][1]==x[4]:
      count+=1
   if  p1[1][1]==x[4]:
      count+=1 
   if p1[2][1]==x[4]:
    count+=1   

   if count>=2:
      c1+=1
   return c1      


      
#main-function 

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
print("Complete data....\n")
print (arr) 

trainig_data=[]
test_data=[]
for i in range(150):
 p=random.randint(0,150)
 k=(p)%10
 if (k>2)or(len(test_data)>=30):
  trainig_data.append(arr[i])
 else:
    test_data.append(arr[i])

t1=len(trainig_data)
t2=len(test_data)
c=0
print("Accuracies..")
for i in range(len(test_data)):
 c=length1NN(trainig_data,test_data[i],c)
print(c/t2*100) 
c1=0
for i in range(len(test_data)):
 c1=length3NN(trainig_data,test_data[i],c1)
print(c1/t2*100) 
f.close()