import numpy as np
class Triangle():
    def __init__(self,pointA=[1,0,0],pointB=[0,1,0],pointC=[0,0,1],color =[120,120,120],t0 = -10000,t1 = 10000):
        self.t0 = t0
        self.t1 = t1
        self.pA = pointA
        self.pB = pointB
        self.pC = pointC
        self.color = color
        self.t0 = -10000000
        self.t1 = 10000000

    def compute_det_A(self,direction=[0,0,0]):
        mat_A = [[self.pA[0] - self.pB[0],self.pA[0] - self.pC[0],direction[0]],
                 [self.pA[1] - self.pB[1],self.pA[1] - self.pC[1],direction[1]],
                 [self.pA[2] - self.pB[2],self.pA[2] - self.pC[2],direction[2]],
                 ]
        return np.linalg.det(np.array(mat_A))

    def compute_det_Beta(self,origin=[0,0,0],direction=[0,0,0]):
        mat_Beta = [[self.pA[0] - origin[0],self.pA[0] - self.pC[0],direction[0]],
                    [self.pA[1] - origin[1],self.pA[1] - self.pC[1],direction[1]],
                    [self.pA[2] - origin[2],self.pA[2] - self.pC[2],direction[2]],
                 ]
        return np.linalg.det(np.array(mat_Beta))

    def compute_det_Alpha(self,origin=[0,0,0],direction=[0,0,0]):
        mat_Alpha = [[self.pA[0] - self.pB[0],self.pA[0] - origin[0],direction[0]],
                     [self.pA[1] - self.pB[1],self.pA[1] - origin[1],direction[1]],
                     [self.pA[2] - self.pB[2],self.pA[2] - origin[2],direction[2]],
                 ]
        return np.linalg.det(np.array(mat_Alpha))

    def compute_det_Mt(self,origin=[0,0,0]):
        mat_Mt = [[self.pA[0] - self.pB[0],self.pA[0] - self.pC[0],self.pA[0] - origin[0]],
                  [self.pA[1] - self.pB[1],self.pA[1] - self.pC[1],self.pA[1] - origin[1]],
                  [self.pA[2] - self.pB[2],self.pA[2] - self.pC[2],self.pA[2] - origin[2]],
                 ]
        return np.linalg.det(np.array(mat_Mt))

    def compute_t(self,origin,direction):
        detA = self.compute_det_A(direction = direction)
        detBeta = self.compute_det_Beta(origin=origin,direction=direction)
        detAlpha = self.compute_det_Alpha(origin=origin,direction=direction)
        detMt = self.compute_det_Mt(origin=origin)
        Beta = detBeta / detA
        Alpha = detAlpha / detA
        t = detMt / detA

        # if (t < self.t0 or t > self.t1):
        #     return False
        if (Beta > 0 and Alpha > 0 and Beta + Alpha < 1):
            return True,t
        else:
            return False,t



