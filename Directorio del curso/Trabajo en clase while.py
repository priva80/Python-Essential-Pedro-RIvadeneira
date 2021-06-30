# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:43:40 2021

@author: Envy-W10
"""

while True:
    x=input ("Ingrese un número:")
    if x=="q" or x== "quit":
        break
    x= int (x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break 

def hi (name):
    print ("Hi:", name)
hi ("Pedro")
hi ("IKNA")
hi("Antonio")

def Saludo1 (nombre1, nombre2):
    print ("Hola",nombre1)
    print ("Hola", nombre2)
Saludo1("IKna","Pedro")
"""
"""
def dirección (Calle, CódigoPostal, Ciudad):
    print ("Su calle es:","\n ", Calle)
    print ("la código postal es:","\n", CódigoPostal)
    print ("Su ciudad es es:","\n", Ciudad)
A= input ("Ingrese la calle")
B=input ("Ingrese el cógido postal")
C= input ("Ingrese la ciudad")

dirección(A,B,C)    


def resta (a,b):
    print (a-b)
    
resta(5,2)
resta (2,9)
resta(a=2,b=5)
resta (b=5,a=2)
"""
"""
def mult (a,b):
    #print (a*b)
    return (a*b,a-b,a**2)
    

print (mult(6,9))
"""
"""
Milista=["A","B","C"]
def ikna(Milista):
    for a in Milista:
        print("Hola",a)
ikna (Milista)


def crealista (n):
    lista1=[]
    for b in range (n):
        lista1.append(b)
    return lista1
print (crealista(12))


    
    