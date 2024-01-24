# -*- coding:utf-8 -*-

"""
快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。
但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 记号中隐含的常数因子很小，
比复杂度稳定等于 O(nlogn) 的归并排序要小很多。
所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。
"""


def quickSort(arr, left=None, right=None):
    """
    业务代码不用传递 left 和 right，这两个参数时内部递归用的
    :param arr:
    :param left:
    :param right:
    :return:
    """
    # left = 0 if not isinstance(left, (int, float)) else left
    # right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    left = left if left is not None else 0
    right = right if right is not None else len(arr) - 1
    if left < right:  # 要排序部分的长度 大于1 才需要排序
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr


def partition(arr, left, right):
    pivot = left  # 基准元素
    index = pivot + 1  # index 指向 基准元素后面 第一个比 基准元素大的元素
    i = index  # i 用于遍历基准 pivot 后的每一个元素
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)  # 最后，index-1处的元素 一定小于等于 基准元素，所以互换位置
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    print(f"归并排序：")
    ls = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    ls.sort()
    print(f"排序前: {ls}")

    quickSort(ls)
    print(f"升序排序后: {ls}")
