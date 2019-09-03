import math

class vetor(object):
    #Construtor
    def __init__(self,x = 0,y = 0,x1 = 0,y1 = 0):
        self.X = int(x)
        self.Y = int(y)
        self.X1 = int(x1)
        self.Y1 = int(y1)
    
    #Funcao escalar
    def escalar(self):
        escalaR = ((self.X * self.X1)+(self.Y*self.Y1))
        print (escalaR)
    
    #funcao modulo
    def modulo(self):
        modulO = math.sqrt((self.X**2)+(self.Y**2))
        print (modulO)
    
    #funcao moudulo2
    def modulo2(self):
        modulO = math.sqrt((self.X1**2)+(self.Y1**2))
        print (modulO)
    #funcao angulo em radianos
    def angulo(self):
        angulO = math.acos(((self.X * self.X1)+(self.Y * self.Y1))/((math.sqrt(((self.X)**2)+((self.Y)**2)))*(math.sqrt(((self.X1)**2)+((self.Y1)**2)))))
        print (angulO)
        
    #funcao projecao
    def projecao(self):
        projecax = ((((self.X * self.X1)+(self.Y*self.Y1))/(math.sqrt((self.X**2)+(self.Y**2))**2))* self.X)
        projecay = ((((self.X * self.X1)+(self.Y*self.Y1))/(math.sqrt((self.X**2)+(self.Y**2))**2))* self.Y)
        print (projecax , projecay)
        
    
vet1 = vetor(1,5,4,1)
vet1.escalar()
vet1.modulo()
vet1.modulo2()
vet1.angulo()
vet1.projecao()
