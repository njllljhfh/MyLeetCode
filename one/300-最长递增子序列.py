# -*- coding:utf-8 -*-
"""
300. 最长递增子序列

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。


示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1


难度: 中等
https://leetcode.cn/problems/longest-increasing-subsequence/
"""

from typing import List


# class Solution:
#     """动态规划"""
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         length = len(nums)
#         dp = [0] * length  # 以nums中每个元素为结尾的 最大递增子序 的长度。dp的index 与 nums的index 对应
#
#         if dp:
#             dp[0] = 1
#             maxLength = 1
#         else:
#             maxLength = 0
#
#         for i in range(1, length):
#             dp[i] = 1
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     maxLength = max(dp[i], maxLength)
#         return maxLength

# class Solution:
#     def lengthOfLIS(self, nums: [int]) -> int:
#         tails, res = [0] * len(nums), 0
#         for num in nums:
#             i, j = 0, res
#             while i < j:
#                 m = (i + j) // 2
#                 if tails[m] < num:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
#                     i = m + 1
#                 else:
#                     j = m
#             tails[i] = num
#             if j == res:
#                 res += 1
#         return res

class Solution:
    """
    贪心 + 二分查找
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)


if __name__ == '__main__':
    # a = [10, 9, 2, 5, 3, 7, 1, 18]  # 4
    # a = [4, 10, 4, 3, 8, 9]  # 3
    # a = [0, 1, 0, 3, 2, 3]  # 4
    # a = [7, 7, 7, 7, 7, 7, 7]  # 1
    a = [0, 1, 3, 4, 5, 6, 7, 8, 2, 3]
    res = Solution().lengthOfLIS(a)
    print(f"长度为：{res}")
