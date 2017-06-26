#Threading part 2

#multiple threads


import threading
import time



def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))
    
    
 
start = time.time()
threads = []

for i in range(5):
    t = threading.Thread(target = sleeper, name = 'thread{}'.format(i), args =(5,'thread{}'.format(i) ) )
    threads.append(t)
    t.start()
    print('{} has started \n'.format(t.name))
 
 
 
    
for i in threads:

    i.join()
    
end = time.time()



print('time is {}'.format(end - start))






#example 2 without threads


import time

def sleeper(n, i):
    print ('Hi, I am function {}. Going to sleep for 5 seconds \n'.format(i))
    time.sleep(n)
    print('function{} has woken up from sleep \n'.format(i))




start = time.time()

for i in range(5):
    print('{} has started \n'.format(i))
    x = sleeper(5, i)
    
    
end  = time.time()


print('time taken: {}'.format(end - start))
