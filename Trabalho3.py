# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:04:12 2019

@author: joaobarboza
"""

#Trabalho 2 
#POO
#Joao Barboza Rodrigues
#11811ECP005

import math

class vetor2D(object):
    
    def __init__(self, x = 0, y = 0):
        self.x = int(x)
        self.y = int(y)
    
class vetor3D(vetor2D):
    
    def __init__(self ,x = 0, y =0 , z = 0, Module = 0):
        vetor2D.__init__(self, x, y)
        self.z = int(z)
        

#Getters
        
    def get_x(self):
        return self.x
   
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z
    
    def get_module(self):
        return self.Module

#Setters
        
    def set_x(self , x):
        self.x = x
        return self.x
    
    def set_y(self , y):
        self.y = y
        return self.y
    
    def set_z(self , z):
        self.z = z
        return self.z
    
#ModulO
    
    def Module1(self):
        self.Module = math.sqrt( ((int(self.x))**2) + ((int(self.y))**2) + ((int(self.z))**2) )
        print (str(self.Module))
        

#Produto Vetorial
        
    def Produto(self,x,y):
        self.x = (((vetor3D.get_y(x))*(vetor3D.get_z(y)))-((vetor3D.get_z(x))*(vetor3D.get_y(y))))
        self.y = (((vetor3D.get_z(x))*(vetor3D.get_x(y)))-((vetor3D.get_x(x))*(vetor3D.get_z(y))))
        self.z = (((vetor3D.get_x(x))*(vetor3D.get_y(y)))-((vetor3D.get_y(x))*(vetor3D.get_x(y))))
        return self
        
    
    
        
