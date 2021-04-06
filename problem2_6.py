# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:00:39 2021

@author: zainab
"""

#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    for i in range(100):
        first_time = random.randint(1,6)
        second_time = random.randint(1,6)
        print(first_time + second_time)
   
#%%