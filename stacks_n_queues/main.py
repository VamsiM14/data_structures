from Queue import MyQueue
from Stack import MyStack


def reverseK(queue, k):
    if k < 0 or k > queue.size():
        return None
    
    nr_length = queue.size() - k
    temp_stack = MyStack()
    for i in range(k):
        temp_stack.push(queue.dequeue())
    while not temp_stack.is_empty():
        queue.enqueue(temp_stack.pop())
    for j in range(nr_length):
        queue.enqueue(queue.dequeue())
        
    return queue
    

q = MyQueue()
for i in range(7):
    q.enqueue(i)
rev = reverseK(q, 3)

print(rev.display())