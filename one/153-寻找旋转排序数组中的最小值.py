# -*- coding:utf-8 -*-
"""
153. 寻找旋转排序数组中的最小值
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。(即向右旋转)

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

难读：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

示例 2：
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。

示例 3：
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数 互不相同
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

链接：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array
"""
from typing import List

"""
二分查找
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """我的解法"""
        length = len(nums)
        left = 0
        right = length - 1

        if length == 0:
            raise ValueError("输入列表不能为空列表")

        while left <= right:
            if nums[left] <= nums[right]:
                # 目标范围内的序列已经是升序
                print(f'left={left}, right={right}')
                return nums[left]

            mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                # 右侧是升序的, 目标范围调整为[left, mid]
                right = mid
            else:
                # 右侧是乱序的，目标范围调整为[mid+1, right]
                left = mid + 1

    # def findMin(self, nums: List[int]) -> int:
    #     """
    #     复杂度分析
    #     时间复杂度：时间复杂度为 O(log n)，其中 n 是数组 nums 的长度。在二分查找的过程中，每一步会忽略一半的区间，因此时间复杂度为 O(log n)。
    #     空间复杂度：O(1)。
    #     链接：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-5irwp/
    #     """
    #     low, high = 0, len(nums) - 1
    #     while low < high:
    #         pivot = low + (high - low) // 2
    #         if nums[pivot] < nums[high]:
    #             high = pivot
    #         else:
    #             low = pivot + 1
    #     return nums[low]


if __name__ == '__main__':
    # nums = [3, 4, 5, 1, 2]
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [11, 13, 15, 17]
    # nums = [19]
    # nums = [7, 0, 1, 3, 4, 6]
    nums = [6, 7, 0, 1, 3, 4]

    solution = Solution()
    result = solution.findMin(nums)
    print(result)
