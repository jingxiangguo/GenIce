import logging

import numpy as np

from genice import rigid

def run(lattice, water_type="TIP3P", guests=[]):
    """
    XMol file format (.xyz)
    """
    logger = logging.getLogger()
    lattice.stage1()   #replicate the unit cell
    lattice.stage2()   #prepare random graph
    lattice.stage3()   #Make an ice graph
    lattice.stage4()   #Depolarize
    lattice.stage5()   #Orientation
    lattice.stage6(water_type)  #Water atoms
    lattice.stage7(guests)      #Guest atoms
    logger.info("Total number of atoms: {0}".format(len(lattice.atoms)))
    logger.info("Output in MDView format.")
    s = ""
    #if celltype == "rect":
    #    s += "-length '({0}, {1}, {2})'\n".format(cell[0,0]*10,cell[1,1]*10,cell[2,2]*10)
    #s += "-center 0 0 0\n"
    #s += "-fold\n"
    s += "{0}\n".format(len(lattice.atoms))
    s += "Generated by GenIce. https://github.com/vitroid/GenIce\n"
    for i in range(len(lattice.atoms)):
        molorder, resname, atomname, position = lattice.atoms[i]
        s += "{0:5} {1:9.4f} {2:9.4f} {3:9.4f}\n".format(atomname,position[0]*10,position[1]*10,position[2]*10)
    s = '#' + "\n#".join(lattice.doc) + "\n" + s
    print(s,end="")