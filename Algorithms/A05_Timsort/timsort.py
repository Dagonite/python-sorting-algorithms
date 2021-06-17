"""
Worst complexity:   n*log(n)
Best complexity:    n
Average complexity: n*log(n)
"""


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1

        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


def timsort(items):
    min_run = 32
    n = len(items)

    for i in range(0, n, min_run):
        insertion_sort(items, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(left=items[start : midpoint + 1], right=items[midpoint + 1 : end + 1])
            items[start : start + len(merged_array)] = merged_array

        size *= 2

    return items


if __name__ == "__main__":
    from random import randint

    from timing import timed_func

    timsort = timed_func(timsort)
    items = [randint(1, 1000) for _ in range(5000)]
    print(timsort(items)[1])