#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:16:44 2019

@author: joaobarboza
"""

#FILA

class FILA(object):
    
    def __init__(self,list_1 = []):
        self.fila = list_1
        
    def get_fila(self):
        return self.fila
    
    def set_fila(self,x):
        self.fila = x
        return self
    
    def take_element(self):
        if not self.fila:
            print( " A fila esta vazia " )
        else:
             print (self.fila[-1:])
             self.fila.pop(-1)
        
    def insert_element(self,x):
        self.fila.insert(0,x)
        
    def printing(self):
        for x in self.fila:
            print( str(x) + " -> ")
