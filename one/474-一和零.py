# -*- coding:utf-8 -*-
"""
474. 一和零
https://leetcode.cn/problems/ones-and-zeroes/description/
中等

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。


示例 1：
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。


示例 2：
输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。


提示：
1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100
"""
from typing import List


# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         length = len(strs)
#         # 3维dp
#         dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]
#         for i in range(1, length + 1):
#             c0 = strs[i - 1].count("0")  # 当前字符串中 0 的个数
#             c1 = len(strs[i - 1]) - c0  # 当前字符串中 1 的个数
#             for j in range(m + 1):
#                 for k in range(n + 1):
#                     if j >= c0 and k >= c1:
#                         dp[i][j][k] = max(
#                             dp[i - 1][j - c0][k - c1] + 1,  # 子集中放入当前 str
#                             dp[i - 1][j][k]  # 子集中不放入当前 str
#                         )
#                     else:
#                         dp[i][j][k] = dp[i - 1][j][k]
#
#         return dp[length][m][n]

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        # 3维dp: 记录各个状态的子集
        dp = [[[''] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]
        for i in range(1, length + 1):
            c0 = strs[i - 1].count("0")  # 当前字符串中 0 的个数
            c1 = len(strs[i - 1]) - c0  # 当前字符串中 1 的个数
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= c0 and k >= c1:
                        # if len(dp[i - 1][j - c0][k - c1]) + 1 > len(dp[i - 1][j][k]):
                        if dp[i - 1][j - c0][k - c1].count(' ') + 1 > dp[i - 1][j][k].count(' '):
                            t = f'{dp[i - 1][j - c0][k - c1]} {i - 1}'.strip()  # 记录子集中字符串的索引
                            dp[i][j][k] = t
                        else:
                            dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        # 处理没有符合要求的子集的边界情况
        if dp[length][m][n] != '':
            index_ls = dp[length][m][n].split(' ')
        else:
            index_ls = []
        final_subset = [strs[int(index)] for index in index_ls]
        print(f"final_subset = {final_subset}")
        return len(final_subset)


if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5  # m 个 0
    n = 3  # n 个 1

    # strs = ["10", "0", "1"]
    # m = 1
    # n = 1

    # strs = ["10", "0001", "111001", "1", "0"]
    # m = 1
    # n = 1

    # strs = ["00", "000"]
    # m = 1
    # n = 10

    res = Solution().findMaxForm(strs, m, n)
    print(res)
