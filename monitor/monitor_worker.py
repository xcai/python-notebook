#!/usr/bin/python3

import time
import queue
import random
from multiprocessing.managers import BaseManager


class MonitorWorkerManager(BaseManager):
    def __init__(self, address=None, authkey=None, serializer='pickle',ctx=None):
        super().__init__(address, authkey, serializer, ctx)
        self.register('get_monitor_queue')

    def start_monitor_worker(self):
        self.connect()
        print("connected to server %s"%self._address)
        task = self.get_monitor_queue()
        print('start to collect message and send to master...')
        while True:
            task.put(str(random.random()))
            time.sleep(5)
        self.shutdown()

if __name__ == '__main__':
    address = ('10.10.10.20', 9000)
    authkey = 'monitor'
    worker = MonitorWorkerManager(address, authkey.encode())
    worker.start_monitor_worker()
