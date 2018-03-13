# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:29:03 2018

@author: chuck
"""
def fad(n):
    if n==0:
        return 1
    else:
        return n*fad(n-1)
    
print(str(fad(3)))