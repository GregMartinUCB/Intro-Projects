# -*- coding: utf-8 -*-
"""
Created on Fri May 30 12:04:58 2014

@author: keamoke
"""

from sympy import Symbol
from sympy import symbols
from numpy import array
from sympy import diff
from sympy import Matrix
from sympy import Derivative


 
def randomImage():
    return array([[0+ np.random.randint(0,20),50+ np.random.randint(0,20),150+ np.random.randint(0,20),200+ np.random.randint(0,20)],
          [50+ np.random.randint(0,20),100+ np.random.randint(0,20),150+ np.random.randint(0,20),200+ np.random.randint(0,20)],
          [150+ np.random.randint(0,20),150+ np.random.randint(0,20),200+ np.random.randint(0,20),230+ np.random.randint(0,20)],
          [200+ np.random.randint(0,20),200+ np.random.randint(0,20),230+ np.random.randint(0,20),235+ np.random.randint(0,20)]])
         
img=randomImage()
img2=randomImage()
img3=randomImage()
img4=randomImage()
img5=randomImage()
img6=randomImage()

plot_image=imshow(img,cmap='gray')



fimage =array([img.flatten(),img2.flatten(),img3.flatten(),img4.flatten(),img5.flatten(),img6.flatten()])

print fimage

class Neuron():
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16=symbols('x1,x2,x3,x4,x5,x6,x7,x8,x9x,10,x11,x12,x13,x14,x15,x16')
    
    phi=array([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16])

    def __init__(self,imgSet):
        self.imgSet=imgSet
        
        
    
    def Objective(self):
        objectiveSum=[]
        
        for i in range(len(self.imgSet)):
            objectiveSum.append([(self.imgSet[i]-self.phi)**2/2])
            
        
        
        return array(objectiveSum)
        
        
        
    def GradientObjective(self,n):
        
        objective=self.Objective()[n]
        print diff(self.x1,self.phi[0])
        imageGradient=[diff(objective, self.phi[0])]
        
        
        #for i in self.phi:
            
            #print i
            #imageGradient.append(diff(objective,i))
            
       
    
        return array(imageGradient)
    
   # def Learning(self,phi):
        
        
    

neuron1=Neuron(fimage)

print neuron1.imgSet


#print neuron1.Objective()
print neuron1.GradientObjective(0)