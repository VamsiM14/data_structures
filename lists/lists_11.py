# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 08:57:18 2022

@author: hp

Problem statement#
Given an integer list, return the maximum sublist sum. The list may contain both positive and negative integers and is unsorted.

Partial function definition#
def find_max_sum_sublist(lst):
  pass
Input#
a list lst
Output#
a number (maximum subarray sum)

"""
def find_max_sum_sublist(lst): 
  if (len(lst) < 1): 
    return 0;

  curr_max = lst[0];
  global_max = lst[0];
  length_array = len(lst);
  for i in range(1, length_array):
    if curr_max < 0: 
      curr_max = lst[i]
    else:
      curr_max += lst[i]
    if global_max < curr_max:
      global_max = curr_max

  return global_max;

print(find_max_sum_sublist([-2,10,7,-5,15,-6]))