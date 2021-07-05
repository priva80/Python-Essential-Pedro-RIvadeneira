# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 17:02:46 2021

@author: Envy-W10
"""
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
def DiadelAno(day,month,year):
    counter=0
    for m in range (1, month):
        counter +=  daysInMonth(year, m)
    counter+=day 
    return counter 

testYears = [2020, 2020, 2016, 1987]

testMonths = [3, 12, 1, 11]

testDays = [5, 29, 31, 30]

testResults=[65,364,31,334]

for i in range(len(testYears)):

                year = testYears[i]

                month = testMonths[i]
                
                day=testDays[i]

                print(day,month,year,"->", end="")

                result = DiadelAno(day,month,year)

                if result == testResults[i]:

                                print("OK")

                else:

                                print("Failed")
while True: 
    try:                               
        print("\nBienvenido\nEste programa le dirá el número de día que corresponde la fecha seleccionada\n")
        d,m,y =input("Ingrese un día, un mes y un año (Utilice solo números ejemplo: 2,12,2020): ").split(",")
        d= int (d)
        y = int(y)
        m = int(m)
        print (DiadelAno(d,m,y))
    except:
        None 
        