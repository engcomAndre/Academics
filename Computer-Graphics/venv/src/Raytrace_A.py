from src.Linear_Operations import LinearOperations as ln
from src.Plain import Plain as pl
from src.Plain import Plain
from src.Sphere import Sphere
from src.Enviroment import Environment
from src.Light import Light
from src.Triangle import Triangle
from src.Poligon import Poligon
import numpy as np
import threading
import matplotlib.pyplot as plt
import cv2

# import poligon_playground_oblique as play


class Raytrace_A ():
    def __init__(self, point_of_vision=[1, 1, 1], plain="", lights=[], enviroment=Environment(),sensibility=1):
        self.point_of_vision = point_of_vision
        self.lights = lights
        self.plain = plain
        self.vector_w, self.vector_u, self.vector_v = ln ().compute_ortogonal_plan (self.point_of_vision)
        self.imagem = np.zeros ((self.plain.len_colunms, self.plain.len_lines, 3), dtype=int)
        self.enviroment = enviroment
        self.sensibility = sensibility

    def compute_origin_oblique_case(self):
        return self.point_of_vision

    def compute_direction_oblique_case(self, x, y):
        ul, vl = self.compute_escalars (x, y)
        return np.dot (-self.plain.distance, self.vector_w) + np.dot (ul, self.vector_u) + np.dot (vl, self.vector_v)

    def compute_escalars(self, x, y):
        l, r, dimens = self.plain.get_scalar_param_ul ()
        b, t, dimens = self.plain.get_scalar_param_vl ()
        ul = ln ().compute_scalar (l, r, dimens, x)
        vl = ln ().compute_scalar (b, t, dimens, y)
        return ul, vl

    def compute_origin_ortography_case(self, x, y):
        ul, vl = self.compute_escalars (x, y)
        return self.point_of_vision + np.dot (ul, self.vector_u) + np.dot (vl, self.vector_v)

    def compute_direction_ortography_case(self):
        return np.dot (self.vector_w, -self.plain.distance)

    def sphere_detection_in_oblique_case(self, sphere):
        # imagem = np.zeros((self.plain.len_colunms,self.plain.len_lines, 3), dtype=int)
        origin = self.compute_origin_oblique_case ();
        for x in range (0, self.imagem.shape[0]):
            for y in range (0, self.imagem.shape[1]):
                direction = self.compute_direction_oblique_case ( x, y)
                delta, t1 = sphere.compute_circle_touch (origin, direction, sphere)
                if delta == True:
                    self.imagem[x][y] = sphere.color
                else:
                    self.imagem[x][y] = [255, 255, 255]
        self.save_image()

    def multiple_sphere_detection_in_oblique_case(self, spheres):
        # imagem = np.zeros((self.plain.len_colunms, self.plain.len_lines, 3), dtype=int)
        origin = self.compute_origin_oblique_case ();
        tmin = ""
        for x in range (0, self.imagem.shape[0]):
            for y in range (0, self.imagem.shape[1]):
                color = [255, 255, 255]
                tmin = ""
                direction = self.compute_direction_oblique_case (x, y)
                for sphere in spheres:
                    delta, t1 = sphere.compute_circle_touch (origin, direction, sphere)
                    if (delta == True and (tmin == "" or tmin > t1)):
                        tmin = t1
                        color = sphere.color
                self.imagem[x][y] = color
        self.save_image ()

    def triangle_detection_in_oblique_case(self, triangle):
        # imagem = np.zeros((self.plain.len_colunms,self.plain.len_lines, 3), dtype=int)
        origin = self.compute_origin_oblique_case ();
        for x in range (0, self.imagem.shape[0]):
            for y in range (0, self.imagem.shape[1]):
                direction = self.compute_direction_oblique_case (self.plain, x, y)
                delta, t = triangle.compute_t (origin=origin, direction=direction)
                if delta == True:
                    self.imagem[x][y] = triangle.color
                else:
                    self.imagem[x][y] = [255, 255, 255]
        # self.save_image()

    def multiple_triangle_detection_in_oblique_case(self, triangles):
        # imagem = np.zeros((self.plain.len_colunms,self.plain.len_lines, 3), dtype=int)
        origin = self.compute_origin_oblique_case ();
        for x in range (0, self.imagem.shape[0]):
            for y in range (0, self.imagem.shape[1]):
                color = [255, 255, 255]
                tmin = ""
                direction = self.compute_direction_oblique_case (x, y)
                for triangle in triangles:
                    t, delta = triangle.compute_t (origin, direction)
                    if (delta == True and (tmin == "" or tmin > abs (t))):
                        tmin = t
                        color = triangle.color
                        self.imagem[x][y] = color
            self.save_image ()

    def poligon_detection_in_oblique_case(self, poligon):
        # imagem = np.zeros((self.plain.len_colunms,self.plain.len_lines, 3), dtype=int)
        origin = self.compute_origin_oblique_case ();
        for x in range (0, self.imagem.shape[0]):
            for y in range (0, self.imagem.shape[1]):
                color = self.onTouchPoligon (origin, poligon, x, y)
                self.imagem[x][y] = color
        self.save_image ()

    def on_touch_poligon(self, origin, direction, poligon):
        # direction = self.compute_direction_oblique_case (x, y)
        setpoint = poligon.points[0]
        color = [255, 255, 255]
        delta = False
        t = ""
        for index in range (1, len (poligon.points) - 1):
            triangle = Triangle (setpoint, poligon.points[index], poligon.points[index + 1], t0=-10, t1=10)
            delta, t = triangle.compute_t (origin, direction)
            if (delta):
                return delta, t
        return delta, t

    def multiple_poligon_detection_in_oblique_case(self, poligons):
        # imagem = np.zeros((self.plain.len_colunms,self.plain.len_lines, 3), dtype=int)
        origin = self.compute_origin_oblique_case ();
        for x in range (0, self.imagem.shape[0]):
            for y in range (0, self.imagem.shape[1]):
                for poligon in poligons:
                    color = self.onMultipleTouchPoligon(origin, poligons, x, y)
                    self.imagem[x][y] = color
            # self.save_image ()

    def save_image(self):
        text = 'Poligon Detection OOP'
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText (self.imagem, text, (5, self.plain.len_lines - 5), font, 0.2, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imwrite ("poligon_detection_{name}.jpg".format (name="OOP"), self.imagem)

    def on_multiple_touch_poligon(self, origin, direction, poligons):
        color = [255, 255, 255]
        tmin = ""
        for poligon in poligons:
            setpoint = poligon.points[0]
            for index in range (1, len (poligon.points) - 1):
                triangle = Triangle (setpoint, poligon.points[index], poligon.points[index + 1], t0=-10, t1=10)
                delta, t = triangle.compute_t (origin, direction)
                if (delta == True and (tmin == "" or tmin > abs (t))):
                    tmin = t
                    color = poligon.color
        return delta, t

    def on_touch_poligons(self, origin, direction, poligons):
        color = self.enviroment.color
        poligonDict = {}
        for poligon in poligons:
            if (isinstance (poligon, Sphere)):
                deltaSphere, tSphere = poligon.compute_circle_touch (origin, direction, poligon)
                if (deltaSphere):
                    poligonDict[abs(tSphere)] = poligon

            if (isinstance (poligon, Poligon)):
                deltaPoligon, tPoligon = self.on_touch_poligon (origin, direction, poligon)
                if (deltaPoligon):
                    poligonDict[abs(deltaPoligon)] = poligon

        if(len(poligonDict) > 0):
            t = min(poligonDict.keys())
            poligon = poligonDict[t]
            vector_p = origin + t * direction #point od intersect poligon
            normal = ln().compute_unitary_vector(np.subtract(vector_p ,self.vector_w))
            # bling-phong shadding L = Ks * i * max(n . h)^p
            # compute vector h = (v + l)/norm(v + l)
            color = [0,0,0]
            for light in self.lights:
                self.lambert_shadding(color, light, normal, poligon, vector_p)
                self.bling_phong_shadding(color, light, normal, poligon, vector_p)
                self.environment_shadding(color)
        return color

    def environment_shadding(self, color):
        color[0] = self.enviroment.color[0] * self.enviroment.intensity + color[0]
        color[1] = self.enviroment.color[1] * self.enviroment.intensity + color[1]
        color[2] = self.enviroment.color[2] * self.enviroment.intensity + color[2]

    def bling_phong_shadding(self, color, light, normal, poligon, vector_p):
        vector_light = ln ().compute_unitary_vector (np.subtract (vector_p, light.point_of_light))
        vector_h = self.vector_w + vector_light / np.linalg.norm (self.vector_w + vector_light)
        color[0] += poligon.color[0] * light.intensity * pow(max (0, (np.dot (normal, vector_h))), self.sensibility)
        color[1] += poligon.color[1] * light.intensity * pow(max (0, (np.dot (normal, vector_h))), self.sensibility)
        color[2] += poligon.color[2] * light.intensity * pow(max (0, (np.dot (normal, vector_h))), self.sensibility)

    def lambert_shadding(self, color, light, normal, poligon, vector_p):
        # lambert shadding L = Kd * i * max(n . l)
        # compute vector n = norm(point_of_vision)
        vector_light = ln().compute_unitary_vector(np.subtract(vector_p, light.point_of_light))
        color[0] += poligon.color[0] * light.intensity * max(0,(np.dot (normal, vector_light)))
        color[1] += poligon.color[1] * light.intensity * max(0,(np.dot (normal, vector_light)))
        color[2] += poligon.color[2] * light.intensity * max(0,(np.dot (normal, vector_light)))


    def compute_ilumination(self,poligon, vector_p):
        if (isinstance (poligon, Sphere)):
            normal = (poligon.center - vector_p) / poligon.radius
        if (isinstance (poligon, Poligon)):
            array = list (np.subtract (poligon.points[0], poligon.points[1]))
            normal = ln ().compute_colinear_vector (list (array))
        for light in self.lights:
            normal_light  = ln().compute_unitary_vector(light.point_of_light - vector_p)
            normal_vision = self.vector_w

            # bling_color = self.bling_phong_shading(color,light,normal,normal_light,normal_vision,sensibility=2)
        color = [red,green,blue]
        return color

    def detect_poligons_in_space_oblique_case(self, poligons):
        origin = self.compute_origin_oblique_case ();
        for x in range (0, self.imagem.shape[0]):
            for y in range (0, self.imagem.shape[1]):
                direction = self.compute_direction_oblique_case (x, y)
                self.imagem[x][y] = self.on_touch_poligons (origin, direction, poligons)
        self.save_image ()

    def detect_poligons_in_space_orthography_case(self, poligons):
        direction = self.compute_direction_ortography_case ();
        for x in range (0, self.imagem.shape[0]):
            for y in range (0, self.imagem.shape[1]):
                origin = self.compute_origin_ortography_case(x, y)
                self.imagem[x][y] = self.on_touch_poligons(origin, direction, poligons)
        self.save_image()

#
def sphere_detection_oblique():
    environment = Environment(color=[220,220,220],intensity = 10)
    light = Light(point_of_light=[40,0,-20],light_color=[240,0,0],intensity=2)
    lightA = Light (point_of_light=[-40, -100, 20], light_color=[0, 245, 0], intensity=1)
    lights = [light,lightA]
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=0.1, nx=250, ny=250)
    raytrace = Raytrace_A(point_of_vision=[0, 0, -6], plain=plainA,enviroment=environment,lights=lights,sensibility=5)
    sphere = Sphere(id=0, center=[0, 0, 0], radius=3, color=[0,120,222])
    raytrace.detect_poligons_in_space_oblique_case([sphere])
