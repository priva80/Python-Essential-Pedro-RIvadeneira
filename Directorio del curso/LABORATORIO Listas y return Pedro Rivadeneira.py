# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 13:23:00 2021

@author: Envy-W10
"""
#Nombre:Pedro Rivadeneira
def isYearLeap(year):
    if year%4==0 and year%100!=0:
        return True 
    elif year%400==0:
        return True
    else:
        return False
    
    
    
    
    
testDat=[1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testDat)):

    yr = testDat[i]

    print(yr,"->",end="")

    result = isYearLeap(yr)

    if result == testResults[i]:

        print("OK")

    else:

        print("Failed")
        
while True:  
    print ("\nBienvenido \nEste programa le ayudara a verificar si un año es bisiesto")

    try:
        x=int(input("Ingrese un año o presione 0 para salir: "))
        print(isYearLeap(x))
        if x==0: break 
    except:
      print ("Ingrese bien los valores")
      