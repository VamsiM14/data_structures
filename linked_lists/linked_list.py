# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 07:27:52 2022

@author: hp

Implementing Singly Linked List Data Structure
"""
from typing import Optional

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
        
        ''' 
            
        '''
        
        delete = False
        if self.is_empty():
            print("List is empty")
            return delete
        
        if self.search(value):
            # Delete at head
            current_head = self.get_head()
            next_element = current_head.next_element
            
            if current_head.data == value:
                current_head.data = None
                self.head = next_element
                delete = True
            else: # Delete at Nth position
                prev_element = current_head
                current_elemnent = next_element
                while current_elemnent.data is not value:
                    prev_element = current_elemnent
                    current_elemnent = current_elemnent.next_element
                current_elemnent.data = None
                prev_element.next_element = current_elemnent.next_element
                delete = True
                
            print(f"Delete successfull for value: {value}")
            return

        else:
            print(f"Value: {value} not found")
            return
        
        
    def length(self):
        counter = 0
        temp = self.head_node
                
        while temp:
            counter += 1
            temp = temp.next_element
        #print(counter)
        return counter
    
    def reverse(self):
        ''' 
        Reverse the linked list.
        
        notes: 
            
            discarded (this creates a new ll rather than to modify the existing one): Idea is to use insert_at_head(item) while traversing through the current list.
        '''
        #reversed_linked_list = LinkedList()
        prev = None
        current = self.head_node
        next = None
        
        while current:
            next = current.next_element
            current.next_element = prev
            prev = current
            current = next
            
        self.head_node = prev
        return self
    
    def detect_loop(self):
        loop = False
        one_step = self.head_node
        two_step = self.head_node
        while one_step and two_step and two_step.next_element:
            one_step = one_step.next_element
            two_step = two_step.next_element.next_element
            if one_step == two_step:
                loop = True
        return loop
        
    def find_mid(self):
        mid_index = self.length()//2 if (self.length() % 2 == 0 ) else (self.length()//2 + 1)
        #print(mid_index)
        current_node = self.head_node
        for i in range(mid_index - 1):
            current_node = current_node.next_element
        return current_node.data
    
    def remove_duplicates(self):
        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node
            while inner_node:
                if inner_node.next_element:
                    if outer_node.data == inner_node.next_element.data:
                        new_next_element = inner_node.next_element.next_element
                        inner_node.next_element = new_next_element
                        #inner_node = inner_node.next_element
                    else:
                        inner_node = inner_node.next_element
                else:
                    inner_node = inner_node.next_element
            outer_node = outer_node.next_element
        return self
    
    def union(self, linked_list):
        
        if linked_list.is_empty():
            return self
        elif self.is_empty():
            return linked_list
        
        primary_linked_list = self.get_head()
        while primary_linked_list.next_element:
            primary_linked_list = primary_linked_list.next_element
        primary_linked_list.next_element = linked_list.get_head()
        self.remove_duplicates()
        return self
    
    def intersection(self, linked_list):
        primary_linked_list = self.get_head()
        
        while primary_linked_list:
            secondary_linked_list = linked_list.get_head()
            match = False
            while secondary_linked_list:
                if primary_linked_list.data == secondary_linked_list.data:
                    new_next_element = secondary_linked_list.next_element
                    secondary_linked_list = new_next_element
                    match = True
                    break
                else:
                    secondary_linked_list = secondary_linked_list.next_element
            if match:
                primary_linked_list = primary_linked_list.next_element
            else:
                self.delete(primary_linked_list.data)
                primary_linked_list = primary_linked_list.next_element
        
        return self
    
    def find_nth(self, n):
        m = self.length() - n
        if m < 0 or m >= self.length():
            return -1
        node = self.get_head()
        for i in range(m):
            node = node.next_element
        return node.data
                    
        
lst1 = LinkedList()
lst1.insert_at_head(14)
lst1.insert_at_head(22)
lst1.insert_at_head(99)
lst1.insert_at_head(7)
lst1.insert_at_head(5)
lst1.insert_at_head(1)
lst1.print_list()
print(lst1.find_nth(-9))
print(help(LinkedList))

'''
        Prev code:
        prev_node = None
        next_node = None

            while current_node:
            #self.insert_at_head(current_node.data)
            #current_node = current_node.next_element
            prev_node = current_node
            next_node = current_node.next_element
            
            extra_temp = temp
            current_node = current_node.next_element
            temp = current_node
            temp.next_element = extra_temp
            
            lst = LinkedList()
            lst.insert_at_head(1)
            lst.insert_at_head(4)
            lst.insert_at_head(6)
            lst.insert_at_head(4)
            lst.insert_at_head(5)


            lst.print_list()
            print(lst.detect_loop())
            print(lst.detect_loop_fly())
            
        return
    
    head = lst.get_head()
    node = lst.get_head()

    for i in range(4):
        if node.next_element is None:
            node.next_element = head.next_element
            break
        node = node.next_element
        
        
lst = LinkedList()
lst.insert_at_tail(1)
lst.insert_at_tail(3)
lst.insert_at_tail(6)
lst.insert_at_tail(5)
lst.insert_at_tail(7)
lst.insert_at_tail(1)
lst.insert_at_tail(3)
lst.insert_at_tail(6)
lst.insert_at_tail(5)
lst.insert_at_tail(7)
lst.insert_at_tail(9)
lst.insert_at_tail(11)
lst.print_list()

# Adding a loop

print("detect_loop()'s result-->", lst.detect_loop())
print("detect_loop_fly()'s result-->", lst.detect_loop_fly())

        '''


''' 
 while temp.next_element:
     if temp.data == value:
         return True
     temp = temp.next_element
 
 if temp.data == value:
     return True
 else:
     return False
 
    
 
        if self.length() < linked_list.length():
            primary_linked_list = self.get_head()
            secondary_linked_list = linked_list.get_head()
        else:
            secondary_linked_list = self.get_head()
            primary_linked_list = linked_list.get_head()
'''