# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:12:49 2021

@author: zainab
"""

#%%

import csv 

def problem3_7(csv_pricefile, flower):
    f = open(csv_pricefile)
    
    for row in csv.reader(f):
        if row[0] == flower: 
           print(row[1])
    f.close()
    
    
   
#%%