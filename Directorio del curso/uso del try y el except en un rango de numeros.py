# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:11:29 2021

@author: Envy-W10
"""

def readint(prompt, min, max):
    while (True):
        try:
            print("Ingrese un valor entre", min, "y", max)
            x=int (input(prompt))
            assert x>= min and x<=max
            return x
        except ValueError:
            print ("Pon solo Números")
        except:
            print ("Error el valor debe estar dentro del rango ")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)




