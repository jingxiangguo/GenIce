# coding: utf-8
#Minimal implementation for genice.
#openjscad-like postmodifier style
import logging

import numpy as np


bondfunc="""
module bond(p1=[0,0,0],p2=[1,1,1],r=1)
{
    d = p2 - p1;
    H = sqrt(d[0]*d[0] + d[1]*d[1] + d[2]*d[2]);
    R = sqrt(d[0]*d[0] + d[1]*d[1]);
    //atan2(y,x)
    theta = 90-atan2(d[2],R);
    phi   = atan2(d[1],d[0]);
    echo(theta,phi);
    translate(p1)
    rotate([0,theta,phi])
    cylinder(r=r, h=H);
}
"""

class OpenScad():
    def __init__(self, s=""):
        self.string = s

    def encode(self, *codes): #Stored value as a string
        return "".join([code.__str__() for code in codes])
    
    def use(self, f):
        return OpenScad("use <{0}>;\n".format(f))

    def defvar(self, name, value):
        return OpenScad("{0}={1};\n".format(name,value))

    def translate(self, value):
        return OpenScad("translate([{0},{1},{2}]){{\n{3}}} //translate\n".format(*value, self.string))

    def scale(self, value):
        return OpenScad("scale([{0},{1},{2}]){{\n{3}}} //scale\n".format(*value, self.string))

    def rotate(self, value):
        return OpenScad("rotate([{0},{1},{2}]){{\n{3}}} //rotate\n".format(*value, self.string))

    def mirror(self, value):
        return OpenScad("mirror([{0},{1},{2}]){{\n{3}}} //mirror\n".format(*value, self.string))

    def add(self, *values):
        return OpenScad("union(){\n" + "".join([self.__str__()] + [value.__str__() for value in values]) + "} //union\n")

    def union(self, *values):
        return self.add(*values)
    
    def subtract(self, *values):
        return OpenScad("difference(){\n" + "".join([self.__str__()] + [value.__str__() for value in values]) + "} //difference\n")

    def intersect(self, *values):
        return OpenScad("intersection(){\n" + "".join([self.__str__()] + [value.__str__() for value in values]) + "} //intersection\n")

    #aliases for backward compat
    def union(self, *values):
        return self.add(*values)
    
    def difference(self, *values):
        return self.subtract(*values)
    
    def intersection(self, *values):
        return self.intersect(*values)

    #operators
    def __or__(self, value):
        return self.add(value)
                
    def __and__(self, value):
        return self.intersect(value)
                
    def __sub__(self, value):
        return self.subtract(value)

    #primitives
    def rhomb(self, cell):
        origin = np.zeros(3)
        points = [x+y+z for x in (origin,cell[0]) for y in (origin,cell[1]) for z in (origin,cell[2])]
        s = "polyhedron(["
        for point in points:
            s += "[{0},{1},{2}],\n".format(*point)
        s += "],\n"
        faces = [[0,1,3,2],[0,4,5,1],[0,2,6,4],[5,4,6,7],[6,2,3,7],[3,1,5,7]]
        s += "["
        for face in faces:
            s += "[{3},{2},{1},{0}],\n".format(*face)
        s += "]);\n"
        return OpenScad(s)

    def bond(self, s1,s2,r=1.0):
        return OpenScad("bond([{0},{1},{2}],[{3},{4},{5}],r={6});\n".format(*s1,*s2,r))

    def sphere(self, r=1):
        return OpenScad("sphere(r={0});\n".format(r))

    def __str__(self):
        return self.string
    
def test():
    o = OpenScad()
    print(o.sphere(r=5).translate([1,2,3]))
    print(o.add(o.sphere(r=2), o.sphere(r=3)))
    print(o.sphere(r=2).add(o.sphere(r=3)).add(o.sphere(r=4))) #another way







def run(lattice, water_type="TIP3P", guests=[]):
    """
    cell is in nm

    openscad2 comes up with OO style
    """
    logger = logging.getLogger()
    for d in range(3):
        lattice.rep[d] += 2  #Extend the size,then cut off later.

    lattice.stage1()   #replicate the unit cell
    lattice.stage2()   #prepare random graph

    scale=50
    roxy=0.07
    rbond=0.06
    logger.info("Output water molecules in OpenSCAD format revised.")
    rep = np.array(lattice.rep)
    trimbox    = lattice.cell *np.array([(rep[i]-2) for i in range(3)])
    trimoffset = lattice.cell[0]+lattice.cell[1]+lattice.cell[2]

    margin = 0.2 # expansion relative to the cell size
    lower = (1.0 - margin) / rep
    upper = (rep - 1.0 + margin) / rep

    bonds = []
    for i,j in lattice.graph.edges_iter(data=False):
        s1 =lattice.reppositions[i]
        s2 =lattice.reppositions[j]
        d = s2-s1
        d -= np.floor( d + 0.5 )
        logger.debug("Len {0}-{1}={2}".format(i,j,np.linalg.norm(d)))
        s2 = s1 + d
        if ( (lower[0] < s1[0] < upper[0] and lower[1] < s1[1] < upper[1] and lower[2] < s1[2] < upper[2] ) or
            (lower[0] < s2[0] < upper[0] and lower[1] < s2[1] < upper[1] and lower[2] < s2[2] < upper[2] ) ):
            bonds.append( (np.dot(s1,lattice.repcell), np.dot(s2,lattice.repcell)))

    nodes = []
    for s1 in lattice.reppositions:
        if lower[0] < s1[0] < upper[0] and lower[1] < s1[1] < upper[1] and lower[2] < s1[2] < upper[2]:
            nodes.append( np.dot(s1, lattice.repcell) )

    o = OpenScad()
    objs = [o.sphere(r="Roxy").translate(node) for node in nodes] + [o.bond(s1,s2,r="Rbond") for s1,s2 in bonds]
    #operations
    ops = [bondfunc,
        o.defvar("$fn", 20),
        o.defvar("Roxy", roxy),
        o.defvar("Rbond", rbond),
        ( o.rhomb(trimbox).translate(trimoffset) & o.add(*objs) ).translate(-trimoffset).scale([scale,scale,scale])]
    s = o.encode(*ops)
    s = '//' + "\n//".join(lattice.doc) + "\n" + s
    print(s,end="")
