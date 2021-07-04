# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:22:06 2021

@author: Envy-W10
"""

try:
    x=int(input("Ingrese un numero:"))
    y=1/x
    print (y)
except ZeroDivisionError:
    print ("mija ponte 11")
except ValueError:
    print ("Meta un enterof")
except:
    print ("Mija no se que pasa")
print ("THE END")
