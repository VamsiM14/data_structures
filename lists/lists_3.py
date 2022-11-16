# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:29:00 2022

@author: hp

Challenge 3: Find Two Numbers that Add up to "k"
Given a list and a number "k", find two numbers from the list that sum to "k".

Problem Statement#
In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k.

Input#
A list and a number k

Output#
A list with two integers a and b that add up to k

Sample Input#
lst = [1,21,3,14,5,60,7,6]
k = 81
Sample Output#
lst = [21,60]
For example, in this illustration, we are given 81 as the number k and when we traverse the whole list we find that 21 and 60 are the integers that add up to 81.

 Input  
 Output  
    21   
    60   
    1   
    21   
    3   
    14   
    5   
    60   
    7   
    6   
    81   
find_sum(lst, 81)
Coding Exercise#
Take a close look and design a step-by-step algorithm first, before jumping on to the implementation. This problem is designed for your practice, so try to solve it on your own first. If you get stuck, you can always refer to the solution provided in the solution section. Good Luck!

Algorithm:
    -> Traverse through the list using a for loop
        -> Traverse again using a 2nd for loop
            -> Now try adding the pair of numbers from 1st & 2nd loop instance variables i,j resply
            -> If they are adding up to k, then return i,j
"""
lst = [1,21,3,14,5,60,7,6]
k = 8
def find_sum_brute_force(lst, k):
    for i in lst:
        for j in lst[1:]:
            if (i + j == k): 
                return [i,j]
            
#result = find_sum_brute_force(lst, k)

def find_sum_moving_indices(lst, k):
    ''' 
    Algorithm:
    -> top level implementation details:
        -> sort the list first
        -> traverse the list parallely from both ends, using the indices: (tech implementation using while loop with condition -> 
                                                                           indices are not equal to each other)
            -> we're gonna check if the two elements ie., the beginnign and ending one are adding up to become k.
                    -> if the sum is greater than k:
                        -> shift the 2nd index at right end to left by one unit
                    -> if the sum is less than k:
                        -> we're gonna do the vice versa i.e., shift the index right
                    -> if neither, we return them using indices:
    
    lst: list
    k:   int
    return: list
    '''
    index1 = 0
    index2 = len(lst) - 1
    _sum = 0
    
    lst.sort()
    
    while (index1 != index2):
        _sum = lst[index1] + lst[index2]
        if _sum > k :
            index2 -= 1
        elif (_sum < k) :
            index1 += 1
        else:
            return [lst[index1], lst[index2]]
        
print(find_sum_moving_indices(lst, k))









