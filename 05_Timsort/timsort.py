# timsort.py
"""On average, the complexity of timsort is O(nlog2n), just like merge sort and quicksort. The logarithmic part comes 
from doubling the size of the run to perform each linear merge operation.

Timsort performs exceptionally well on already-sorted or close-to-sorted lists, leading to a best-case scenario of O(n). 
In this case, timsort clearly beats merge sort and matches the best-case scenario for Quicksort. But the worst case for 
timsort is also O(nlog2n), which surpasses Quicksort's O(n^2)."""


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


def timsort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(left=array[start : midpoint + 1], right=array[midpoint + 1 : end + 1])
            array[start : start + len(merged_array)] = merged_array

        size *= 2

    return array


if __name__ == "__main__":
    import random

    from timing import timed_func

    timsort = timed_func(timsort)
    items = [random.randint(1, 1000) for _ in range(5000)]
    print(timsort(items)[1])