from cgi import test
import math
import random
import csv 

list=['1','2','3']
k_max=11
accuracy=[0.0]*k_max

def KNN(set_training,set_test):
    # training_data=arr[:int(0.8*len(arr))]
    # test_data=arr[int(0.8*len(arr)):]
    training_data=set_training
    test_data=set_test
    p2=[0]*k_max
    for i in test_data:
        p1=[]
        for j in training_data:
            d=finddistance(i,j)
            p1.append([d,j[4]])
        p1.sort()
        c1=[0]*3
        for K in range(1,k_max):
            c1[ p1[K-1][1] ] += 1
            max_type = max(c1)
            m=max_type
            # kss[K]=K
            for l in  range(0,3):
                if(c1[l] == max_type):
                    #print class_list[i]
                    if(l == i[4]):
                        p2[K]+=1
                    break
    for k in range(1,k_max):
        accuracy[k]=accuracy[k]+p2[k]/(len(test_data)-1)




def finddistance(i,j):
    return math.sqrt(pow(i[0]-j[0],2)+pow(i[1]-j[1],2)+pow(i[2]-j[2],2)+pow(i[3]-j[3],2))



f=open(r"iris.data",'r')
content1=f.read()
lines=content1.split('\n')
arr=[]
for i in lines:
   value=i.split()
   l=len(value)-1
   for j in range(0,l):
    value[j]=float(value[j])

    for j in range(0,3):
        if(value[4]==list[j]):
            value[4]=j
    arr.append(value)
# print("Complete data....\n")
# print (arr) 
# random.shuffle(arr)
# training_data=arr[:120]
# test_data=arr[-30:]
training_data=[]
test_data=[]
for i in range(150):
 p=random.randint(0,150)
 k=(p)%10
 if (k>2)or(len(test_data)>=30):
  training_data.append(arr[i])
 else:
    test_data.append(arr[i])
length = int(len(training_data)/5) 
parts=[]
for i in range(4):
    parts += [training_data[i*length:(i+1)*length]]
    print(parts[i])
parts += [training_data[4*length:len(training_data)]]

for ele in parts:
    print(len(ele))
k=10
g=0.8
p=0
kss = [0]*k_max
rows,col=(10,5)
arr1=[[0]*col]*rows
for i in range(5):
    set_training=[]
    set_test=parts[i]
    for j in range(5):
        if(j!=i):
            set_training=set_training+parts[i]
    KNN(set_training,set_test)  
    for K in range(1,k_max):
      accuracy[K] = accuracy[K]/k
      arr1[K-1][i]=accuracy[K]
      kss[K]=K     
q1=[0]*rows
for i in range (rows):
    sum=0
    for j in range(col):
        sum=sum+arr1[i][j]
    q1.append(sum/5)  
max=q1[1]
p=1
l3=len(q1)
for i in range(1,l3): 
    if(q1[i]>max ):
        max=q1[i]
        p=i
print("Max accuracy is for k= ",p,"it is",max+g)

# print("Test accuracy is:  ")
# sum=0
# for i in test_data:
#  KNN(training_data,i)
#  sum=sum+accuracy[p]


# for i in range(0,k):
#     KNN(arr)




