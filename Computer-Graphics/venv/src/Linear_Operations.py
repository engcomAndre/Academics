import numpy as np
from functools import reduce
from copy import deepcopy
from src.Plain import Plain as pl


class LinearOperations():
    def __init__(self,string=""):
        self.string = string

    def compute_unitary_vector(self,vector=[0,0,0]):
        if(list(vector) == list([0,0,0])):
            return vector
        return list(vector/np.linalg.norm(vector))

    def compute_colinear_vector(self,*args):
        if(len(args) == 1):
            t = deepcopy(args[0])
            min_t = t.index(min(np.abs(t)))
            if (t[min_t] == 1):
                t[min_t] = 0
            else:
                t[min_t] = 1
        elif(len(args) == 2):
            return self.compute_unitary_vector(list(np.cross(args[0],args[1])))
        return self.compute_unitary_vector(list(np.cross(args[0],t)))

    def compute_ortogonal_plan(self,origin):
        w = self.compute_unitary_vector(origin)
        u = self.compute_colinear_vector(w)
        v = self.compute_colinear_vector(w,u)
        return w,u,v

    def compute_scalar(self,dels_lb,dels_rt,dimens,index):
        return dels_lb + ((dels_rt - dels_lb)*(index + 0.5)) / dimens


    def solve_quadratic_equation(self,A,B,C):
        delta = B ** 2 - 4 * A * C
        t1 = t2 = ""        
        if delta >= 0:
            t1 = abs((-B - delta ** 0.5) / A)
            t2 = abs((-B + delta ** 0.5) / A)
            return True,min([t1,t2])
        return False, min([t1,t2])





