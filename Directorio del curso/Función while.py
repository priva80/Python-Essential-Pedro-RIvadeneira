# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:14:52 2021

@author: Envy-W10
"""

contar=int (input ("Ingrese un número para contar:"))
y=1
while y<=contar:
    print (y)
    y=y+1
    print("Dentro de while")
print ("\n","fuera del while")


x=input ("Ingrese un número para contar")
x=int (x)
while True:
    print (y)
    y=y+1# puede escribirse como y+=
    if y>x:
        break
