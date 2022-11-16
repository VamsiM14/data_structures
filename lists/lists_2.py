# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:48:15 2022

@author: hp
"""

a = [1,3,4,5]
b = [2,6,7,8]

def merge_lists(lst1, lst2):
    # 'Write your code here
    arr = []
    for i in lst1:
        print(f'''=> entered 1st for: i = {i}''')
        for j in lst2:
            print(f'''=> entered 2nd for: j = {j}''')    
            print(f'''-> counter values: i: {i}, j: {j}''' )
            if i <= j:
                print(f''' -> Adding i: {i} to arr''')
                arr += [i]
                print(f''' -> arr: {arr}''')
                print(f''' -> Removing {i} from lst1 ''')
                lst1.remove(i)
                print(f''' -> lst1: {lst1}''')
                break
            else:
                print(f''' -> Adding j: {j} to arr''')
                arr += [j]
                print(f''' -> arr: {arr}''')
                print(f''' -> Removing {j} to arr''')
                lst2.remove(j)
                print(f''' -> lst2: {lst2}''')
    print(f''' ----> final: {arr + lst1 + lst2}''')
    return arr + lst1 + lst2

#merge_lists(a, b)

def merge_lists2(lst1, lst2):
    ind1 = 0
    ind2 = 0
    while(ind1 < len(lst1) and ind2 < len(lst2)):
        if lst1[ind1] > lst2[ind2]:
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1
    if(ind2 < len(lst2)):
        lst1.extend(lst2[ind2:])
    
    print(f''' lst1: {lst1}''')
    return lst1
merge_lists2(a,b)
