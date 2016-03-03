
import time


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        
    def __enter__(self):
        self.start = time.time()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.secs = self.end - self.start
        if self.verbose:
            self.msecs= self.secs * 1000
            with open('timer.txt', 'a') as f:
                print >> f, "elapsed time: %f ms" % self.msecs


import bcrypt

with Timer(verbose=True) as t:
    salt = bcrypt.gensalt()
    print 'salt: ',salt
    cpwd = bcrypt.hashpw('cosmo', salt)
    print 'cpwd: ', cpwd
    print cpwd == bcrypt.hashpw('cosmo', cpwd)