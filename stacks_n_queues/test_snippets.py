# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:33:22 2022

@author: hp
"""

z = set('abc')
z.add('san')
z.update(set(['p', 'q']))
print(z)