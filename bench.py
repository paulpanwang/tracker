# Example benchmark
import time
import logging

def benchmark(func):
    """
        st decorator to calculate the total time of a func
    """

    def st_func(*args, **keyArgs):
        t1 = time.time()
        r = func(*args, **keyArgs)
        t2 = time.time()
        logging.info("%s,%s", func.__name__, t2 - t1)
        return r

    return st_func
