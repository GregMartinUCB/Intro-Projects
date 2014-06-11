# -*- coding: utf-8 -*-
"""
Created on Thu May 22 18:35:01 2014

"""
from sympy import *
from sympy.mpmath import *
"""
Just creating arrays of points.
"""
i=np.random.randint(10,size=(10,2))
line=np.array([[0,1.1],[1,2.9],[2,4.5],[3,7.5],[4,9.1],[5,11.1],[6,12.3],[7,15.8],[8,16.1],[9,19.9]])

"""
Declaring some variables
"""
m,b=var("m,b")

"""
Defining the linear fit equation
"""
def E(a,m,b):
    total =0
    for n in range(10):
        total= total+ ((a[n,1]-(m*a[n,0]+b))**2)/2
        print total
    print total
    return total
    
"""
Initializing said equation with the array of points Then taking the 
darivative.
"""
em= E(line,m,b).diff(m)

eb= E(line,m,b).diff(b)
print em
print eb


a= solve([em,eb],[m,b])
print a



def plotE(mb):
    for point in range(len(line)):
        scatter(line[point,0],line[point,1])
    slope = float(mb[m])
    intercept = float(mb[b])
    x=np.arange(0,10,1)
    y=slope*x + intercept
    plt.plot(x,y)
    plt.title("Solved Exactly")

plotE(a)


"""
*******************************************************************************
*Now we shall use gradient slope decent.
*******************************************************************************
"""
def Evaluate(m_1,b_1):
    for_m=em.subs(m,m_1).evalf()
    Initial_em= for_m.subs(b,b_1).evalf()
    
    for_b=eb.subs(m,m_1).evalf()
    Initial_eb= for_b.subs(b,b_1).evalf()
    
    Gradient=[Initial_em,Initial_eb] 
    
    return Gradient

print Evaluate(0,0)

def Raise_Lower(m_1,b_1,n):
    if Evaluate(m_1,b_1)[0]<0:
        #print Evaluate(m_1,b_1)[0] 
        m_1=m_1+1/n**.5
          
    else:
        m_1=m_1-1/n**.5
        
    if Evaluate(m_1,b_1)[1]<0:
        #print Evaluate(m_1,b_1)[1]
        b_1=b_1+1/n**.5
    else:
        b_1=b_1-1/n**.5
    
    return [m_1,b_1]

def Decend(m_1,b_1):

    n=1
    while Evaluate(m_1,b_1)!=[0,0]:
        #print m_1,b_1
        print Evaluate(m_1,b_1)

        m_1=Raise_Lower(m_1,b_1,n)[0]
        b_1=Raise_Lower(m_1,b_1,n)[1]
        
        n= n+1
        
        if n>700:
            return [m_1,b_1]
            break


print Decend(0,0)
    


