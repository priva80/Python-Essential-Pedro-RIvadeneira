# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:24:28 2021

@author: Envy-W10

"""
#Pedro Rivadeneira
def isYearLeap(year):
    if year%4==0 and year%100!=0:
        return True 
    elif year%400==0:
        return True
    else:
        return False
        
def daysInMonth(year,month):
    data= {
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
        }
    if 0>=month or month>12:
            None
    if isYearLeap(year) and month == 2:
        return data[month] + 1
    return data[month]
  
testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):

                year = testYears[i]

                month = testMonths[i]

                print(year, month, "->", end="")

                result = daysInMonth(year, month)

                if result == testResults[i]:

                                print("OK")

                else:

                                print("Failed")
while True: 
    try:                               
        print("\nBienvenido\nEste programa le dirá el número de días que tiene el mes elegido\n")
        y, m =input("Ingrese un año y un mes (Utilice solo números ejemplo: 2020,12): ").split(",")
        y = int(y)
        m = int(m)
        print (daysInMonth(y,m))
    except:
        None 
   

