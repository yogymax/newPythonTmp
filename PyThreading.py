import _thread
import time

number =0
# Define a function for the thread
def m1( threadName, delay):
    number=0
    for item in range(0,11):
        number = number +1
        print ("%s: %d" % ( threadName, number ))
        time.sleep(delay)

# Create two threads as follows
try:
   _thread.start_new_thread( m1, ("Thread-1", 2, ) )
   _thread.start_new_thread( m1, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass