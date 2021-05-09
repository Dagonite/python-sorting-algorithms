# quicksort.py
"""With Quicksort, the input list is partitioned in linear time, O(n), and this process repeats recursively an average 
of log2n times. This leads to a final complexity of O(nlog2n). 

However, the selection of the pivot affects the runtime of the algorithm. The O(n) best-case scenario happens when the 
selected pivot is close to the median of the array, and an O(n2) scenario happens when the pivot is the smallest or 
largest value of the array.

Theoretically, if the algorithm focuses first on finding the median value and then uses it as the pivot element, then 
the worst-case complexity will come down to O(nlog2n). The median of an array can be found in linear time, and using it 
as the pivot guarantees the Quicksort portion of the code will perform in O(nlog2n).

By using the median value as the pivot, you end up with a final runtime of O(n) + O(nlog2n). This can be simplified down 
to O(nlog2n) because the logarithmic portion grows much faster than the linear portion."""


def quicksort(items):
    if len(items) < 2:
        return items

    low, same, high = [], [], []
    pivot = items[random.randint(0, len(items) - 1)]

    for item in items:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


if __name__ == "__main__":
    import random, time

    items = [random.randint(1, 1000) for _ in range(5000)]
    start = time.perf_counter()
    quicksort(items)
    print(time.perf_counter() - start)