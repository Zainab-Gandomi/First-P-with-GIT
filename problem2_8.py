# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:23:13 2021

@author: zainab
"""

#%%
def problem2_8(temp_list):
    sum_ = 0
    for i in range(0,len(temp_list)):
       sum_ = sum_ + temp_list[i] 
    
    print("Average:", sum_/len(temp_list))
    print("High:", max(temp_list))
    print("Low:", min(temp_list))
#%%