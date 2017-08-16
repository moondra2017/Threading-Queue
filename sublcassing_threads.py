 -*- coding: utf-8 -*-
Threading part 4 - subclassing



__int__ method
run method
*Source code*

def run(self):
        """Method representing the thread's activity.
        You may override this method in a subclass. 
        The standard run() method
        invokes the callable object passed to 
        the object's constructor as the
        target argument, if any, with sequential and 
        keyword arguments taken
        from the args and kwargs arguments, respectively.
        """
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs




t = threading.Thread(target = sleeper, name = 'thread1',\
 #                    args = (5, 'thread1')) 
###TEST1


import time
import threading

class MyThread(threading.Thread):
    def run(self):
        print('{} has started!'.format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
        print('{} has finished!'.format(self.getName()))
        
def sleeper (n, name) :
    print('Hi, I am {}. Going to sleep for 5 seconds\
          \n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))
    
    
    
for i in range(4):
    t = MyThread(target = sleeper, 
                 name = 'thread {}'.format(i+1),
                 args = (3, 'thread {}'.format(i+1)))
    t.start()




 #TEST TWO, 
 
 
 #Changing overriding __init__
def __init__(self, group=None, target=None, name=None,
args=(), kwargs=None, *, daemon=None):


import time
import threading

class MyThread(threading.Thread):
    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args = args
        
        
    def run(self):
        print('thread {} has started'.format(self.number))
        self.func(*self.args)
        print('thread {} has finished'.format(self.number))
        
        
def double(number, cycles):
    for i in range(cycles):
        number += number
    print(number)
    
    
threads_list = []

for i in range(50):
    t = MyThread(number = i +1, func = double, 
                 args = [i, 3])
    threads_list.append(t)
    t.start()
    
for t in threads_list:
    t.join()
        
        
    

 TEST 3 SUPER  

 METHOD 1 ############################

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style
        
        
    def run(self, *args, **kwargs):
        print('thread starting')
        super(MyThread, self).run(*args, **kwargs)
        print('thread has ended')
        
        
        
def sleeper (num, style):
    print('we are sleeping for {} seconds as {}'.format(num, style))
    time.sleep(num)   



t = MyThread(number =3, style = 'yellow', target = sleeper, 
             args = [3, 'yellow']) 

t.start()    

    
        
        
        
         




            
            


    
    
    
