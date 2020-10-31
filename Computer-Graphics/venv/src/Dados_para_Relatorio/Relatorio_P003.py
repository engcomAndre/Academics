from src.Plain import Plain
from src.Sphere import Sphere
from src.Raytrace_A import Raytrace_A as Raytrace
from src.Triangle import Triangle
from src.Poligon import Poligon
from src.Light import Light
from src.Enviroment import Environment
from src.Linear_Operations import LinearOperations as ln
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# - Iluminação: escolher um dos tipos de projeção e aplicar. Nesses casos devem ser utilizados mais de 1 objeto na cena.
#     - Lambert                     ok
#     - Blinn-phong                 ok
#     - cor do ambiente             ok
#     - multiplas fontes de luz     ok

def sphere_detection_oblique():
    environment = Environment(color=[220,220,220],intensity = 10)
    light = Light(point_of_light=[40,0,-6],light_color=[240,0,0],intensity=2)
    lightA = Light (point_of_light=[-40, 0, -6], light_color=[0, 245, 0], intensity=2)
    lights = [light,lightA]
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=0.1, nx=250, ny=250)
    raytrace = Raytrace(point_of_vision=[0, 0, -6], plain=plainA,enviroment=environment,lights=lights,sensibility=1)
    sphere = Sphere(id=0, center=[0, 0, 0], radius=3, color=[0,120,222])
    raytrace.detect_poligons_in_space_oblique_case([sphere])
# sphere_detection_oblique()


def triangle_detection_oblique():
    environment = Environment (color=[220, 220, 220], intensity=10)
    light = Light(point_of_light=[40, 10, -10], light_color=[240, 0, 0], intensity=2)
    lightA = Light(point_of_light=[-40, -10, 10], light_color=[0, 245, 0], intensity=2)
    lights = [light,lightA]
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=0.1, nx=250, ny=250)
    raytrace = Raytrace (point_of_vision=[0, 0, -6], plain=plainA, enviroment=environment, lights=lights, sensibility=1)
    poligonT = [[5, -3, 0], [0, 2, 0], [-5, -3, 0]]
    triangle = Poligon([poligonT[0], poligonT[1], poligonT[2]], color=[40, 0, 241])
    raytrace.detect_poligons_in_space_oblique_case([triangle])
# triangle_detection_oblique()

def poligon_detection_oblique():
    environment = Environment (color=[220, 220, 220], intensity=10)
    light = Light (point_of_light=[40, 0, -20], light_color=[240, 0, 0], intensity=2)
    lightA = Light (point_of_light=[-40, -100, 20], light_color=[0, 245, 0], intensity=1)
    lights = [light, lightA]
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=0.2, nx=250, ny=250)
    raytrace = Raytrace (point_of_vision=[0, 0, -6], plain=plainA, enviroment=environment, lights=lights, sensibility=2)

    poligon0 = [[6, 5, 0], [-6, 5, 0], [-6, -5, 0], [6, -5, 0]]
    rectangleA = Poligon ([poligon0[0], poligon0[1], poligon0[2], poligon0[3]], color=[200, 120, 20])
    raytrace.detect_poligons_in_space_oblique_case ([rectangleA])
# poligon_detection_oblique()


def multiple_poligon_oblique():
    environment = Environment (color=[220, 220, 220], intensity=10)
    light = Light(point_of_light=[40, 10, -10], light_color=[240, 0, 0], intensity=3)
    lightA = Light(point_of_light=[-40, -10, -10], light_color=[0, 245, 0], intensity=1)
    lights = [light, lightA]
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=0.15, nx=250, ny=250)
    raytrace = Raytrace(point_of_vision=[0, 0, -10], plain=plainA, enviroment=environment, lights=lights, sensibility=2)

    poligon0 = [[20, -20, 15],[-20, -20, 15],[-12, -10, -1],[12, -10, -1]]
    poligon1 = [[20,  20, 15],[-20,  20, 15],[-12,  10, -1],[12,  10, -1]]

    rectangleA = Poligon([poligon0[0], poligon0[1], poligon0[2], poligon0[3]], color=[20, 255, 20])
    rectangleB = Poligon([poligon1[0], poligon1[1], poligon1[2], poligon1[3]], color=[255, 20, 20])
    sphereB = Sphere(id=0, center=[0, 0, 0], radius=6, color=[0,120,222])

    raytrace.detect_poligons_in_space_oblique_case([rectangleA,rectangleB,sphereB])
multiple_poligon_oblique()












