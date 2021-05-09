# timing.py

import time


def timed_func(func):
    def timed(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        total_time = time.perf_counter() - start
        return res, total_time

    return timed