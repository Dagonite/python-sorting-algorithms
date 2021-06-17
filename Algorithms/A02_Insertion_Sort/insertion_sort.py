"""
Worst complexity:   n ** 2
Average complexity: n ** 2
Best complexity:    n
"""


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
    from random import randint

    from timing import timed_func

    insertion_sort = timed_func(insertion_sort)
    items = [randint(1, 1000) for _ in range(5000)]
    print(insertion_sort(items)[1])