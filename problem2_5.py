# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:50:03 2021

@author: zainab
"""

import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)  # don't remove when you submit for grading
    for i in range(10):
        value = random.randint(1,6)
        print(value)
#%%