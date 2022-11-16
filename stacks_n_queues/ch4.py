# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:30:19 2022

@author: hp
"""

from Stack import MyStack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        # Write your code here


    # Inserts Element in the Queue
    def enqueue(self, value):
        if self.main_stack.is_empty():
            self.main_stack.push(value)
        else:
            temp_stack = MyStack()
            while not self.main_stack.is_empty():
                temp_stack.push(self.main_stack.pop())
            temp_stack.push(value)
            for i in range(temp_stack.size()):
                self.main_stack.push(temp_stack.pop())
                
    # Removes Element From Queue
    def dequeue(self):
        if self.main_stack.is_empty():
            return -1
        else:
            return self.main_stack.pop()
        
    def display(self):
        return self.main_stack.__str__()
        
if __name__ == "__main__" :
    queue = NewQueue()
    for i in range(5):
        queue.enqueue(i+1)
    print("----------", queue.display())
    for i in range(5):
        queue.dequeue()