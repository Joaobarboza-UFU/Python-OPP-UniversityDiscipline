#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:40:45 2019

@author: joaobarboza
"""

class funcionario(object):
    
    def __init__(self, nome = " ", codigo = " ", salario = 1000 , escolaridade = 0):
        self.nome = nome
        self.codigo = codigo
        self.salario = salario
        self.escolaridade = escolaridade
        
    def get_nome(self):
        return self.nome
   
    def get_codigo(self):
        return self.codigo
    
    def get_escola(self):
        return self.escola
    
    def get_colegio(self):
        return self.colegio
    
    def get_universidade(self):
        return self.universidade
    
    def get_curso(self):
        return self.curso
        
    def get_salario(self):
        return self.salario
    
    def get_escolaridade(self):
        return self.escolaridade
        
        
    def print_info_funcionario(self):
        print("Dados do funcionario:")
        print("Nome = " + str(self.nome))
        print("Codigo = " + str(self.codigo))
        print("Salario = " + str(self.salario))
    

class funcionario_ensinobasico(funcionario):
    
    def __init__(self, nome = " ", codigo = " ",escola = " ",salario = 1100,escolaridade = 1):
        funcionario.__init__(self, nome , codigo , salario, escolaridade)
        self.escola = escola
        
    def print_info_funcionarioB(self):
        print("Dados do funcionario:")
        print("Nome = " + str(self.nome))
        print("Codigo = " + str(self.codigo))
        print("Salario = " + str(self.salario))
        print("Escola = " + str(self.escola))
        
class funcionario_ensinomedio(funcionario_ensinobasico):
    
    def __init__(self, nome = " ", codigo = " ", escola = " ", colegio = " ",salario = 1500,escolaridade = 2):
        funcionario_ensinobasico.__init__(self, nome, codigo, escola , salario , escolaridade)
        self.colegio = colegio
        
    def print_info_funcionarioM(self):
        print("Dados do funcionario:")
        print("Nome = " + str(self.nome))
        print("Codigo = " + str(self.codigo))
        print("Salario = " + str(self.salario))
        print("Escola = " + str(self.escola))
        print("Escola de conclusao do ensino medio = " + str(self.colegio))

        
class funcionario_ensinosuperior(funcionario_ensinomedio):
    
    def __init__(self, nome = " ", codigo = " ", escola = " ", colegio = " ", universidade = " ", curso = " ",salario = 2000,escolaridade = 3):
        funcionario_ensinomedio.__init__(self, nome , codigo , escola , colegio, salario , escolaridade)
        self.universidade = universidade
        self.curso = curso
        
    def print_info_funcionarioM(self):
        print("Dados do funcionario:")
        print("Nome = " + str(self.nome))
        print("Codigo = " + str(self.codigo))
        print("Salario = " + str(self.salario))
        print("Escola = " + str(self.escola))
        print("Escola de conclusao do ensino medio = " + str(self.colegio))
        print("Universidade = " + str(self.universidade))
        print("Curso = " + str(self.curso))
        
class relatorio(object):
    
    def __init__(self,dict_relatorio = {'Salariototal':0,'SalarioSemEscolaridade':0,'SalarioEnsinoBasico':0,'SalarioEnsinoMedio':0,'SalarioEnsinoSuperior':0}):
        self.dict = dict_relatorio
        
    def get_dict(self):
        return self.dict
        
    def inclusao_funcionario(self,x):
        if funcionario.get_escolaridade(x) == 0:
            relatorio.get_dict(self)['Salariototal'] = relatorio.get_dict(self)['Salariototal'] + 1000
            relatorio.get_dict(self)['SalarioSemEscolaridade'] = relatorio.get_dict(self)['SalarioSemEscolaridade'] + 1000
            return self.dict
        if funcionario.get_escolaridade(x) == 1:
            relatorio.get_dict(self)['Salariototal'] = relatorio.get_dict(self)['Salariototal'] + 1100
            relatorio.get_dict(self)['SalarioEnsinoBasico'] = relatorio.get_dict(self)['SalarioEnsinoBasico'] + 1100
            return self.dict
        if funcionario.get_escolaridade(x) == 2:
            relatorio.get_dict(self)['Salariototal'] = relatorio.get_dict(self)['Salariototal'] + 1500
            relatorio.get_dict(self)['SalarioEnsinoMedio'] = relatorio.get_dict(self)['SalarioEnsinoMedio'] + 1500
            return self.dict
        if funcionario.get_escolaridade(x) == 3:
            relatorio.get_dict(self)['Salariototal'] = relatorio.get_dict(self)['Salariototal'] + 2000
            relatorio.get_dict(self)['SalarioEnsinoSuperior'] = relatorio.get_dict(self)['SalarioEnsinoSuperior'] + 2000
            return self.dict
        else:
            pass
    
    def printar_relatorio(self):
        
        for x in relatorio.get_dict(self):
            print(" O gasto com " + str(x) + "é : " + str(relatorio.get_dict(self)[x]))
        

