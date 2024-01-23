# -*- coding:utf-8 -*-
import math


def shellSort(arr, reverse=False):
    gap = 1

    while (gap < len(arr) / 3):
        gap = gap * 3 + 1

    while gap > 0:
        # print(f"gap = {gap}")
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            if reverse:
                while j >= 0 and arr[j] < temp:
                    arr[j + gap] = arr[j]
                    j -= gap
            else:
                while j >= 0 and arr[j] > temp:
                    arr[j + gap] = arr[j]
                    j -= gap
            arr[j + gap] = temp
        # print(f"arr = {arr}")
        gap = math.floor(gap / 3)
    return arr


if __name__ == '__main__':
    print(f"希尔排序：")
    ls = [5, 1, 6, 3, 4, 9, 8, 7, 2, 0]
    print(f"排序前: {ls}")

    shellSort(ls)
    print(f"升序排序后: {ls}")

    shellSort(ls, reverse=True)
    print(f"降序排序后: {ls}")
