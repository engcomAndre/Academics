from src.Plain import Plain

from src.Raytrace import Raytrace
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def oblique_case_radiues():
    plain = Plain (nx=25, ny=25)
    raytrace = Raytrace (plain=plain)
    raytrace.plot_raies_oblique_case ()


def orthography_case_radius():
    plain = Plain (nx=25, ny=25)
    raytrace = Raytrace (plain=plain)
    raytrace.plot_raies_ortography_case ()


oblique_case_radiues ()
# orthography_case_radius()
