# -*- coding: utf-8 -*-



#Using threading with queue

import queue
import threading
import time


def putting_thread(q):
    while True:
        print('starting thread')
        time.sleep(10)
        q.put(5)
        print('put something')
##        
#    
#        
#
q = queue.Queue()
t = threading.Thread(target = putting_thread, args = (q,),daemon = True)
t.start()

q.put(5)



print(q.get())
print('first item gotten')
print(q.get())
print('finished')


#intializing a variable to q.get()

x =q.get()

print(x)



#difference between LIFO and FIFO


import queue
q = queue.Queue()

for i in range(5):
    q.put(i)
    
while not q.empty():
    print(q.get(), end = '   ')
    
    
print('\n')    
    
    
import queue
q = queue.LifoQueue()

for i in range(5):
    q.put(i)
    
while not q.empty():
    print(q.get(), end = '   ')
    
    
    
    
# priority queue


import queue
import time

q = queue.PriorityQueue()

q.put((1, 'Priority 1'))
q.put((3, 'Prioirty 3'))
q.put((4 ,'Priority 4'))
q.put((2 ,'Priority 2'))




for i in range(q.qsize()):
    print(q.get()[1])



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    