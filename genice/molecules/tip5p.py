# coding: utf-8
"""
[1] """
desc={"ref": {"TIP5P": "M. W. Mahoney and W. L. Jorgensen, A five-site model for liquid water and the reproduction of the density anomaly by rigid, nonpolarizable potential functions, J. Chem. Phys. 112 (2000) 8910-8922."},
      "brief": "A typical five-site water model.",
      "usage": "No options available."
      }

import math
import numpy as np


oh = 0.09572 #nm
om = 0.07    #nm
hangle = 104.52 * math.pi / 180 / 2
mangle = 109.47 * math.pi / 180 / 2
mass=18
ohz = oh * math.cos(hangle)
ohy = oh * math.sin(hangle)
omz =-om * math.cos(mangle)
omx = om * math.sin(mangle)
oz  = -ohz*2/mass


sites = np.array([[0, 0,oz],
                  [0, ohy,ohz+oz],
                  [0,-ohy,ohz+oz],
                  [ omx,0,omz+oz],
                  [-omx,0,omz+oz],
                  ]) # nm, OHHMM

atoms = ["O","H","H",".","."]
labels = ["OW","HW1","HW2","MW1","MW2"]
name = "SOL"
