# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 22:34:18 2022

@author: hp

Problem Statement#
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number, the 1st index will have the smallest, and the 2nd index will have second-largest, and so on. In other words, all the even-numbered indices will have the largest numbers in the list in descending order and the odd-numbered indices will have the smallest numbers in ascending order.

Input:#
A sorted list

Output:#
A list with elements stored in max/min form

Sample Input#
lst = [1,2,3,4,5]
Sample Output#
lst = [5,1,4,2,3]

"""
#from math import ceil

def max_min(lst):
    lst_max = lst[len(lst)//2:]
    lst = lst[:len(lst)//2]
    max_index = 0
    for i in range(len(lst_max)-1,-1,-1):
        lst.insert(max_index, lst_max[i])
        max_index +=2
    return lst

print(max_min([1,2,3,4,5]))

