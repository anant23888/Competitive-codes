from cmath import exp
import csv
import random
import math
import numpy as np
file=open('heart.csv')
type(file)
csvreader=csv.reader(file)
rows=[]
for row in csvreader:
    rows.append(row)

    

no_of_rows_test=307
training=[[0 for i in range(len(rows[0]))] for j in range(len(rows))]
for ele in range(0,len(rows)):
    for i in range(0,len(rows[0])):
        training[ele][i]=rows[ele][i]
        
def randomIndetraining(arr,m):
    i=0;
    while(i<m):
        n=random.randint(0,len(training))
        if(i==0):
            arr.append(n)
            i=i+1
        else:
            flag=0
            for ele in arr:
                if(ele==n):
                    flag=1
                    break
            
            if(flag==0):
                arr.append(n)
                i=i+1

arr=[]
test=[[0 for i in range(len(rows[0]))] for j in range(no_of_rows_test)]
randomIndetraining(arr,no_of_rows_test)
arr.sort()
for ele in range(0,no_of_rows_test):
    for i in range(0,len(rows[0])):
        test[ele][i]=training[arr[ele]][i]


for ele in range(0,no_of_rows_test):
    training.pop(arr[ele]-ele)

for ele in training:
    for i in range(0,len(ele)):
        ele[i]=float(ele[i]);

for ele in test:
    for i in range(0,len(ele)):
        ele[i]=float(ele[i]);
        
        
# print(len(training))
# print(len(test))
def separate_by_class(dataset,l):
        separated = dict()
        for i in range(len(dataset)):
            vector = dataset[i]
            class_value = vector[l]
            if (class_value not in separated):
                separated[class_value] = list()
            separated[class_value].append(vector)
        return separated

    
separated = separate_by_class(training,-1)

# probability of classes
pro_clases=[]
for label in separated:
    pro_clases.append(len(separated[label])/len(training))



def mean_feature(i,dataset):
    sum0=0;
    for row in dataset:
        sum0=sum0+row[i];
        
    return sum0/len(dataset);



def dev_feature(i,dataset,mean):
    sum0Dev=0;
    for row in dataset:
        sum0Dev=sum0Dev+(row[i]-mean)**2.0;
    
    return (sum0Dev/len(separated[label]))**(0.5);


def fun2(x,mean,dev):
    prob=math.exp((-0.5)*(((x-mean)/dev)**2))
    prob=prob/dev
    prob=prob/((2*3.14)**(0.5))
    return prob;

def fun3(dataset,i):
    separated_by_category_fetures=separate_by_class(dataset,i);
    arr2=[]
    for label in separated_by_category_fetures:
        arr3=[]
        arr3.append(label)
        arr3.append(len(separated_by_category_fetures[label])/len(dataset))
        arr2.append(arr3);
    
    return arr2;
        
mean_each_class=[]
dev_each_class=[]
def fun1(dataset):
    mean_of_features=[];
    dev_of_features=[];
    mean_of_features.append(mean_feature(0,dataset))
    mean_of_features.append(mean_feature(3,dataset))
    mean_of_features.append(mean_feature(4,dataset))
    mean_of_features.append(mean_feature(7,dataset))
    mean_of_features.append(mean_feature(9,dataset))
    dev_of_features.append(dev_feature(0,dataset,mean_of_features[0]));
    dev_of_features.append(dev_feature(3,dataset,mean_of_features[1]));
    dev_of_features.append(dev_feature(4,dataset,mean_of_features[2]));
    dev_of_features.append(dev_feature(7,dataset,mean_of_features[3]));
    dev_of_features.append(dev_feature(9,dataset,mean_of_features[4]));
    mean_each_class.append(mean_of_features)
    dev_each_class.append(dev_of_features)

prob_category_features_each_class=[]
for label in separated:
    category_features_prob=[]
    fun1(separated[label])
    category_features_prob.append(fun3(separated[label],1));
    category_features_prob.append(fun3(separated[label],2));
    category_features_prob.append(fun3(separated[label],5));
    category_features_prob.append(fun3(separated[label],6));
    category_features_prob.append(fun3(separated[label],8));
    category_features_prob.append(fun3(separated[label],10));
    category_features_prob.append(fun3(separated[label],11));
    category_features_prob.append(fun3(separated[label],12));
    prob_category_features_each_class.append(category_features_prob)


def p_x_wi(k,i):
    p=1;
    for ele in range(0,len(test[i])):
        if(ele==0):
            p=p*fun2(test[i][ele],mean_each_class[int(k)][0],dev_each_class[int(k)][0]);
        elif ele==1:
            for j in prob_category_features_each_class[int(k)][0]:
                if(j[0]==test[i][ele]):
                    p=p*j[1];
                    break;
        elif ele==2:
            for j in prob_category_features_each_class[int(k)][1]:
                if(j[0]==test[i][ele]):
                    p=p*j[1];
                    break;
                    
        elif ele==3:
            p=p*fun2(test[i][ele],mean_each_class[int(k)][1],dev_each_class[int(k)][1]);
        elif ele==4:
            p=p*fun2(test[i][ele],mean_each_class[int(k)][2],dev_each_class[int(k)][2]);
        elif ele==5:
            for j in prob_category_features_each_class[int(k)][2]:
                if(j[0]==test[i][ele]):
                    p=p*j[1];
                    break;
                    
        elif ele==6:
            for j in prob_category_features_each_class[int(k)][3]:
                if(j[0]==test[i][ele]):
                    p=p*j[1];
                    break;
                    
        elif ele==7:
            p=p*fun2(test[i][ele],mean_each_class[int(k)][3],dev_each_class[int(k)][3]);
        elif ele==8:
            for j in prob_category_features_each_class[int(k)][4]:
                if(j[0]==test[i][ele]):
                    p=p*j[1];
                    break;
                    
        elif ele==9:
            p=p*fun2(test[i][ele],mean_each_class[int(k)][4],dev_each_class[int(k)][4]);
        elif ele==10:
            for j in prob_category_features_each_class[int(k)][5]:
                if(j[0]==test[i][ele]):
                    p=p*j[1];
                    break;
                    
        elif ele==11:
            for j in prob_category_features_each_class[int(k)][6]:
                if(j[0]==test[i][ele]):
                    p=p*j[1];
                    break;
                    
        elif ele==12:
            for j in prob_category_features_each_class[int(k)][7]:
                if(j[0]==test[i][ele]):
                    p=p*j[1];
                    break;
    
    return p;

count=0;
for ele in range(0,len(test)):
    p_x=0;
    for label in separated:
        p_x=p_x+p_x_wi(label,ele);     

    p_wi_x=[]
    for label in separated:
        p_w1_x=p_x_wi(label,ele)*pro_clases[int(label)]
        p_w1_x=p_w1_x/p_x;
        print("proster probability of"+"class",label," ",p_w1_x)
        p_wi_x.append(p_w1_x)

    if(p_wi_x[0]>p_wi_x[1]):
        predicted_class=0;
    else:
        predicted_class=1;
    
    if(predicted_class==test[ele][13]):
        count=count+1;
    
    print("----------------")
    
    
print("Accuracy: ",count/len(test)*100)