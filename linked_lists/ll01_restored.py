# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 07:27:52 2022

@author: hp

Implementing Singly Linked List Data Structure
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        
class LinkedList:
    def __init__(self):
        self.head_node = None
        
    def get_head(self):
        return self.head_node #returns head node
    
    def is_empty(self):
        if self.head_node is None: #cheeck whether head node is empty
            return True
        else:
            return False

    def insert_at_head(self, data):
        ''' Insert a Node with specified data at the head position'''
        temp_node = Node(data) #create a temp Node(data)
        temp_node.next_element = self.head_node # point the new node's pointer to the head of previous node
        self.head_node = temp_node # make the new node as linkedlist's head
        return self.head_node
    
    # supplementary print function
    def print_list(self):
        if self.is_empty():
            print("Linked list is empty")
            return False
        temp = self.head_node
        
        while temp.next_element is not None:
            print(temp.data, end="->")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True
            
    
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)
    
        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return
    
        # if list not empty, traverse the list to the last node
        temp = self.get_head()
    
        while temp.next_element:
            temp = temp.next_element
    
        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    def search(self, value):
        
        if self.get_head() is None:
            return False
        temp = self.get_head()
        
        if temp.data == value:
           return True
        else:
           while temp.next_element:
               temp = temp.next_element
               if temp.data == value:
                   return True
               
        return False
    
    def delete(self, value):
        
        if self.get_head() is None:
            print("List is empty")
            return
        temp = self.get_head()
        
        if temp.data == value:
            self.head = temp.next_element
            delete 
           
                   
        
lst = LinkedList()
lst.insert_at_head(11)
lst.insert_at_head(10)
print(lst.search(100))
print(lst.search(11))

''' 
 while temp.next_element:
     if temp.data == value:
         return True
     temp = temp.next_element
 
 if temp.data == value:
     return True
 else:
     return False
'''