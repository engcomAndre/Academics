import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import mat
from math import fabs
from copy import deepcopy


imageOriginal = cv2.imread("imgA.jpg",0)

cv2.imshow("image",imageOriginal)
cv2.waitKey(0)