# sphere_detection_oblique()


def multiple_poligon_oblique():
    environment = Environment (color=[240, 240, 240], intensity=10)
    light = Light(point_of_light=[40, 10, -30], light_color=[240, 0, 0], intensity=3)
    lightA = Light(point_of_light=[-40, -10, -10], light_color=[0, 245, 0], intensity=2)
    lights = [light, lightA]
    lights = [light]
    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=0.15, nx=200, ny=200)
    raytrace = Raytrace_A(point_of_vision=[0, 0, -10], plain=plainA, enviroment=environment, lights=lights, sensibility=2)

    poligon0 = [[20, -20, 15],[-20, -20, 15],[-12, -10, -1],[12, -10, -1]]
    poligon1 = [[20,  20, 15],[-20,  20, 15],[-12,  10, -1],[12,  10, -1]]

    rectangleA = Poligon([poligon0[0], poligon0[1], poligon0[2], poligon0[3]], color=[20, 255, 20])
    rectangleB = Poligon([poligon1[0], poligon1[1], poligon1[2], poligon1[3]], color=[255, 20, 20])
    sphereB = Sphere(id=0, center=[0, 0, 0], radius=6, color=[0,120,222])

    raytrace.detect_poligons_in_space_oblique_case([rectangleA,rectangleB,sphereB])
