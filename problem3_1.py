# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:47:59 2021

@author: zainab
"""

#%%
def problem3_1(txtfilename):
    line_len = 0
    text_file = open(txtfilename)     
    
    for line in text_file:         
        print(line , end = "")
        
        line_len = line_len + len(line)
    print()
    print()    
    print("There are",line_len,"letters in the file.")
    text_file.close()  
#%%