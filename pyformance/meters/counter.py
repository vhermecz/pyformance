from threading import Lock

class Counter(object):
    """
    An incrementing and decrementing metric
    """
    def __init__(self):
        super(Counter, self).__init__()
        self.lock = Lock()
        self.counter = 0
        
    def inc(self, val=1):
        with self.lock:
            self.counter = self.counter + val
        
    def dec(self, val=1):
        self.inc(-val)
        
    def get_count(self):
        return self.counter
    
    def clear(self):
        with self.lock:
            self.counter = 0

