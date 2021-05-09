# merge_sort.py
"""The merge() function has a linear runtime. It receives two arrays whose combined length is at most n (the length of 
the original input array), and it combines both arrays by looking at each element at most once. This leads to a runtime 
complexity of O(n).

The second step splits the input array recursively and calls merge() for each half. Since the array is halved until a 
single element remains, the total number of halving operations performed by this function is log2n. Since merge() is 
called for each half, there is a total runtime of O(nlog2n)."""


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


def merge_sort(items):
    if len(items) < 2:
        return items

    midpoint = len(items) // 2

    return merge(left=merge_sort(items[:midpoint]), right=merge_sort(items[midpoint:]))


if __name__ == "__main__":
    import random, time

    items = [random.randint(1, 1000) for _ in range(5000)]
    start = time.perf_counter()
    merge_sort(items)
    print(time.perf_counter() - start)