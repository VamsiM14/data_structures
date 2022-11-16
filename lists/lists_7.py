# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 12:33:19 2022

@author: hp

Problem Statement#
Implement a function find_second_maximum(lst) which returns the second largest element in the list.

Input:#
A List

Output:#
Second largest element in the list

Sample Input#
[9,2,3,6]
Sample Output#
6

Algo:
    ->lst.sort()[-2]
"""

def find_second_maximum(lst):
    max = float('-inf')
    secondmax = float('-inf')
    for val in lst:
        if val > max:
            secondmax = max
            max = val
        elif val > secondmax:
            secondmax = val
    return secondmax

print(find_second_maximum([9,2,3,6]))

