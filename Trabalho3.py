#!/usr/bin/env python3
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
    
    def __init__(self , z = 0, Module = 0):
        
        self.z = int(z)
        
    def Create(self):
        
        self.x = int(input("Digite o valor de x:"))
        self.y = int(input("Digite o valor de y:"))
        self.z = int(input("Digite o valor de z:"))
        return self

#Getters
        
    def get_x(self):
        print(str(self.x))
        return self.x
   
    def get_y(self):
        print(str(self.y))
        return self.y
    
    def get_z(self):
        print(str(self.z))
        return self.z
    
    def get_module(self):
        print(self.Module)

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
    
#Modulo
    
    def Module1(self):
        self.Module = math.sqrt( ((int(self.x))**2) + ((int(self.y))**2) + ((int(self.z))**2) )
        print (str(self.Module))
        
