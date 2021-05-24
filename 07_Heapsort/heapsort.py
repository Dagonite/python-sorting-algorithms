# heapsort.py
"""Heapsort is a comparison-based sorting algorithm. Heapsort can be thought of as an improved selection sort: like 
selection sort, heapsort divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted 
region by extracting the largest element from it and inserting it into the sorted region. Unlike selection sort, 
heapsort does not waste time with a linear-time scan of the unsorted region; rather, heap sort maintains the unsorted 
region in a heap data structure to more quickly find the largest element in each step."""


def heapsort(items):
    for start in range(int((len(items) - 2) / 2), -1, -1):
        siftdown(items, start, len(items) - 1)

    for end in range(len(items) - 1, 0, -1):
        items[end], items[0] = items[0], items[end]
        siftdown(items, 0, end - 1)
    return items


def siftdown(items, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and items[child] < items[child + 1]:
            child += 1
        if items[root] < items[child]:
            items[root], items[child] = items[child], items[root]
            root = child
        else:
            break


if __name__ == "__main__":
    import random

    from timing import timed_func

    heapsort = timed_func(heapsort)
    items = [random.randint(1, 1000) for _ in range(8000)]
    print(heapsort(items)[1])