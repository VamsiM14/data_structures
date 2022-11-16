# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:03:24 2022

@author: hp

Problem Statement#
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

Input:#
A list of numbers (could be floating points or integers)

Output:#
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input#
arr = [1,2,3,4]
Sample Output#
arr = [24,12,8,6]

Algo:
    -> traverse through the input list using a for loop:
        -> for every element in the list return a product of all other elements by re-traversing again using a 2nd for loop:
    
    -> This appears more like a brute force algo.. will comeback after implementing this for a refinement
"""
import timeit 


def giveProductOfAllExceptSelf(lst):
    resultOuter = []
    for indexOuter in range(len(lst)):
        resultInner = 1
        for indexInner in range(len(lst)):
            if indexInner != indexOuter:
                resultInner *= lst[indexInner]
        resultOuter.append(resultInner)
    return resultOuter

print('1:', timeit.timeit(lambda:giveProductOfAllExceptSelf([1,2,3,4])))

''' 
New Algo with No nested loops:
-> first calculate product on left
-> then on right
'''
def giveProductOfAllExceptSelfNew(lst):
    left = 1
    right = 1
    product = []
    
    for ele in lst:
        product.append(left)
        left = left*ele
        
    for index in range(len(lst)-1, -1, -1):
        product[index] *= right
        right *= lst[index]
        
    return product

print('2:', timeit.timeit(lambda:giveProductOfAllExceptSelfNew([1,2,3,4])))
                
