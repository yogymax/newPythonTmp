import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

listOfItems = []

def consumer(cv):
    logging.debug('Consumer thread started ...')

    while True:
        with cv:
            logging.debug('Consumer waiting ...')
            cv.wait()
            logging.debug('Consumer consumed the resource')

        time.sleep(2)
        if listOfItems.__len__() !=0:
            print(listOfItems.pop())

def producer(cv):
    logging.debug('Producer thread started ...')
    while True:
        with cv:
            logging.debug('Making resource available')
            logging.debug('Notifying to all consumers')
            cv.notify()
        time.sleep(1)
        a = random.randint(1, 100);
        print('Item Produced ..', a)
        listOfItems.append(a)

if __name__ == '__main__':
    condition1 = threading.Condition()
    condition2 = threading.Condition()

    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition1,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition2,))
    pd = threading.Thread(name='producer', target=producer, args=(condition1,))


    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(5)
    pd.start()
