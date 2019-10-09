#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:53:46 2019

@author: joaobarboza
"""

class Pagtos(object):
    
    def __init__(self,CPF = "" , VALOR = 0 , CODE = 0):
        self.cpf = CPF
        self.valor = VALOR
        self.code = CODE
        
    def get_cpf(self):
        return self.cpf
    
    def get_valor(self):
        return self.valor
    
    def get_code(self):
        return self.code
    
    def set_cpf(self,x):
        self.cpf = x
        return self
    
    def set_valor(self,x):
        self.valor = x
        return self
    
    def set_code(self,x):
        self.code = x
        return self
    
class Alimentacao(Pagtos):
    
    def __init__(self,CPF = " " , VALOR = 0 , CODE = 0 , DESCRICAO = " " ):
        Pagtos.__init__(self,CPF,VALOR,CODE)
        self.descricao = DESCRICAO
        self.valor_faturaa = VALOR*1.12
        Historico.set_pagamento_historico_Alimenticia(H1,self)
        
    def get_descricao(self):
        return self.descricao
    
    def get_valor_faturaa(self):
        return self.valor_faturaa
    
    def set_descricao(self,x):
        self.descricao = x
        return self
    
    def set_valor_faturaa(self,x):
        self.valor_faturaa = x
        return self
    
class Saude(Pagtos):
    
    def __init__(self,CPF = " " , VALOR = 0 , CODE = 0 , ESTABELECIMENTO = " "):
        Pagtos.__init__(self,CPF,VALOR,CODE)
        self.estabelecimento = ESTABELECIMENTO
        self.valor_faturas = VALOR*1.05
        Historico.set_pagamento_historico_Saude(H1,self)
        
    def get_estabelecimento(self):
        return self.estabelecimento
    
    def get_valor_faturas(self):
        return self.valor_faturas
    
    def set_estabelecimento(self,x):
        self.estabelecimento = x
        return self
    
    def set_valor_faturas(self,x):
        self.valor_faturas = x
        return self.valor_faturas
    
class Historico(object):
    
    def __init__(self , dict1 = {}):
        self.dict = dict1
        
    def get_historico(self):
        return self.dict
    
    def set_pagamento_historico_Saude(self,pagamento):
        Historico.get_historico(self)[pagamento] = {'Modalidade de venda':'saude','CPF':Pagtos.get_cpf(pagamento),'VALOR':Pagtos.get_valor(pagamento) , 'CODE':Pagtos.get_code(pagamento) , 'valor fatura':Saude.get_valor_faturas(pagamento), 'estabelecimento':Saude.get_estabelecimento(pagamento)}
        return self.dict
    
    def set_pagamento_historico_Alimenticia(self,pagamento):
        Historico.get_historico(self)[pagamento] = {'Modalidade de venda':'alimenticia','CPF':Pagtos.get_cpf(pagamento),'VALOR':Pagtos.get_valor(pagamento) , 'CODE':Pagtos.get_code(pagamento) , 'valor fatura':Alimentacao.get_valor_faturaa(pagamento) ,'Descricao':Alimentacao.get_descricao(pagamento) }
    
    def relatorio(self):
        for x in Historico.get_historico(self):
            print(str(x) + ":" + str(Historico.get_historico(self)[x]))
            
H1 = Historico()
