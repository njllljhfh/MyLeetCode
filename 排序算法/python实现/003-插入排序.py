# -*- coding:utf-8 -*-


def insertionSort(arr, reverse=False):
    """
    最好时间复杂度O(n)
    最坏时间复杂度O(n²)
    稳定
    :param arr:
    :param reverse: 是否倒序
    :return:
    """
    for i in range(1, len(arr)):
        preIndex = i - 1
        current = arr[i]

        if reverse:
            # 向右移动已排序的数据，知道找到当前要插入的正确位置
            while preIndex >= 0 and arr[preIndex] < current:
                arr[preIndex + 1] = arr[preIndex]
                preIndex -= 1
        else:
            while preIndex >= 0 and arr[preIndex] > current:
                arr[preIndex + 1] = arr[preIndex]
                preIndex -= 1

        # 将当前数据插入到已排序部分的正确位置
        arr[preIndex + 1] = current
    return arr


if __name__ == '__main__':
    print(f"插入排序：")
    ls = [5, 1, 6, 3, 4, 9, 8, 7, 2, 0]
    print(f"排序前: {ls}")

    insertionSort(ls)
    print(f"升序排序后: {ls}")

    insertionSort(ls, reverse=True)
    print(f"降序排序后: {ls}")
