# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:09:52 2021

@author: Envy-W10
"""

def fibonacci (n):
    a, b= 0,1
    for i in range (0,n,1):
        print (a,end =" ")
        a,b=b,a+b
