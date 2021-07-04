# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:35:38 2021

@author: Envy-W10
"""

file=open("devices.txt","a")
while True:
    newitem=input("Ingrese un nuevo dispositivo: ")
    if newitem=="exit":
        print ("All done")
        break 
    
    file.write(newitem+"\n")
file.close()