
import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time
import queue
from threading import Thread




SAVE_DIR = r'C:\Users\Moondra\Desktop\TEMP\Puppy_threading'



def decorator_function(func):
    def wrapper(*args,**kwargs):
        session = requests.Session()
        retry = Retry(connect=0, backoff_factor=0.2)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        return func(*args, session = session, **kwargs)
    return wrapper








#Using threading:
image_count = 0

#optional decorator_function
#@decorator_function   
def download_image(SAVE_DIR,q, session = None):
        global image_count
        if not session:
                session = requests.Session()
        while not q.empty():
            
            try:

                    r = session.get(q.get(block = False))

            except (requests.exceptions.RequestException, UnicodeError) as e:
                print(e)
                image_count += 1
                q.task_done()
                continue

            image_count += 1
            q.task_done()

            print('image', image_count)
            with open(os.path.join(
                        SAVE_DIR, 'image_{}.jpg'.format(image_count)),
                        'wb') as f:

                f.write(r.content)
                
               

q =queue.Queue()
with open(r'C:\Users\Moondra\Desktop\puppies.txt', 'rt') as f:
    for i in range(200):
        line = f.readline()
        q.put(line.strip())
print(q.qsize())


threads = []
start = time.time()
for i in range(20):
     t = Thread(target = download_image, 
                args = (SAVE_DIR,q))
     #t.setDaemon(True)
     threads.append(t)
     t.start()
q.join()

for t in threads:
    t.join()
    print(t.name, 'has joined')

end = time.time()
print('time taken: {:.4f}'.format(end - start))


#time taken: 7.4640
#time taken: 5.0860













                      

                      
