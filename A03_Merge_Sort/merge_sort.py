# merge_sort.py
"""
Worst complexity:   n * log(n)
Average complexity: n * log(n)
Best complexity:    n * log(n)
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