# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:14:46 2021

@author: zainab
"""

#%%
def problem3_3(month, day, year):
   
    months = ("January","February","March","April","May","June","July","August","September","October","November","December")
    month = int(month-1)
    day = str(day)
    day_mon = (day+",")
    print(months[month], day_mon,year)
      
      
#%%