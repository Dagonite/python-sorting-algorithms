"""File containing a timing function that can be used as a decorator."""

import time


def timed_func(func):
    def timed(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        total_time = time.perf_counter() - start
        return res, total_time

    return timed