# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:18:19 2018

@author: chuck
"""

import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)