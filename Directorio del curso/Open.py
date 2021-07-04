# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:11:58 2021

@author: Envy-W10
"""
list=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()#Strip es para quitar algo
    print (item)
    list.append(item)
    
file.close()
print(list)