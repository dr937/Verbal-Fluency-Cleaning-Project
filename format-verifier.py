# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:58:21 2022

Makes sure that all files in folder have the Num_MM-DD-YYYY_Fluency_En format
by checking the presence of dashes and underscores.

Output: An array of all files with incorrect formatting.

@author: david
"""

import os

files = os.listdir(r'C:\Users\david\PROJECTS\Item-Level Data Project - WHICAP\Verbal Fluency English AT')

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

    
    
