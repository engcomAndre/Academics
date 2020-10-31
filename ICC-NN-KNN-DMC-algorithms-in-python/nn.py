from src.dataset import dataset
from random import randint
from scipy.spatial import distance
import numpy as np
import collections


def extract_dataset_test_sample(sample_size, dataset):
    dataset_test = []
    while (len (dataset_test) < sample_size):
        dataset_test.append (dataset.pop (randint (0, len (dataset)-1)))
    return dataset_test


def nn(dataset, data_test):
    distance = ""
    _class = ""
    for data in dataset:
        temp_distance = np.linalg.norm (np.subtract (data[:len (data_test) - 1], data_test[:len (data_test) - 1]))
        if (distance == "" or distance > temp_distance):
            distance = temp_distance
            _class = data[-1]
    return _class


num_samples = 12
def run_test(arraytest=extract_dataset_test_sample (num_samples, dataset)):
    matches = 0
    for data_test in arraytest:
        nn (dataset, data_test)
        if (data_test[len(data_test) - 1] == nn (dataset, data_test)):
            matches += 1
    print ("Total de Amostras={samples} Acertos = {matches} Erros ={error}".format (samples=num_samples, matches=matches,
                                                                                 error=num_samples - matches))
run_test ()
