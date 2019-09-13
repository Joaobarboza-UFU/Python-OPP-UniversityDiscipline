#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:53:35 2019

@author: joaobarboza
"""

#Estacionamento
#Trabalho 2 
#Joao Barboza Rodrigues
#11811ECP005

class Horario(object):
    
    def __init__(self, Hora = 0 , Minutos = 0 , Segundos = 0):
        self.Hora = Hora
        self.Minutos = Minutos
        self.Segundos = Segundos
        
    def gravacao(self):
        self.Hora = input("Horas:")
        self.Minutos = input("Minutos:")
        self.Segundos = input("Segundos:")
        

    def strHora(self, strTempo = ""):
          self.strTempo = str(self.Hora)+":"+str(self.Minutos)+":"+str(self.Segundos)
          print (self.strTempo)

    def get_Hora(self):
        print (str(self.Hora))
        return self.Hora
    def get_Minutos(self):
        print (str(self.Minutos))
        return self.Minutos
    def get_Segunds(self):
        print (str(self.Segundos))
        return self.Segundos

    def set_Hora(self,x):
        self.Hora = x
        return self.Hora
    def set_Minutos(self,x):
        self.Minutos = x
        return self.Minutos
    def set_Segundos(self,x):
        self.Segundos = x
        return self.Segundos
    
    def adicionar(self, tempoADD):
        self.Hora = (int(tempoADD.Hora) + (int(self.Hora)))
        self.Minutos = (int(tempoADD.Minutos) + (int(self.Minutos)))
        self.Segundos = (int(tempoADD.Segundos) + (int(self.Segundos)))
        return self
    
    def remove(self, tempoADD):
        self.Hora = (int(tempoADD.Hora) - (int(self.Hora)))
        self.Minutos = (int(tempoADD.Minutos) - (int(self.Minutos)))
        self.Segundos = (int(tempoADD.Segundos) - (int(self.Segundos)))
        return self
    
class Estacionamento(object):
    
    def __init__(self, Chapa = "", Marca = "", Entrada = Horario() , Saida = Horario()):
        self.Chapa = Chapa
        self.Marca = Marca
        self.Entrada = Entrada
        self.Saida = Saida
        
    def RegistroCarro(self):
        self.Chapa = input("Placa do carro:")
        self.Marca = input("Marca do carro:")
        
    def InfoCarro(self):
        print ("Placa do carro:" + self.Chapa)
        print ("Marca do carro:" + self.Marca)
        Horario.strHora(self.Entrada)
        Horario.strHora(self.Saida)
        
    def Preco(self):
        Horario.remove(self.Entrada, self.Saida)
        Preco = (int(self.Entrada.Hora) * 7)
        print("O preco a ser pago e:" + str(Preco) + "Reais")
        
            
    def Relatorio(self, veiculo1 , veiculo2 , veiculo3 ,veiculo4 ,veiculo5):
        for i in range (5, 1 , -1):
            if (int(i))==5:
                self = veiculo1
            if (int(i))==4:
                self = veiculo2
            if (int(i))==3:
                self = veiculo3
            if (int(i))==2:
                self = veiculo4
            if (int(i))==1:
                self = veiculo5
            for j in range (5 , 1 , -1):
                     if (int(j))==5:
                        print (self.Chapa)
                     if (int(j))==4:
                        print ( self.Marca)
                     if (int(j))==3:
                        Horario.strHora(self.Entrada)
                     if (int(j))==2:
                        Horario.strHora(self.Saida)
                     if (int(j))==1:
                        Estacionamento.Preco(self)
                
                    
               
