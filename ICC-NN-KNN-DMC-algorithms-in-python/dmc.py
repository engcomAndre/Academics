from src.dataset import dataset
from random import randint
from scipy.spatial import distance
from operator import *
from scipy import ndimage
import numpy as np
from collections import Counter



def extract_dataset_test_sample(sample_size, dataset):
    dataset_test = []
    while (len (dataset_test) < sample_size):
        dataset_test.append (dataset.pop (randint (0, len (dataset) - 1)))
    return dataset_test


def nn(dataset, data_test):
    nn_array = []
    for data in dataset:
        nn_array.append ([np.linalg.norm
                          (np.subtract (data[:len (data_test) - 1], data_test[:len (data_test) - 1])), data[-1]])
    return nn_array[0]

def compute_centroids(dataset):
    dict = {}
    classes = []
    for data in dataset:
        if (data[-1] not in list (dict.keys ())):
            dict[data[-1]] = []
            classes.append (data[-1])
        dict[data[-1]].append (data[:len (data) - 1])
    centroids = []
    for key in dict.keys ():
        lista = (list (ndimage.center_of_mass (np.array (dict[key]))))
        lista.append (key)
        centroids.append (lista)
    return centroids


def dmc(dataset, data_test):
    centroids = compute_centroids(dataset)
    centroid = (list(ndimage.center_of_mass(np.array(data_test[:len(data_test)-1]))))
    return nn(centroids,centroid)[1]


num_samples = 20
data_test = extract_dataset_test_sample (num_samples, dataset)[0]

def run_test(dataset=extract_dataset_test_sample (num_samples, dataset)):
    matches = 0
    for data_test in dataset:
        data1 = data_test[len (data_test) - 1]
        data2 = dmc(dataset, data_test)
        real = data1 == data2
        if (data_test[len (data_test) - 1] == dmc(dataset, data_test)):
            matches += 1
            print (data_test, dmc(dataset, data_test))
    print (
        "Total de Amostras={samples} Acertos = {matches} Erros ={error}".format (samples=num_samples,
                                                                                 matches=matches,
                                                                                 error=num_samples - matches))
run_test()
