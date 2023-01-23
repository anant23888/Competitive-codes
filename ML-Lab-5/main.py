from math import exp, pi, sqrt
import random
from statistics import variance

def splitdata(a):
    trainsize=int(len(a)*0.7)
    training_data=[]
    test_data=list(a)
    while len(training_data)<trainsize:
        i=random.randrange(len(test_data))
        j=test_data.pop(i)
        training_data.append(j)
    return [training_data,test_data]

def classseparated(training_data):
	a1 = dict()
	for i in range(len(training_data)):
		c = training_data[i]
		c1 = c[-1]
		if (c1 not in a1):
			a1[c1] = list()
		a1[c1].append(c)
	return a1

def mean(data):
	return sum(data)/float(len(data))

def standardeviation(data):
    avg=mean(data)
    l=float(len(data)-1)
    for x in data:
        k=sum([x-avg]**2)
    var=k/l
    return sqrt(var)    

def combiningdata(dataset):
    combine=[]
    for data in dataset:
        combine=[mean(data),standardeviation(data),len(data)]
    return combine    

def gaussianprob(x,mean,std):
    m1=-((x-mean)**2/(2*std**2))
    m=exp(m1)
    return (1/sqrt(2*pi)*std)*m
            



def calculate(a1,l,x):
    cp1=[]
    combine=[]
    p1=[]
    for i in range(l):
        for j in range(13):
            cp2=[]

            for k in range(len(a1[i])):
                cp2.append(a1[i][k][j]) 
            cp1.append(cp2)   
    print(len(cp1))                
    print(len(cp1[0]))   
    # cp2=dict() 
    # for i in range(len(cp1)):
    #     k=cp1[i]
    #     k1=k[-1]
    #     if k1 not in cp2:
    #         cp2[k1]=list()
    #     cp2[k1].append(k)    
    # print(len(cp2))

    for i in cp1:
        for j in len(i):
         k1=1
         combine=combiningdata(cp1[i])
         for p in range(13):
          k=(gaussianprob(x[p],combine[p][0],combine[p][1]))
          k1=k1*k
          print(k1)
          


f=open(r"heart.csv",'r')
content1=f.read().split()
content=[eval(i) for i in content1]
arr=[]
rows,col=(1025,14)
for i in range(rows):
   a=[]
   for j in range(col):
     a.append(content[col*i+j])
   arr.append(a) 
training_data,test_data=splitdata(arr)
a1=classseparated(training_data)
prob=[]
for i in test_data:
    calculate(a1,len(a1),i)
    # prob.append(p)

# print(prob)        