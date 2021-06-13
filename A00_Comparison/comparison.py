# comparison.py
import random
import time

from timing import timed_func
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quicksort import quicksort
from timsort import timsort
from heapsort import heapsort

algorithms = [
    bubble_sort,
    insertion_sort,
    merge_sort,
    quicksort,
    timsort,
    heapsort,
    sorted,
]

x = [random.randint(1, 1000) for _ in range(5000)]

for algorithm in algorithms:
    items = x[:]
    start = time.perf_counter()
    name = "built-in sorted" if algorithm.__name__ == "sorted" else algorithm.__name__
    algorithm(items)
    print(f"{name:<15} took {time.perf_counter() - start:.7f} seconds")
