"""
Worst complexity:   n ** (log3/log1.5)
Best complexity:    n ** (log3/log1.5)
Average complexity: n ** (log3/log1.5)
"""


def stooge_sort(items, i=0, j=None):
    if j is None:
        j = len(items) - 1
    if items[j] < items[i]:
        items[i], items[j] = items[j], items[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        stooge_sort(items, i, j - t)
        stooge_sort(items, i + t, j)
        stooge_sort(items, i, j - t)
    return items


if __name__ == "__main__":
    from random import randint

    from timing import timed_func

    stooge_sort = timed_func(stooge_sort)
    items = [randint(1, 1000) for _ in range(250)]
    print(stooge_sort(items)[1])