# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:14:18 2019

@author: Ahmad
"""

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import matplotlib.pyplot as plt


class Rumgeom:
    def __init__(self):
        vec = Vector(2, 5, 3)
        vec.draw()
        
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.quiver(0, 0, 0, self.x, self.y, self.z)
        
        ax.set_xlim([-self.x, self.x])
        ax.set_ylim([-self.y, self.y])
        ax.set_zlim([-self.z, self.z])
        plt.show()
    
    def get_length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def scale(self, n):
        self.x *= n
        self.y *= n
        self.z *= n
        
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def draw(self):
        pass
    
class Line:
    def __init__(self, point, vector):
        self.point = point
        self.vector = vector
        
    def draw(self):
        pass
    
class Plane:
    def __init__(self, point, vector_1, vector_2):
        self.point = point
        self.vector_1 = vector_1
        self.vector_2 = vector_2
        
    def draw(self):
        pass
    
    def get_normal(self):
        x
        
    
Rumgeom()