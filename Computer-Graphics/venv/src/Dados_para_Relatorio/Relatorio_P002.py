from src.Plain import Plain
from src.Sphere import Sphere
from src.Raytrace import Raytrace
from src.Triangle import Triangle
from src.Poligon import Poligon
from src.Enviroment import Environment
from src.Linear_Operations import LinearOperations as ln
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# - Caso ortográfico    ok
#	- esfera            ok
#	- triângulo         ok
#	- polígono qualquer ok
# - Caso oblíquo        ok
#	- esfera            ok
#	- triângulo         ok
#	- polígono qualquer ok


def sphere_detection_oblique(sphere = Sphere(id=0, center=[0, 0, 0], radius=5, color=[0, 200, 255])):
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=0.25, nx=250, ny=250)
    raytrace = Raytrace (point_of_vision=[0, 0, -6], plain=plainA)
    raytrace.detect_poligons_in_space_oblique_case([sphere])
# sphere_detection_oblique()

def triangle_detection_oblique():
    poligonT = [[5, -2, 0], [0, 3, 0], [-5, -2, 0]]
    triangle = Poligon ([poligonT[0], poligonT[1], poligonT[2]], color=[255, 200, 0])
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=0.1, nx=250, ny=250)
    raytrace = Raytrace (point_of_vision=[0, 0, -6], plain=plainA)
    raytrace.detect_poligons_in_space_oblique_case ([triangle])
# triangle_detection_oblique()
def poligon_detection_oblique():
    poligon0 = [[8, 3, 0],[0, 8, 0],[-8, 3, 0], [-5, -5, 0], [5, -5, 0]]
    rectangleA = Poligon ([poligon0[0], poligon0[1], poligon0[2], poligon0[3],poligon0[4]], color=[200, 120, 20])
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=0.2, nx=250, ny=250)
    raytrace = Raytrace (point_of_vision=[0, 0, -6], plain=plainA)
    raytrace.detect_poligons_in_space_oblique_case ([rectangleA])
# poligon_detection_oblique()

def sphere_detection_ortography(sphere = Sphere(id=0, center=[0, 0, -100], radius=5, color=[255, 200, 0])):
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=100, nx=250, ny=250)
    raytrace = Raytrace (point_of_vision=[0, 0, -50], plain=plainA)
    raytrace.detect_poligons_in_space_orthography_case([sphere])
# sphere_detection_ortography()

def triangle_detection_ortography():
    poligonT = [[5, -2, 0], [0, 3, 0], [-5, -2, 0]]
    triangle = Poligon ([poligonT[0], poligonT[1], poligonT[2]], color=[0, 0, 255])
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=100, nx=250, ny=250)
    raytrace = Raytrace (point_of_vision=[0, 0, -600], plain=plainA)
    raytrace.detect_poligons_in_space_orthography_case([triangle])
# triangle_detection_ortography()

def poligon_detection_ortography():
    poligon0 = [[8, 3, 0], [0, 8, 0], [-8, 3, 0], [-5, -5, 0], [5, -5, 0]]
    rectangleA = Poligon ([poligon0[0], poligon0[1], poligon0[2], poligon0[3],poligon0[4]], color=[200, 120, 20])
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance= 0.5, nx=500, ny=500)
    raytrace = Raytrace (point_of_vision=[0, 0, -1], plain=plainA)
    raytrace.detect_poligons_in_space_orthography_case([rectangleA])
poligon_detection_ortography()

def multiple_poligon_oblique():
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=1, nx=100, ny=100)
    raytrace = Raytrace (point_of_vision=[0, 0, -1], plain=plainA)

    poligon0 = [[6, -8, 0], [-6, -8, 0], [-6, -5, 0], [6, -5, 0]]
    poligon1 = [[6,  4, 0], [-6,  4, 0], [-6,  8, 0], [6,  8, 0]]

    rectangleA = Poligon ([poligon0[0], poligon0[1], poligon0[2], poligon0[3]], color=[20, 255, 20])
    rectangleB = Poligon ([poligon1[0], poligon1[1], poligon1[2], poligon1[3]], color=[255, 20, 20])

    sphereB = Sphere (id=0, center=[0, 0, 0], radius=0.985, color=[20, 20, 255])

    raytrace.detect_poligons_in_space_oblique_case([rectangleA,rectangleB,sphereB])

def multiple_poligon_ortography():
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=1, nx=100, ny=100)
    raytrace = Raytrace (point_of_vision=[0, 0, -1], plain=plainA)

    poligon0 = [[6, -8, 0], [-6, -8, 0], [-6, -5, 0], [6, -5, 0]]
    poligon1 = [[6,  4, 0], [-6,  4, 0], [-6,  8, 0], [6,  8, 0]]

    rectangleA = Poligon ([poligon0[0], poligon0[1], poligon0[2], poligon0[3]], color=[20, 255, 20])
    rectangleB = Poligon ([poligon1[0], poligon1[1], poligon1[2], poligon1[3]], color=[255, 20, 20])

    sphereB = Sphere (id=0, center=[0, 0, 0], radius=0.985, color=[20, 20, 255])

    raytrace.detect_poligons_in_space_orthography_case([rectangleA,rectangleB,sphereB])

# multiple_poligon_ortography()







