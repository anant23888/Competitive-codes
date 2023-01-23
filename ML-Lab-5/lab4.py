from csv import reader
from math import sqrt
from math import exp
from math import pi
import random
def stoi(dataset, column):
	class_values = [row[column] for row in dataset]
	distinct = set(class_values)
	info = dict()
	for i, value in enumerate(distinct):
		info[value] = i
	for row in dataset:
		row[column] = info[row[column]]
	return info

def split_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated

def mean(numbers):
	return sum(numbers)/float(len(numbers))

def std_dev(numbers):
	avg = mean(numbers)
	return sqrt(sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1))
	

def mean_stdev_count_forEachColumn(dataset):
	statistics = [(mean(column), std_dev(column), len(column)) for column in zip(*dataset)]
	del(statistics[-1])
	return statistics

def summarize_by_class(dataset):
	separated = split_by_class(dataset)
	statistics = dict()
	for class_value, rows in separated.items():
		statistics[class_value] = mean_stdev_count_forEachColumn(rows)
	return statistics

def gaussian_PDF(x, mean, std_dev):
	return (1 / (sqrt(2 * pi) * std_dev)) * exp(-((x-mean)**2 / (2 * std_dev**2 )))

def calculate_class_probabilities(statistics, row):
	total_rows = sum([statistics[label][0][2] for label in statistics])
	probabilities = dict()
	for class_value, class_statistics in statistics.items():
		probabilities[class_value] = statistics[class_value][0][2]/float(total_rows)
		for i in range(len(class_statistics)):
			mean, std_dev, _ = class_statistics[i]
			probabilities[class_value] *= gaussian_PDF(row[i], mean, std_dev)
	return probabilities

def naive_bayes(statistics, row):
	probabilities = calculate_class_probabilities(statistics, row)
	best_label, max_probability = None, -1
	for class_value, probability in probabilities.items():
		if best_label is None or probability > max_probability:
			max_probability = probability
			best_label = class_value
	return best_label

dataset = list()
with open('heart.csv', 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
for i in range(len(dataset[0])-1):
    for row in dataset:
        row[i] = float(row[i].strip())
stoi(dataset, len(dataset[0])-1)
model = summarize_by_class(dataset)
random.shuffle(dataset)
#splitting data in 70:30
train1 = dataset[:int(0.7*len(dataset))]
test1 = dataset[int(0.7*len(dataset)):]
count=0
for i in range(len(test1)):
	label = naive_bayes(model, test1[i])
	if test1[i][13]==label:
		count=count+1
print('Accuracy is ',count/len(test1)*100,'%')