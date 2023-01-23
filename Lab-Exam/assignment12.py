import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('mnist_train.csv')
# print(data.head())
data=np.array(data)
m,n=data.shape
# np.random.shuffle(data)
data_val=data[0:9600].T
# print(data_test)
x_val=data_val[1:n]
# print(x_test)
y_val=data_val[0]
# print(y_test)
data_train=data[9600:38400]
y_train=data_train[0]
x_train=data_train[1:n]
