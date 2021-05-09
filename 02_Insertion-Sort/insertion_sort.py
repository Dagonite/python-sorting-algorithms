# insertion_sort.py
"""Insertion sort consists of two nested loops. As such, the average runtime is still O(n^2). The worst-case is a 
reverse order array which is still O(n^2). The best case is when the array is already sorted as the inner loop is never 
executed, resulting in an O(n) runtime. In practise, insertion sort is usually quicker than bubble sort."""


def insertion_sort(items):
    for i in range(1, len(items)):
        key_item = items[i]
        j = i - 1

        while j >= 0 and items[j] > key_item:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = key_item

    return items


if __name__ == "__main__":
    import random

    from timing import timed_func

    insertion_sort = timed_func(insertion_sort)
    items = [random.randint(1, 1000) for _ in range(5000)]
    print(insertion_sort(items)[1])