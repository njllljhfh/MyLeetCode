# -*- coding:utf-8 -*-
"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums 是一个非递减数组
-10^9 <= target <= 10^9
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
from typing import List

"""
二分查找
"""


class Solution:
    """
    官方解法-视频讲解中的解法
    复杂度分析
    时间复杂度： O(log n)，其中 n 为数组的长度。二分查找的时间复杂度为 O(log n)，一共会执行两次，因此总时间复杂度为 O(log n)。
    空间复杂度：O(1) 。只需要常数空间存放若干变量。
    链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-de-di-3-4/
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 0:
            return [-1, -1]

        firstPosition = self._findFistPosition(nums, target)
        if firstPosition == -1:
            return [-1, -1]

        lastPosition = self._findLastPosition(nums, target)

        return [firstPosition, lastPosition]

    def _findFistPosition(self, nums, target):
        """寻找第一次出现的位置"""
        left = 0
        right = len(nums) - 1

        while left < right:
            # mid = int((left + right) / 2)
            mid = (left + right) >> 1
            if nums[mid] < target:
                # 目标值在[mid+1, right]
                left = mid + 1
            elif nums[mid] == target:
                # 目标值在[left, mid]
                right = mid
            else:
                # nums[mid] > target
                # 目标值在[left, mid-1]
                right = mid - 1

        if nums[left] != target:
            return -1
        else:
            return left

    def _findLastPosition(self, nums, target):
        """寻找最后一次出现的位置"""
        left = 0
        right = len(nums) - 1

        while left < right:
            # mid = int((left + right + 1) / 2)
            mid = (left + right + 1) >> 1  # 这里必须向上取整，否则可能在 nums[mid] == target 时进入死循环.
            if nums[mid] < target:
                # 目标值在[mid+1, right]
                left = mid + 1
            elif nums[mid] == target:
                # 目标值在[mid, right]
                left = mid
            else:
                # nums[mid] > target
                # 目标值在[left, mid-1]
                right = mid - 1
        return left


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    solution = Solution()
    result = solution.searchRange(nums, target)
    print(result)
