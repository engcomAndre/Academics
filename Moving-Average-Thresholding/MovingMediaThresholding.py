import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import mat
from math import fabs
from copy import deepcopy

def InitialAverage(initPixelIntensity,nCoeficient):
    return initPixelIntensity / nCoeficient

def CurrentAverage(previousAverage,nCoeficient,PixelIntensity):
    return previousAverage * (n - 1)/n + PixelIntensity

def ScrollImage(image,nCoeficient = 5,bCoeficient = 0.5):
    tImage = deepcopy(image)
    previousAvr = tImage[nCoeficient+1][0] / nCoeficient
    for _ln in range(nCoeficient,tImage.shape[0]):
        for _cl in range(tImage.shape[1]):
            avr = previousAvr + (tImage[_ln][_cl] - tImage[_ln - nCoeficient][_cl]) / nCoeficient
            previousAvr = avr

            print("media : {md}".format(md=avr))
            input("...")




img = cv2.imread("inputA.jpg",cv2.IMREAD_GRAYSCALE)

ScrollImage(img,20,)



