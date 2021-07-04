# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 11:53:48 2021

@author: Envy-W10
"""
#FUNCIONES 1 Pedro Rivadeneira
def l100kmtompg(x):
    x=x/3.785411784
    resultado=62.13711922373339/x
    print ("\n El resultado es: ",resultado,"millas sobre galón \n")
def mpgtol100km (x):
    resultado=((100/1.609344)/(x/3.785411784))
    print ("\n El resultado es: ", resultado, "litros sobre 100km \n")
"""
l100kmtompg(3.9)
l100kmtompg(7.5)
l100kmtompg(10.)
mpgtol100km(60.3)
mpgtol100km(31.4)
mpgtol100km(23.5)
"""
while True:
    print("Bienvenido,\n Presione 1 si desea convertir litros sobre 100km a millas sobre galón \n Presione 2 si desea convertir de millas sobre galón a litros sobre 100km \n Presione 0 para salir ")
    
    y=int(input("Ingrese únicamnete los valores indicados anteriormente: "))
    if y==1:
            x=float(input("Ingrese el valor a convertir de litros sobre 100 km a millas sobre galón: "))
            l100kmtompg(x)
    elif y==2:
            x=float(input("Ingrese el valor a conveti de millas sobre galón a litros sobre 100 km: "))
            mpgtol100km(x)
    elif y==0: 
        break  
    else:
        print ("\n ERROR: Ingrese unicamente los valores indicados \n ")
    
   
    
    