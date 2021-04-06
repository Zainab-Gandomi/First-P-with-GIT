# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:13:24 2021

@author: zainab
"""

#%%
import random

def problem2_4():
    list1 = []
    random.seed(70)
    for i in range(10):
        value = random.random()
        list1.append(value*5 + 30)
    print(list1) 