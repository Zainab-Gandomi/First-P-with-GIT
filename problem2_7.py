# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:11:18 2021

@author: zainab
"""

#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a = float(input("Enter of side one: "))
    b = float(input("Enter of side one: "))
    c = float(input("Enter of side one: "))
    s = 0.5* (a+b+c)
    x = s * (s-a) * (s-b) * (s-c)
    area = x**0.5
    print("Area of a triangle with sides",a,b,c,"is", area)
#%%