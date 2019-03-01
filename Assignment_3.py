#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 00:11:21 2018
#Arash Barmas
#Assignment 3
#Pic 16

@author: arashbarmas
"""

import math
class MathVector:
    def __init__(self,*vec):
        
        if len(vec) == 1:
            if type(vec[0])== int:
                self.vec = [0 for i in range(0,vec[0])]
            else:
                self.vec = [i for i in vec[0]]
        else:
            self.vec = [x for x in list(vec)]
            
    def get_el(self,i):
        return self.vec[i-1]
    def neg(self):
        return MathVector([-x for x in self.vec])
    def mag(self):
        mag=0
        for x in self.vec:
            mag += x**2
        return math.sqrt(mag) 
    def dot(self,other):
        if type(other) == int:
            return MathVector([i*other for i in self.vec])
        else:
            return sum([i*j for i,j in zip(self.vec,other.vec)])
        #if type(other) == MathVector:
            #return sum([i*j for i,j in zip(self.vec,other.vec)])
        #else:
            #return MathVector([i*other for i in self.vec])
    def sp(self,scalor):
        return MathVector([scalor*x for x in self.vec])
    def plus(self,other):
        return MathVector([x+y for x,y in zip(self.vec,other.vec)])
    def print_me(self):
        print self
    def __repr__(self):
        return str(self.vec)
    #magic methods
    def __add__(self,other):
        return self.plus(other)
    def __mul__(self,other):
        return self.dot(other)
    def __neg__(self):
        return self.neg()
    def __getitem__(self,j):
        return self.get_el(j)
    def __abs__(self):
        return self.mag()
    __rmul__=__mul__    
    
    
    
u = MathVector(5)
print "u =",
u.print_me()

v = MathVector([2,3,6])
print "v =",
v.print_me()

v = MathVector((2,3,6))
print "v =",
v.print_me()

w = MathVector(1,2,3)
print "w =",
w.print_me()

print v.get_el(2)
v.neg().print_me()
print v.mag()
print v.dot(w)
v.sp(3).print_me()
v.plus(w).print_me()
w = MathVector(1,2,3)
v = MathVector((2,3,6))

print v
print v[2]
print -v
print abs(v)
print v*w
print v*3
print 3*v
print v+w