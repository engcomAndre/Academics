from src.Plain import Plain
from src.Sphere import Sphere
from src.Raytrace import Raytrace
from src.Triangle import Triangle
from src.Poligon import Poligon
from src.Linear_Operations import LinearOperations as ln
import numpy as np
def poligons():

    poligon =[[2.75,-3.75,5],[-3, -3.75,5],[-3, 3.35,5],[ 2.75, 3.35,5]]
    poligon1 =[[0.75, 0.35,0],[-0.9, 0.35,0],[-0.9, 0.75,0],[ 0.75, 0.75,0]]
    poligonT =[[5,-3,0],[0,-8,0],[-5,-3,0]]

    rectangleA = Poligon ([poligon[0], poligon[1], poligon[2], poligon[3]], color=[255, 0, 0])
    rectangleB = Poligon ([poligon1[0], poligon1[1], poligon1[2], poligon1[3]], color=[120, 120, 120])
    triangle = Poligon ([poligonT[0], poligonT[1], poligonT[2]], color=[120, 120, 255])
    sphereA = Sphere (id=0, center=[0.6, 0.6, 5.78], radius=4.4, color=[120, 60, 0])
    sphereB = Sphere (id=0, center=[0, 0, 0], radius=0.89, color=[60, 60, 0])
    return [sphereA,sphereB,rectangleB]

plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=1, nx=75, ny=75)
ray = Raytrace (point_of_vision=[0, 0, 1], plain=plainA)
ray.detect_poligons_in_space_orthography_case(poligons())