# multiple_poligon_oblique()
#













def poligons():
    enviroment = Environment(color=[0, 255, 255], intensity=0 )
    light1 = Light(point_of_light=[-125, -125, 50],light_color=[50, 50, 220], intensity=1)
    light2 = Light(point_of_light=[ 125,  125,-10],light_color=[250, 55, 55], intensity=1)
    lights = [light1]

    plainA = Plain (left=-10, right=10, top=10, bottom=-10, distance=1, nx=50, ny=50)

    ray = Raytrace (point_of_vision=[0, 0, 1], plain=plainA, enviroment=enviroment, lights=lights,sensibility=2)

    poligon0 = [[6, -8, 0], [-6, -8, 0], [-6, -5, 0], [6, -5, 0]]
    poligon1 = [[6, -4, 0], [-6, -4, 0], [-6, -1, 0], [6, -1, 0]]
    poligon2 = [[6, 0, 0], [-6, 0, 0], [-6, 3, 0], [6, 3, 0]]
    poligon3 = [[6, 4, 0], [-6, 4, 0], [-6, 7, 0], [6, 7, 0]]

    # poligonT = [[5, 6, 0], [0, 1, 0], [-5, 6, 0]]

    # testing multiple object ilumination ok
    rectangleA = Poligon ([poligon0[0], poligon0[1], poligon0[2], poligon0[3]], color=[20, 20, 20])
    rectangleB = Poligon ([poligon1[0], poligon1[1], poligon1[2], poligon1[3]], color=[20, 20, 20])
    rectangleC = Poligon ([poligon2[0], poligon2[1], poligon2[2], poligon2[3]], color=[20, 20, 20])
    rectangleD = Poligon ([poligon3[0], poligon3[1], poligon3[2], poligon3[3]], color=[20, 20, 20])

    # triangle = Poligon ([poligonT[0], poligonT[1], poligonT[2]], color=[120, 120, 120])
    # sphereA = Sphere (id=0, center=[0, 0, 0], radius=0.9, color=[60, 10, 200])
    # sphereB = Sphere (id=0, center=[0, 0, 0], radius=0.99, color=[60, 60, 60])

    # testing with ilumination ok
    # sphereC = Sphere (id=0, center=[0, 0, -100], radius=100, color=[255, 0, 0])
    # ray.detect_poligons_in_space_oblique_case ([sphereC])
    ray.detect_poligons_in_space_oblique_case ([rectangleA,rectangleB,rectangleC,rectangleD])

    # return [sphereC]
    # return [rectangleA,rectangleB,triangle,sphereA]


