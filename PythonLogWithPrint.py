import threading
import time
import logging

#logging.basicConfig(level=logging.debug,
 #                   format='(%(threadName)-9s) %(message)s',)

def consumer(cv):
    print('Consumer thread started ...')
    with cv:
        print('Consumer waiting ...')
        cv.wait()
        print('Consumer consumed the resource')

def producer(cv):
    print('Producer thread started ...')
    with cv:
        print('Making resource available')
        print('Notifying to all consumers')
        cv.notifyAll()

if __name__ == '__main__':
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()
