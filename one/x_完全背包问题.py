# -*- coding:utf-8 -*-
"""

"完全背包问题"

中等

给你一个整数数组 coins 表示不同面额的硬币，背包能装下的最大金额 amount 。
请你计算并返回可放入背包中的最大金额，返回 0 。
假设每一种面额的硬币有无限个。
题目数据保证结果符合 32 位带符号整数。


示例 1：
    输入：amount = 11, coins = [4, 5, 9]
    输出：10


提示：
    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    coins 中的所有值 互不相同
    0 <= amount <= 5000
"""
import timeit
from typing import List


class Solution(object):

    @classmethod
    def change(cls, amount: int, coins: List[int]) -> int:
        m = len(coins)
        dp = [[0] * (amount + 1) for _ in range(m + 1)]
        # print(dp)
        # print('---')

        for i in range(1, m + 1):
            for j in range(1, amount + 1):
                k = int(j / coins[i - 1])
                if k > 0:
                    # 优化前
                    dp[i][j] = max(
                        [
                            dp[i - 1][j - num * coins[i - 1]] + num * coins[i - 1]
                            for num in range(0, k + 1)
                        ]
                    )
                else:
                    dp[i][j] = dp[i - 1][j]

        # print(dp)
        return dp[m][amount]

    @classmethod
    def change_opt(cls, amount: int, coins: List[int]) -> int:
        m = len(coins)
        dp = [[0] * (amount + 1) for _ in range(m + 1)]
        # print(dp)
        # print('---')

        for i in range(1, m + 1):
            for j in range(1, amount + 1):
                k = int(j / coins[i - 1])
                if k > 0:
                    # 优化后
                    dp[i][j] = max(dp[i][j - coins[i - 1]] + coins[i - 1], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
                # ---

        # print(dp)
        return dp[m][amount]


if __name__ == '__main__':
    amount = 11
    coins = [4, 5, 9]

    res = Solution.change_opt(amount, coins)
    print(res)

    # number_of_runs = 100
    # # 测试函数a
    # time_change = timeit.timeit(lambda: Solution.change(amount, coins), number=number_of_runs)
    # avg_time_change = time_change / number_of_runs
    #
    # # 测试函数b
    # time_change_opt = timeit.timeit(lambda:  Solution.change_opt(amount, coins), number=number_of_runs)
    # avg_time_change_opt = time_change_opt / number_of_runs
    #
    # print(f"change: 总时间 {avg_time_change:.6f} 秒, 平均每次 {avg_time_change:.6f} 秒")
    # print(f"change_opt: 总时间 {avg_time_change_opt:.6f} 秒, 平均每次 {avg_time_change_opt:.6f} 秒")
    # print(f"性能比较: 函数 change_opt 是函数 change 的 {avg_time_change / avg_time_change_opt:.2f} 倍快")
