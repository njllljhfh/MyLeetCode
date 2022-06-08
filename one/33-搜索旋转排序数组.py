# -*- coding:utf-8 -*-
"""
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1。

难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-10^4 <= target <= 10^4
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

链接：https://leetcode.cn/problems/search-in-rotated-sorted-array
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """我的解法"""
        length = len(nums)
        left = 0
        right = length - 1

        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # 左边是有序的
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # nums[mid] < target
                    left = mid + 1
            else:
                # 右边是有序的
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # nums[mid] > target
                    right = mid - 1

        print(f'left={left},right={right}')
        return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     """官方解法"""
    #     if not nums:
    #         return -1
    #     l, r = 0, len(nums) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if nums[mid] == target:
    #             return mid
    #         if nums[0] <= nums[mid]:
    #             if nums[0] <= target < nums[mid]:
    #                 r = mid - 1
    #             else:
    #                 l = mid + 1
    #         else:
    #             if nums[mid] < target <= nums[len(nums) - 1]:
    #                 l = mid + 1
    #             else:
    #                 r = mid - 1
    #     return -1


if __name__ == '__main__':
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0
    # nums = [1, 3]
    # target = 3
    nums = [5, 1, 3]
    target = 3

    solution = Solution()
    result = solution.search(nums, target)
    print(result)
