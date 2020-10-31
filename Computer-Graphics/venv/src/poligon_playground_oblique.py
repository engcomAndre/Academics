from src.Plain import Plain
from src.Sphere import Sphere
from src.Raytrace import Raytrace
from src.Triangle import Triangle
from src.Poligon import Poligon
from src.Linear_Operations import LinearOperations as ln
import numpy as np
#
# plainA = Plain(left=-10,right=10,top=10,bottom=-10,distance=1,nx = 100,ny = 100)
# ray = Raytrace(point_of_vision=[0,0,1],point_of_light=[0,0,0],plain=plainA)
#
# def poligons():
#     plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=1, nx=100, ny=100)
#     ray = Raytrace (point_of_vision=[0, 0, 1], point_of_light=[0, 0, 0], plain=plainA)
#
#     poligon  = [[6, -8, 0], [-6, -8, 0], [-6, -5, 0],[6,-5,0]]
#     poligon1 = [[6,  4, 0], [-6,  4, 0], [-6,  7, 0],[6, 7,0]]
#     poligonT = [[5,  6, 0], [0,   1, 0], [-5, 6, 0]]
#
#     rectangleA = Poligon([poligon[0], poligon[1], poligon[2],poligon[3]], color=[255, 0, 0])
#     rectangleB = Poligon([poligon1[0], poligon1[1], poligon1[2], poligon1[3]], color=[120, 120, 120])
#     triangle = Poligon ([poligonT[0], poligonT[1], poligonT[2]], color=[120, 120, 255])
#     sphereA = Sphere(id=0, center=[0,0,0], radius=0.9, color=[0,10,200])
#     sphereB = Sphere(id=0, center=[0, 0, 0], radius=0.99, color=[200, 10, 20])
#     sphereC = Sphere(id=0, center=[0, 0, 0], radius=3, color=[0, 0, 0])
#
#     ray.detect_poligons_in_space_oblique_case ([sphereB])
#
#     return [sphereB]
#     # return [rectangleA,rectangleB,triangle,sphereA]
#
# from copy import deepcopy
# class struct ():
#     def __init__(self):
#         self.centro = [30, 30, 30]
#         self.raio = 10;
#         self.cor = [20, 10, 200]
#         self.tipo = 'esfera'
#
#
#
# nx = 1000
# ny = 1000
# e = [5,5,5]
# d = 10
# l = -10
# r = 10
# t = 10
# b = -10
# obj = struct()
# w = e / np.linalg.norm(e)
# w = [np.abs(w)]
# p = w.index(min(w))
#
# tmp = deepcopy(w[0])
# tmp[p] = 1
# tmpxw = np.cross(tmp, w)[0]
# u = (tmpxw / np.linalg.norm(tmpxw))
# v = (np.cross (u, w))
#
#
# # m = np.zeros(nx, ny, 3)
# m = np.zeros ((nx, ny, 3), dtype=int)
#
# for i in range(1,nx):
#     for j in range (1,ny):
#         u_ = l + (r - l) * (0.5 + i) / nx
#         v_ = b + (t - b) * (0.5 + j) / ny
#
#         origem = e
#         direcao = np.cross(d,w) + np.cross(u_ , u) + np.cross(v_ , v)
#         direcao = np.sum(direcao)
#
#         A = np.dot(direcao, direcao)
#         B = np.dot(2 * direcao, (origem - obj.centro))
#         C = (np.dot (origem - obj.centro, origem.centro) - raio ^ 2)
#
#         delta = B ^ 2 - 4 * A * C;
#
#
#         if (delta >= 0):
#
#
#             posluz = [20,200,-10]
#
#             T1 = (-B + sqrt (delta)) / A
#             T2 = (-B - sqrt (delta)) / A
#
#             T = min(T1, T2)
#
#             P = origem + T * direcao
#
#             normal = (P - obj.centro) / obj.raio
#
#             luz = P - posluz
#             ilumi = 1
#
#             uniLuz = luz / np.linalg.norm(luz)
#             uniVis = w;
#
#             Lred = 100 * ilumi * max (0, dot (normal, uniLuz));
#
#             Lgreen = 0 * ilumi * max (0, dot (normal, uniLuz));
#
#             Lblue = 255 * ilumi * max (0, dot (normal, uniLuz));
#
#             m[i, j, 0] = Lred;
#             m[i, j, 1] = Lgreen;
#             m[i, j, 2] = Lblue;
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
