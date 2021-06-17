"""
Worst complexity:   n ** 2
Average complexity: n ** 2
Best complexity:    n
"""


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
    from random import randint

    from timing import timed_func

    bubble_sort = timed_func(bubble_sort)
    items = [randint(1, 1000) for _ in range(5000)]
    print(bubble_sort(items)[1])
