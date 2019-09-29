# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:30:45 2019

@author: joaobarboza
"""

class funcionario(object):
    
    def __init__(self, nome = " ", codigo = " ", escolaridade = 0, salario = 1000):
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
    
    def aux_relatorio(self , x , y , z , k , w):
        i = self.escolaridade
        j = self.salario
        if i == 0:
            y = y + j
            x = x + j
            return x , y
        if i == 1:
            z = z + j
            x = x + j
            return x ,z
        if i == 2:
            k = k + j
            x = x + j
            return x , k
        if i == 3:
            w = w + j
            x = x + j
            return x , w
        return self
        
        
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
        funcionario_ensinobasico.__init__(self, nome, codigo,salario , escola)
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
        funcionario_ensinomedio.__init__(self, nome , codigo ,salario , escola , colegio)
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
        
def relatorio(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,salariototal = 0 , salariobasico = 0 ,salariofund = 0 , salariomedio = 0 , salariosup = 0):
        funcionario.aux_relatorio(x1 , salariototal , salariobasico, salariofund , salariomedio , salariosup)
        funcionario.aux_relatorio(x2 , salariototal , salariobasico, salariofund , salariomedio , salariosup)
        funcionario.aux_relatorio(x3 , salariototal , salariobasico, salariofund , salariomedio , salariosup)
        funcionario.aux_relatorio(x4 , salariototal , salariobasico, salariofund , salariomedio , salariosup)
        funcionario.aux_relatorio(x5 , salariototal , salariobasico, salariofund , salariomedio , salariosup)
        funcionario.aux_relatorio(x6 , salariototal , salariobasico, salariofund , salariomedio , salariosup)
        funcionario.aux_relatorio(x7 , salariototal , salariobasico, salariofund , salariomedio , salariosup)
        funcionario.aux_relatorio(x8 , salariototal , salariobasico, salariofund , salariomedio , salariosup)
        funcionario.aux_relatorio(x9 , salariototal , salariobasico, salariofund , salariomedio , salariosup)
        funcionario.aux_relatorio(x10 , salariototal , salariobasico, salariofund , salariomedio , salariosup)
        print ("Relatorio de custos da empresa:")
        print ("___________________________________________________________")
        print ("Custo total: " + str(salariototal))
        print ("___________________________________________________________")
        print ("Custo funcionários sem escolaridade: " + str(salariobasico))
        print ("___________________________________________________________")
        print ("Custo funcionários que concluiram o ensino básico:" + str(salariofund))
        print ("___________________________________________________________")
        print ("Custo funcionários que concluiram o ensino médio:" + str(salariomedio))
        print ("___________________________________________________________")
        print ("Custo funcionários que concluiram o ensino superior:" + str(salariosup))

