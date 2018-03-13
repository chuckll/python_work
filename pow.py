# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:38:04 2018

@author: chuck
"""

def f(n,x):
    if n==1:
        return x
    else:
        return f(n/2,x)*f(n/2,x)



def m(n,x):
    if n%2 == 1:
       result = x*f(n-1,x)
    else:
       result= f(n,x)
       
    return result       
    
print(str(m(10,2)))