# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:30:15 2022

@author: hp

Implement a function, find_first_unique(lst) that returns the first unique integer in the list.

Input#
A list of integers

Output#
The first unique element in the list

Sample Input#
[9,2,3,2,6,6]
Sample Output#
9
"""
import timeit

def find_first_unique(lst):
    fuv = lst[0]
    i = 1
    while (i < len(lst)):
        if lst[i] == fuv:
            lst.__delitem__(0)
            lst.__delitem__(i-1)
            return find_first_unique(lst)
        else:
            i += 1
    return fuv

print('1:', timeit.timeit(lambda:find_first_unique([4,5,1,2,0,4])))

def find_first_unique_sol2(lst):
    fuv_lst = []
    i = 0
    while (i < len(lst)):
        if lst[i] in fuv_lst:
            fuv_lst.remove(lst[i])
            i +=1
        else:
            fuv_lst.append(lst[i])
            i +=1
    return fuv_lst[0]
print('2:', timeit.timeit(lambda:find_first_unique_sol2([4,5,1,2,0,4])))

def find_first_unique_given_sol(lst):
    for index1 in range(len(lst)):
        index2 = 0
        # iterate the second list using index2
        while(index2 < len(lst)):
            if (index1 != index2 and lst[index1] == lst[index2]):
                break
            index2 += 1
        if (index2 == len(lst)):
            return lst[index1]
    return None
print('3:', timeit.timeit(lambda:find_first_unique_given_sol([4,5,1,2,0,4])))