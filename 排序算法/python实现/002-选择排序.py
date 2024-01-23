# -*- coding:utf-8 -*-


def selectionSort(arr, reverse=False):
    """
    最好时间复杂度O(n²)
    最坏时间复杂度O(n²)
    不稳定
    :param arr:
    :param reverse: 是否倒序
    :return:
    """

    for i in range(len(arr) - 1):
        # 记录最大或小数的索引
        minMixIndex = i

        for j in range(i + 1, len(arr)):
            if reverse:
                if arr[j] > arr[minMixIndex]:
                    minMixIndex = j
            else:
                if arr[j] < arr[minMixIndex]:
                    minMixIndex = j

        # i 不是最值时，将 i 和最值进行交换
        if i != minMixIndex:
            arr[i], arr[minMixIndex] = arr[minMixIndex], arr[i]
    return arr


if __name__ == '__main__':
    print(f"选择排序：")
    ls = [5, 1, 6, 3, 4, 9, 8, 7, 2, 0]
    print(f"排序前: {ls}")

    selectionSort(ls)
    print(f"升序排序后: {ls}")

    selectionSort(ls, reverse=True)
    print(f"降序排序后: {ls}")
