# comparison.py
"""Script comparing the speeds of the different sorting algorithms."""

import random
import time
import importlib

algorithms = [
    sorted,
]

algorithms.append(importlib.import_module("Algorithms.A01_Bubble_Sort.bubble_sort").bubble_sort)
algorithms.append(importlib.import_module("Algorithms.A02_Insertion_Sort.insertion_sort").insertion_sort)
algorithms.append(importlib.import_module("Algorithms.A03_Merge_Sort.merge_sort").merge_sort)
algorithms.append(importlib.import_module("Algorithms.A04_Quicksort.quicksort").quicksort)
algorithms.append(importlib.import_module("Algorithms.A05_Timsort.timsort").timsort)
algorithms.append(importlib.import_module("Algorithms.A07_Heapsort.heapsort").heapsort)

x = [random.randint(1, 1000) for _ in range(5000)]

for algorithm in algorithms:
    items = x[:]
    start = time.perf_counter()
    name = "built-in sorted" if algorithm.__name__ == "sorted" else algorithm.__name__
    algorithm(items)
    print(f"{name:<15} took {time.perf_counter() - start:.7f} seconds")
