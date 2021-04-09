# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:36:41 2021

@author: zainab
"""
#%%
import random
ran_list = []
random.seed(150)
for i in range(0,25):
    ran_list.append(round(100*random.random(),1))


    def  problem4_2 (ran_list) :
        import statistics
        print(statistics.mean(ran_list))
        print( statistics.stdev(ran_list))
        
    
    
#%%