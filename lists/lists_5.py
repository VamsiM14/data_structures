# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 09:43:09 2022

@author: hp

Implement a function findMinimum(lst) which finds the smallest number in the given list.

Input:#
A list of integers

Output:#
The smallest number in the list

Sample Input#
arr = [9,2,3,6]
Sample Output#
2

"""

def find_minimum(arr):
    if len(arr) == 0:
        return None
    
    minValue = arr[0]
    for i in range(len(arr))[1:]: # iterating over the length of array
        if arr[i] < minValue:
            minValue = arr[i]
            
    return minValue

print(find_minimum([5,56,767]))
