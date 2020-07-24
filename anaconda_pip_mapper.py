# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:18:11 2020

@author: Garrett
# To get anaconda env use: conda list -e > requirements.txt
# Note can only map envs within the same os system (e.g. can map windows package versions to linux package versions)
# https://beta.deepnote.com/

This python script can be used to map anaconda environments to pip environments for loading into deepnote.
"""
#%% Packages & Data
import re

read = r"C:\Users\Garrett\requirements.txt"
write = r"C:\Users\Garrett\requirements2.txt"
#%%
with open(read, 'r') as file:
    data = file.read()
    
test = re.sub(r'[=]{1}[^=]*\n', '\n', data)
test = re.sub(r'=', '==', test)

with open(write, 'w') as file:
    file.write(test)