# poligons ()
# for light in self.lights:
        #     vector_light = vector_p - light.point_of_light  # vector l
        #     normal_light = ln().compute_unitary_vector (vector_light)
        #     normal_vision = self.vector_w
        #     lambert_shading = self.lambert_shading(poligon.color, light, normal_vision, vector_light)
        #     # bling_phong_shading = self.bling_phong_shading(poligon.color, light, normal, normal_light, normal_vision,sensibility)
        #     # sumatory_shadings[0] += lambert_shading[0] + bling_phong_shading[0]
        #     # sumatory_shadings[1] += lambert_shading[1] + bling_phong_shading[1]
        #     # sumatory_shadings[2] += lambert_shading[2] + bling_phong_shading[2]
        #     # sumatory_shadings = np.linalg.su(lambert_shading,bling_phong_shading)
        #
        # #
        # # superposition_shading = self.superposition_shading (sumatory_shadings)
        #
        # # color = self.environment_shading(bling_phong_shading, color, lambert_shading)
        # color = superposition_shading
    #
    # def superposition_shading(self, sumatory_shadings):
    #     red = np.dot (self.enviroment.color, self.enviroment.intensity)[0] + sumatory_shadings[0]
    #     green = np.dot (self.enviroment.color, self.enviroment.intensity)[1] + sumatory_shadings[1]
    #     blue = np.dot (self.enviroment.color, self.enviroment.intensity)[2] + sumatory_shadings[2]
    #     color = [red, green, blue]
    #     return color
    #
    # def environment_shading(self, bling_phong_shading, color, lambert_shading):
    #     red = self.enviroment.color[0] * self.enviroment.intensity + lambert_shading[0] + bling_phong_shading[0]
    #     green = self.enviroment.color[1] * self.enviroment.intensity + lambert_shading[1] + bling_phong_shading[1]
    #     blue = self.enviroment.color[2] * self.enviroment.intensity + lambert_shading[2] + bling_phong_shading[2]
    #     color = [red, green, blue]
    #     return color
    #
    # def bling_phong_shading(self, color, light, normal, normal_light, normal_vision, sensibility):
    #     vector_h = [normal_vision[0] + normal_light[0], normal_vision[1] + normal_light[1],
    #                 normal_vision[2] + normal_light[2]]
    #     vector_h = vector_h / np.linalg.norm (vector_h)
    #     red =   (color[0] * light.light_color[0] * light.intensity * pow (max (0, np.dot (normal, vector_h)), light.intensity))
    #     green = (color[1] * light.light_color[1] * light.intensity * pow (max (0, np.dot (normal, vector_h)), light.intensity))
    #     blue =  (color[2] * light.light_color[2] * light.intensity * pow (max (0, np.dot (normal, vector_h)), light.intensity))
    #     color = [red, green, blue]
    #     return color
    #
    # def lambert_shading(self, color, light, normal_vision, normal_light):
    #     red = color[0]   * light.intensity * max(0, np.dot(normal_vision, normal_light))
    #     green = color[1] * light.intensity * max(0, np.dot(normal_vision, normal_light))
    #     blue =  color[2]  * light.intensity * max(0, np.dot(normal_vision, normal_light))
    #     color = [red, green, blue]
    #     return color