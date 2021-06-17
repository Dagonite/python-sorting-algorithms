"""
Worst complexity:   n ** 2
Average complexity: n * log(n)
Best complexity:    n * log(n)
"""

from random import randint


def quicksort(items):
    if len(items) < 2:
        return items

    low, same, high = [], [], []
    pivot = items[randint(0, len(items) - 1)]

    for item in items:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


if __name__ == "__main__":
    from time import perf_counter

    items = [randint(1, 1000) for _ in range(5000)]
    start = perf_counter()
    quicksort(items)
    print(perf_counter() - start)