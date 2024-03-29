# -*- coding:utf-8 -*-
import math
import timeit


def mergeSort(arr) -> (list, list):
    """
    最好时间复杂度O(n*logn)
    最坏时间复杂度O(n*logn)
    稳定
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    middle = math.floor(len(arr) / 2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left: list, right: list):
    """
    left 和 right 都是已排序序列
    :param left:
    :param right:
    :return:
    """
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # 将剩下元素的直接按顺序放在已排序的列表的尾部
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result  # 已排序


# ------------------------------- 优化版 ------------------------------------

# dragon: 优化pop和append(优化后，当列表的规模很大的时候，性能提升明显)
# def merge(left: list, right: list):
#     result = [None] * (len(left) + len(right))
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result[i + j] = left[i]
#             i += 1
#         else:
#             result[i + j] = right[j]
#             j += 1
#
#     while i < len(left):
#         result[i + j] = left[i]
#         i += 1
#
#     while j < len(right):
#         result[i + j] = right[j]
#         j += 1
#     return result


# ls = [i for i in range(100000, 0, -1)]
#
#
# def test():
#     mergeSort(ls)


if __name__ == '__main__':
    print(f"归并排序：")
    ls = [5, 1, 6, 3, 10, 4, 9, 8, 7, 2, 0]
    print(f"排序前: {ls}")

    res = mergeSort(ls)
    print(f"升序排序后: {res}")

    # 测试性能
    # print(timeit.timeit('test()', setup='from __main__ import test', number=10))
