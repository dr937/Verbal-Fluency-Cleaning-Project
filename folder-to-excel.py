# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:32:36 2022

@author: david
"""

import os
import pandas as pd

files = os.listdir(r'C:\Users\david\PROJECTS\Item-Level Data Project - WHICAP\Verbal Fluency English AT')

ids = []
dates = []

for obj in files:
    labels = obj.split("_")
    ids.append(labels[0])
    dates.append(labels[1])
    

comb_dict = {'Subject ID': ids, 'Date': dates}

df = pd.DataFrame(comb_dict)

df.to_csv(r'C:\Users\david\PROJECTS\Item-Level Data Project - WHICAP\fluency.csv', header=True, index = False)
    
    
