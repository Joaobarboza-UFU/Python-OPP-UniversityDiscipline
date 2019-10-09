#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:53:25 2019

@author: joaobarboza
"""
import math

class NumComplexo(object):
    
    def __init__(self,real = 0,imaginario = 0 ):
        self.real = real
        self.imaginario = imaginario
        
    def get_parte_real(self):
        return self.real
    
    def get_parte_imaginario(self):
        return self.imaginario
    
    def soma_complexos(self,num1 , num2):
        self.real = NumComplexo.get_parte_real(num1) + NumComplexo.get_parte_real(num2)
        self.imaginario = NumComplexo.get_parte_imaginario(num1) + NumComplexo.get_parte_imaginario(num2)
        return self
        
    def produto_complexos(self,num1,num2):
        self.real = (((NumComplexo.get_parte_real(num1))*(NumComplexo.get_parte_real(num2))) - ((NumComplexo.get_parte_imaginario(num1))*(NumComplexo.get_parte_imaginario(num2))))
        self.imaginario =  (((NumComplexo.get_parte_real(num1))*(NumComplexo.get_parte_imaginario(num2))) + ((NumComplexo.get_parte_imaginario(num1))*(NumComplexo.get_parte_real(num2))))
        return self 
    
    def modulo_complexo(self):
        modulo = math.sqrt((self.real**2)+(self.imaginario**2))
        return modulo
    
    def argumento_complexo(self):
        argumento = math.acos((self.real)/(NumComplexo.modulo_complexo(self)))
        return argumento
    
    def forma_polar(self):
        print((str(NumComplexo.modulo_complexo(self)) + "(cos" + str(NumComplexo.argumento_complexo(self)) + " + i . sen" + str(NumComplexo.argumento_complexo(self)) + ")"))
        
    # Num1 = NumComplexo(1,1)
    # Num2 = NumComplexo(3,-1)
    # Num3 = NumComplexo(0,0)
    # NumComplexo.soma_complexos(Num3,Num1,Num2)
    # <__main__.NumComplexo at 0x11e23a5f8>
    # NumComplexo.forma_polar(Num3)
    # 4.0(cos0.0 + i . sen0.0)
    # NumComplexo.produto_complexos(Num3,Num1,Num2)
    # <__main__.NumComplexo at 0x11e23a5f8>
    # NumComplexo.forma_polar(Num3)
    # 4.47213595499958(cos0.46364760900080615 + i . sen0.46364760900080615)
        
