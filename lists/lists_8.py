# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:47:34 2022

@author: hp

Problem Statement#
Implement a function right_rotate(lst, k) which will rotate the given list by k. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.

Input#
A list and a positive number by which to rotate that list

Output:#
The given list rotated by k elements

Sample Input#
lst = [10,20,30,40,50]
k = 3
What if the given input k is greater than the length of the lst?

Sample Output#
lst = [30,40,50,10,20]

Algo:
    -> 
    
    
[1, 2, 3, 4, 5], 2
[300, -1, 3, 0], 3
[0, 0, 0, 2], 2
['right', 'rotate', 'python'], 4
[], 1
['13', 'a', 'Python'], 3
"""

def right_rotate(lst, k):
    new_lst = lst[:]
    i = 0
    while (i+k <= len(lst)-1):
        new_lst[i+k] = lst[i]
        i += 1
        
    while (i+k >= len(lst)-1 and i < len(lst)):
        rem = (i+k)-(len(lst)-1)
        while (rem > len(lst)):
            rem = rem - len(lst)
        
        new_lst[rem-1] = lst[i]
        i += 1
        
    return new_lst

print(right_rotate(['right', 'rotate', 'python'], 4))