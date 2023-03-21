# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:58:21 2022

Makes sure that all files in folder have the Num_MM-DD-YYYY_Fluency_En format
by checking the presence of dashes and underscores.

Output: An array of all files with incorrect formatting.

@author: david
"""
"""
Simple companion code to folder-to-excel that verifies that all files are formatted appropriately for both the aforementioned code and any future automtion purposes
"""
import os

files = os.listdir(r'')

check_files = []

for obj in files:
    count_dash = 0
    count_under = 0
    
    if obj[6] != "_":
        check_files.append(obj)
    elif obj[9] != "-":
        check_files.append(obj)
    elif obj[12] != "-":
        check_files.append(obj)
    elif obj[17] != "_":
        check_files.append(obj)
    elif obj[25] != "_":
        check_files.append(obj)

print(check_files)

    
    
