#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:13:21 2019

@author: joaobarboza
"""

# Aula POO 15 de Outubro de 2019
# Pilhas

class pilha(object):
    
    def __init__(self,pilha=[]):
        self.pilha = pilha
        
    def insert(self,valor):
        self.pilha.append(valor)
        print (self.pilha)
        
    def remove(self):
        try:
            self.pilha.pop()
            print(self.pilha)
        except IndexError:
            print("pilha vazia")
            
    def imprimir(self):
        print (self.pilha)
        

            

        
