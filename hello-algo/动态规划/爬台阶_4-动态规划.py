# -*- coding:utf-8 -*-

"""
动态规划是一种“从底至顶”的方法：从最小子问题的解开始，迭代地构建更大子问题的解，直至得到原问题的解。

对于爬楼梯问题：
- 将数组 dp 称为 dp表，dp[i] 表示状态 i 对应子问题的解。
- 将最小子问题对应的状态（第 1 阶和第 2 阶楼梯）称为初始状态。
- 将递推公式 dp[i] = dp[i-1] + dp[i-2] 称为状态转移方程。
"""


def climbing_stairs_dp(n: int) -> int:
    """爬楼梯：动态规划"""
    if n == 1 or n == 2:
        return n

    # 初始化 dp 表，用于存储子问题的解
    dp = [0] * (n + 1)

    # 初始状态：预设最小子问题的解
    dp[1], dp[2] = 1, 2

    # 状态转移：从较小子问题逐步求解较大子问题
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(f'dp = {dp}')
    return dp[n]


"""
空间优化:
对于本问题，dp[i] 只与 dp[i-1] 和 dp[i-2] 有关，因此我们无须使用一个数组 dp 来存储所有子问题的解，而只需两个变量滚动前进即可。

观察以下代码，由于省去了数组 dp 占用的空间，因此空间复杂度从 O(n) 降至 O(1)。

在动态规划问题中，当前状态往往仅与前面有限个状态有关，这时我们可以只保留必要的状态，通过“降维”来节省内存空间。
这种空间优化技巧被称为“滚动变量”或“滚动数组”。
"""


def climbing_stairs_dp_comp(n: int) -> int:
    """爬楼梯：空间优化后的动态规划"""
    if n == 1 or n == 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    # res = climbing_stairs_dp(3)
    # res = climbing_stairs_dp(50)
    res = climbing_stairs_dp_comp(50)
    print(f'res = {res}')
