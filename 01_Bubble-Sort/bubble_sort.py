# bubble_sort.py
"""Bubble sort consists of two nested for loops in which the algorithm performs n-1 comparisons, then n-2 comparisons,
and so on until the final comparison is done. This comes at a total of n(n-1)/2 comparisons. This simplifies down to
n^2-n which can be further simplified, leaving bubble sort with an average and worst-case complexity of O(n^2). In cases
where the algorithm receives an array that's already sorted, the runtime complexity comes down to O(n) as the algorithm
will not needed to visit any element more than once."""


def bubble_sort(items):
    for i in range(len(items)):
        already_sorted = True
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                already_sorted = False

        if already_sorted:
            break

    return items


if __name__ == "__main__":
    import random

    from timing import timed_func

    bubble_sort = timed_func(bubble_sort)
    items = [random.randint(1, 1000) for _ in range(5000)]
    print(bubble_sort(items)[1])
