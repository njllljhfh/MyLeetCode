# -*- coding:utf-8 -*-
"""
704. 二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

难度：简单
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """我的解法"""
        n = len(nums)

        # 3个指针,列表中的索引
        start = 0
        end = n - 1

        # 二分查找
        while start <= end:
            middle = (start + end) // 2
            if target < nums[middle]:
                end = middle - 1
            elif target > nums[middle]:
                start = middle + 1
            else:
                return middle

        return -1


if __name__ == '__main__':
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 9

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2

    solution = Solution()
    res = solution.search(nums, target)
    print(res)
