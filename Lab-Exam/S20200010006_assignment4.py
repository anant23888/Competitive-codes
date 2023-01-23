# from __future__ import all_feature_names
import csv
import random
import math

file=open('IRIS.csv')
type(file)
csvreader=csv.reader(file)
rows=[]
for row in csvreader:
    rows.append(row)

    
training=[[0 for i in range(len(rows[0]))] for j in range(len(rows))]


for ele in range(0,len(rows)):
    for i in range(0,len(rows[0])):
        training[ele][i]=rows[ele][i]
        
no_of_rows_test=30
test=[[0 for i in range(len(rows[0]))] for j in range(no_of_rows_test)]

arr=[]

def randomIndex(arr,m):
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
   
randomIndex(arr,no_of_rows_test)     

arr.sort()
for ele in range(0,no_of_rows_test):
    for i in range(0,len(rows[0])):
        test[ele][i]=training[arr[ele]][i]


for ele in range(0,no_of_rows_test):
    training.pop(arr[ele]-ele)


#Discretize the data by rounding each feature value to its closest integer
def discretize(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=round(float(data[i][j]))
    return data



def function1(training,test):
    training=discretize(training)
    test=discretize(test)
    # Total number of classes in data set
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
    print(separated)
    # probability of each classes

    def totalClassRows(class_value,dataset):
        sum=0;
        for i in range(len(dataset)):
            if(dataset[i][len(dataset[i])-1]==class_value):
                sum=sum+1
                    
        return sum;
            
    prob=[0 for i in range(0,len(separated))]
    for label in separated:
        sum=totalClassRows(label,training)
        prob[label-1]=sum/len(training)
            

    #probability of each feature
    def cal_prob(dataset,featureIndex,feature_val):
        sum=0
        for i in range(len(dataset)):
            if(dataset[i][featureIndex]==feature_val):
                sum=sum+1
            
        p=sum/len(dataset)
        return p
                
                
    def feature_value_prob(dataset):
        all_feature=[]
        for i in range(len(dataset[0])-1):
            column=[];
            seperated_by_feature=separate_by_class(dataset,i)
            for label_feature in seperated_by_feature:
                vector=[]
                vector.append(label_feature)
                vector.append(cal_prob(dataset,i,label_feature))
                column.append(vector)
                    
            all_feature.append(column)
            
        return all_feature


            
    # v1=feature_value_prob(separated[1])
        # v1.pop(0)
        # for ele in v1:
        #     print(ele)

    all_feature_eachClass=[]
    for label in separated:
        all_feature_eachClass.append(feature_value_prob(separated[label]))


    print("Probability of each feature value of all features of each class: ")
    

        # Now p(x/w) for each class for training data set:

        #Only first element
    count=0;
    for z in range(0,len(test)):
        prob_test_feature_class=[];
        for label in separated:
            p=1;
            for i in range(len(all_feature_eachClass[label-1])):
                for j in range(len(all_feature_eachClass[label-1][i])):
                    if(all_feature_eachClass[label-1][i][j][0]==test[z][i]):
                        p=p*all_feature_eachClass[label-1][i][j][1];
                        break;
            prob_test_feature_class.append(p);
                
        p_x=0;
        for ele in range(len(prob_test_feature_class)):
            p_x=p_x+prob_test_feature_class[ele]*prob[ele]

        p_w_x=[]
        for label in separated:
            p_x_w=prob_test_feature_class[label-1]
            y=p_x_w*prob[label-1];
            p_wi_x=y/p_x
            p_w_x.append(p_wi_x)
        
        print("P(w()/x) of all three class")
        for ele in p_w_x:
            print("P(w()/x):",ele)
            
        print()
            
        k=1;
        max=p_w_x[0]

        for label in separated:
            if(max<p_w_x[label-1]):
                max=p_w_x[label-1]
                k=label

        if(test[z][len(test[z])-1]==k):
            count=count+1;
            
        
    print("Accuracy:")
    print(count/len(test)*100);


for f in range(0,2):
    if(f==0):
        print("If the data is used without discretization")
        function1(training,test)
        flag=1
        print("====================================================================================")
    else:
        print("If the data is used with discretization:")
        training=discretize(training)
        test=discretize(test)
        function1(training,test)
        
print("====================================================================================")
print("Using the OCR data:")
file=open('training.csv')
type(file)
csvreader=csv.reader(file)


rows_tra=[]
no_columns_tra=0
for row in csvreader:
    no_columns_tra=len(row)
    rows_tra.append(row)

training=[[0 for i in range(no_columns_tra)] for j in range(len(rows_tra))]


for ele in range(0,len(rows_tra)):
    for i in range(0,no_columns_tra):
        training[ele][i]=rows_tra[ele][i]
        
file.close()
        
file=open('test.csv')
type(file)
csvreader=csv.reader(file)
rows_tes=[]
no_columns_tes=0
for row in csvreader:
    no_columns_tes=len(row)
    rows_tes.append(row)


test=[[0 for i in range(no_columns_tes)] for j in range(len(rows_tes))]
for ele in range(0,len(rows_tes)):
    for i in range(0,no_columns_tes):
        test[ele][i]=rows_tes[ele][i]
        
function1(training,test)