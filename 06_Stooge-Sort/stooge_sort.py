# stooge_sort.py
"""Stooge sort is a recursive sorting algorithm. It is notable for its exceptionally bad time complexity of 
O(n^(log3 / log1.5)) = O(n^2.7095...). The running time of the algorithm is thus slower compared to reasonable sorting 
algorithms, and is slower than Bubble sort, a canonical example of a fairly inefficient sort."""


def stoogesort(items, i=0, j=None):
    if j is None:
        j = len(items) - 1
    if items[j] < items[i]:
        items[i], items[j] = items[j], items[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        stoogesort(items, i, j - t)
        stoogesort(items, i + t, j)
        stoogesort(items, i, j - t)
    return items


if __name__ == "__main__":
    import random

    from timing import timed_func

    stoogesort = timed_func(stoogesort)
    items = [random.randint(1, 1000) for _ in range(250)]
    print(stoogesort(items)[1])