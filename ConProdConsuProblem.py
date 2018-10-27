import threading
import time
import logging
import random
from queue import Queue

#logging.basicConfig(level=logging.DEBUG,
#                   format='(%(threadName)-9s) %(message)s', )

logging.basicConfig(
    #filename='prodConsume.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt="%Y-%mon-%d %H:%M:%S")



BUF_SIZE = 10
q = Queue(BUF_SIZE)


class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        print('producer started working')
        #print('Inside producer Q : ', list(q))
        while True:
            if not q.full():
                item = random.randint(1, 10)
                q.put(item)
                logging.debug('Putting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(1)
         #       print('Inside run producer Q : ', list(q))
        return


class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        print('consucer started working')
        #print('Inside consucer Q : ', list(q))
        while True:
            if not q.empty():

                item = q.get()
                logging.debug('Getting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(2)
         #       print('Inside run consucer Q : ', list(q))
        return


if __name__ == '__main__':
    p1 = ProducerThread(name='producer1')
    #p2 = ProducerThread(name='producer2')
    c = ConsumerThread(name='consumer')

    #p2.start()
    p1.start()
    time.sleep(15)
    c.start()
    time.sleep(2)
