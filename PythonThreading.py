

import threading
import time

class MyThread(threading.Thread):

    def run(self):  #task
        for item in range(101,150):
            print(item)
            time.sleep(1)


t1 = MyThread() # inborn New stage of thread
t1.start() # Runnable

for item in range(400,440):
    print(item)

t1.join(30)
for item in range(1,60):
    print(item)


#create a thread
# Register that thread in Cpu Scheduler
#call Run method -- assign task to worker
print('\n\n\n')

'''
def m1(threadName, delay):
    number=0
    for item in range(0,11):
        number = number +1
        print ("%s: %d" % ( threadName, number ))


# Create two threads as follows
_thread.start_new_thread( m1, ("Thread-1", 2, ))#newnborn/Runnable/Running
'''