from src.dataset import dataset
from random import randint
from scipy.spatial import distance
from operator import *
import numpy as np
from collections import Counter



def extract_dataset_test_sample(sample_size, dataset):
    dataset_test = []
    while (len (dataset_test) < sample_size):
        dataset_test.append (dataset.pop (randint (0, len(dataset)-1)))
    return dataset_test

def nn(dataset, data_test):
    nn_array = []
    for data in dataset:
        nn_array.append([np.linalg.norm
                        (np.subtract(data[:len (data_test) - 1], data_test[:len (data_test) - 1])), data[-1]])
    return nn_array

def knn(dataset, data_test,k):
    nn_array = nn(dataset, data_test)
    knn_array = sorted(nn_array,key=itemgetter(0))[:k]
    _classVotes = dict(Counter(list(map(lambda x: x[1], knn_array))))
    _class = (max(_classVotes.items(), key=itemgetter(1))[0])
    return _class

num_samples = 20
data_test=extract_dataset_test_sample(num_samples, dataset)[0]
def run_test(dataset=extract_dataset_test_sample(num_samples, dataset)):
    matches = 0
    for data_test in dataset:
        if (data_test[len(data_test) - 1] == knn(dataset, data_test,50)):
            matches += 1
            print(data_test,knn(dataset, data_test,50))
    print (
        "Total de Amostras={samples} Acertos = {matches} Erros ={error}".format (samples=num_samples, matches=matches,
                                                                                 error=num_samples - matches))
run_test()
