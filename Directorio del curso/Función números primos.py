# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:04:30 2021

@author: Envy-W10
"""
def isPrime(x):
       if x < 2:
           return False
       elif x==2:
           return True
       for n in range (2, x):
           if x % n == 0:
               return False
       return True
m=int(input("Ingrese un número:"))
print(isPrime (m))
