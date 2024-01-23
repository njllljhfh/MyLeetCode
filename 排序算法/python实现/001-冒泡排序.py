# -*- coding:utf-8 -*-


def bubbleSort(arr, reverse=False):
    """
    最好时间复杂度O(n)
    最坏时间复杂度O(n²)
    稳定
    :param arr:
    :param reverse: 是否倒序
    :return:
    """
    for i in range(1, len(arr)):  # 一共便利 length-1 趟
        for j in range(len(arr) - i):
            if reverse:
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    print(f"冒泡排序：")
    ls = [5, 1, 6, 3, 4, 9, 8, 7, 2, 0]
    print(f"排序前: {ls}")

    bubbleSort(ls)
    print(f"升序排序后: {ls}")

    bubbleSort(ls, reverse=True)
    print(f"降序排序后: {ls}")
