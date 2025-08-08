# -*- coding:utf-8 -*-
"""
给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。
其中第 i 个物品的重量为 wt[i]，价值为 val[i]，现在让你用这个背包装物品，最多能装的价值是多少？
"""
from pprint import pprint

from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray


class Solution(object):

    @classmethod
    def main(cls, W, N, wt: list, val: list):

        # dp[i][w] 的定义如下：对于前 i 个物品，当前背包的容量为 w，这种情况下可以装的最大价值是 dp[i][w]
        # 边界条件：
        #   1. dp[0][...] = 0
        #   2. dp[...][0] = 0
        dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
        print(dp)
        print('---')

        for i in range(1, N + 1):  # 前 i 个物品
            for w in range(1, W + 1):  # 背包总容量为 w
                # i - 1: 是当前这个物品在 wt 和 val 中的 index，因为i是从1开始的，所以 index 要减 1
                # 去掉当前全部i个物品中的最后一个物品的重量后，背包剩余的可用重量
                history_w = w - wt[i - 1]
                if history_w < 0:
                    print(f"i={i}, w={w}")
                    dp[i][w] = dp[i - 1][w]
                else:
                    final_value_ls = [
                        dp[i - 1][history_w] + val[i - 1],
                        dp[i - 1][w]
                    ]
                    dp[i][w] = max(final_value_ls)

        pprint(dp, width=40)
        return dp[N][W]

    @classmethod
    def main_2(cls, W, N, wt: list, val: list):

        # dp[i][w] 的定义如下：对于前 i 个物品，当前背包的容量为 w，这种情况下可以装的最大价值是 dp[i][w]
        # 边界条件：
        #   1. dp[0][...] = 0
        #   2. dp[...][0] = 0
        # dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
        #
        # for i in range(1, N + 1):  # 前 i 个物品
        #     for w in range(1, W + 1):  # 背包总容量为 w
        #         # i - 1: 是当前这个物品在 wt 和 val 中的 index，因为i是从1开始的，所以 index 要减 1
        #         # 去掉当前全部i个物品中的最后一个物品的重量后，背包剩余的可用重量
        #         history_w = w - wt[i - 1]
        #         if history_w < 0:
        #             print(f"i={i}, w={w}")
        #             dp[i][w] = dp[i - 1][w]
        #         else:
        #             final_value_ls = [
        #                 dp[i - 1][history_w] + val[i - 1],
        #                 dp[i - 1][w]
        #             ]
        #             dp[i][w] = max(final_value_ls)

        dp = [0 for _ in range(W + 1)]
        for i, v in enumerate(val):  # 遍历硬币
            for w in range(W - wt[i], W + 1):
                dp[w] += dp[w - wt[i]]
        return dp[W]


if __name__ == '__main__':
    wt = [2, 1, 3]
    val = [4, 2, 3]

    w = 4  # 背包最大可装载重量
    n = len(wt)

    # res = Solution.main(w, n, wt, val)
    # print(res)
    print('---')
    res = Solution.main_2(w, n, wt, val)
    print(res)

    # for i in range(1, 11)[::-1]:
    #     print(i)
