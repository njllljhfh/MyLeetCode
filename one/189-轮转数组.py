# -*- coding:utf-8 -*-
"""
189. 轮转数组
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

进阶：
尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
"""
from typing import List


class MySolution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        我的解法
        时间复杂度应该是O(n*k)，n 是数组长度. 太慢了，不能用
        """
        n = len(nums)
        p = n - 1

        while k > 0:
            for i in range(p, 0, -1):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            k -= 1


class Solution:
    """
    方法三：数组翻转
    官方解法:https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-by-leetcode-solution-nipk/

    复杂度分析
    时间复杂度：O(n)，其中 n 为数组的长度。每个元素被翻转两次，一共 n 个元素，因此总时间复杂度为 O(2n)=O(n)。
    空间复杂度：O(1)。
    """

    def reverse(self, nums: list[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        # print(nums)
        self.reverse(nums, 0, k - 1)
        # print(nums)
        self.reverse(nums, k, n - 1)
        # print(nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    # nums = [-1, -100, 3, 99]
    # k = 2

    solution = Solution()
    solution.rotate(nums, k)
    print(nums)
