import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import mat
from math import fabs
from copy import deepcopy

image = cv2.imread("testeA.png",cv2.IMREAD_GRAYSCALE)

def CalcIntensityHistogram(image):
    histogram = [0]*256
    for line in image:
        for pixel in line:
            histogram[pixel] += 1
    return histogram

def NormHistogram(Histogram):
    piHistogram = [0]*256
    sizeImage = np.sum(Histogram)
    for intensity in range(len(piHistogram)):
        piHistogram[intensity] = Histogram[intensity]/sizeImage
    return piHistogram

def CalcAcumulatedProb(normHistogram):
    probabilityHistogram = deepcopy(normHistogram)
    for intensity in range(1,len(normHistogram)):
        probabilityHistogram[intensity] += probabilityHistogram[intensity - 1] \
                                        + normHistogram[intensity]
    return probabilityHistogram

def CalcMediaHistogram(normHistogram):
    mediaHistogram = [0] * 256
    for intensity in range(0,len(normHistogram)):
        mediaHistogram[intensity] = intensity * normHistogram[intensity]
    return mediaHistogram

def CalcAccumulatedMediaHistogram(mediaHistogram):
    AccmulateMediaHistogram = [0] * 256
    for intensity in range(1,len(mediaHistogram)):
        AccmulateMediaHistogram[intensity] = AccmulateMediaHistogram[intensity - 1]\
                                             + mediaHistogram[intensity]
    return AccmulateMediaHistogram

def CalcVarianceHistogram(ProbAccHisto,MediaAccHisto):
    varianceHistogram = [0] * 256
    for intensity in range(len(ProbAccHisto)):
        varianceHistogram[intensity] = \
            CalcVariance(MediaAccHisto[len(MediaAccHisto)-1],ProbAccHisto[intensity],MediaAccHisto[intensity])
    return varianceHistogram

def CalcMaxVarianceIndex(varianceHistogram):
    return varianceHistogram.index(max(varianceHistogram))

def CalcVariance(mediaGlobal,Probk,Mediak,):
    return fabs((mediaGlobal * Probk - Mediak)**2)\
           /(Probk * (1 - Probk))

def Limiarizacao(image,limiar):
    tempImage = deepcopy(image)
    for line in range(tempImage.shape[0]):
        for colunm in range(tempImage.shape[1]):
            if(tempImage[line][colunm] >= limiar):
                tempImage[line][colunm] = 255
            else:
                tempImage[line][colunm] = 0
    return tempImage


def OtsuMethod(OriginalImage):
    tempImage = deepcopy(OriginalImage)

    _Histogram = CalcIntensityHistogram(tempImage)
    print("Calculed Histogram :{val}".format(val=_Histogram))

    _NormHistogram = NormHistogram(_Histogram)
    print("Normalized Histogram :{val}".format(val=_NormHistogram))

    _propAccumulatedHistogram = CalcAcumulatedProb(_NormHistogram)
    print("Probabilities Acc Histogram :{val}".format(val=_propAccumulatedHistogram))

    _mediaHistogram = CalcMediaHistogram(_NormHistogram)
    print("Media Histogram :{val}".format(val=_mediaHistogram))

    _AccumulatedMediaHistogram = CalcAccumulatedMediaHistogram(_mediaHistogram)
    print("Media Accumulated Histogram:{val}".format(val=_AccumulatedMediaHistogram))

    _varianceHistogram = CalcVarianceHistogram(_propAccumulatedHistogram,_AccumulatedMediaHistogram)
    print("variance Histogram:{val}".format(val=_varianceHistogram))

    _IndexMaximizeVariance = CalcMaxVarianceIndex(_varianceHistogram)
    print("Index Maximize Variance:{val}".format(val=_IndexMaximizeVariance))

    resImage = Limiarizacao(image,_IndexMaximizeVariance)

    cv2.imshow("limiarizado ",resImage)
    cv2.waitKey(0)

    resIndex = [0]*256
    resIndex[_IndexMaximizeVariance] = 1000
    plt.plot(_Histogram)
    plt.plot(resIndex,'k',color="red")
    plt.show()

OtsuMethod(image)
















