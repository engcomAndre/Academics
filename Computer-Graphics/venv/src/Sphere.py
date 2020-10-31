from src.Linear_Operations import LinearOperations as ln
import numpy as np
class Sphere():
    def __init__(self,id = "",center="",radius=1,color=[120,120,120]):
        self.id = id
        self.center = center
        self.radius = radius
        self.color = color
        self.points = center

    def compute_circle_touch(self,origin,direction,sphere):
        eminusc = np.subtract(origin, sphere.center)
        dot_dir_dir = np.dot(direction, direction)
        dot_dir_eminusc = np.dot(2*direction, eminusc)
        dot_eminusc_eminusc = np.dot (eminusc, eminusc) - sphere.radius ** 2
        return ln().solve_quadratic_equation(dot_dir_dir, dot_dir_eminusc, dot_eminusc_eminusc)







