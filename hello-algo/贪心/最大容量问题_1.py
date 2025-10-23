# -*- coding:utf-8 -*-
"""
输入一个数组 ht，其中的每个元素代表一个垂直隔板的高度。数组中的任意两个隔板，以及它们之间的空间可以组成一个容器。
容器的容量等于高度和宽度的乘积（面积），其中高度由较短的隔板决定，宽度是两个隔板的数组索引之差。
请在数组中选择两个隔板，使得组成的容器的容量最大，返回最大容量。
"""


def max_capacity(ht: list[int]) -> int:
    """最大容量：贪心"""
    # 初始化 i, j，使其分列数组两端
    i, j = 0, len(ht) - 1

    # 初始最大容量为 0
    res = 0

    # 循环贪心选择，直至两板相遇
    while i < j:
        # 更新最大容量
        cap = min(ht[i], ht[j]) * (j - i)
        res = max(res, cap)
        # 向内移动短板
        if ht[i] < ht[j]:
            i += 1
        else:
            j -= 1
    return res


if __name__ == "__main__":
    ht = [3, 8, 5, 2, 7, 7, 3, 4]

    # 贪心算法
    res = max_capacity(ht)
    print(f"最大容量为 {res}")
