"""Script comparing the speeds of multiple sorting algorithms."""

from random import randint
from time import perf_counter
from importlib import import_module

algorithms = [
    sorted,
]

algorithms.append(import_module("Algorithms.A01_Bubble_Sort.bubble_sort").bubble_sort)
algorithms.append(import_module("Algorithms.A02_Insertion_Sort.insertion_sort").insertion_sort)
algorithms.append(import_module("Algorithms.A03_Merge_Sort.merge_sort").merge_sort)
algorithms.append(import_module("Algorithms.A04_Quicksort.quicksort").quicksort)
algorithms.append(import_module("Algorithms.A05_Timsort.timsort").timsort)
algorithms.append(import_module("Algorithms.A07_Heapsort.heapsort").heapsort)
algorithms.append(import_module("Algorithms.A08_Tree_Sort.tree_sort").tree_sort)

x = [randint(1, 1000) for _ in range(5000)]

for algorithm in algorithms:
    items = x[:]
    start = perf_counter()
    name = "built-in sorted" if algorithm.__name__ == "sorted" else algorithm.__name__
    algorithm(items)
    end = perf_counter()
    print(f"{name:<15} took {end - start:.7f} seconds")
