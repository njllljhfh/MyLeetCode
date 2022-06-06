# -*- coding:utf-8 -*-
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

难度：简单
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

进阶：你能尽量减少完成的操作次数吗？
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        官方解法：https://leetcode-cn.com/problems/move-zeroes/solution/yi-dong-ling-by-leetcode-solution/
        复杂度分析
        时间复杂度：O(n)，其中 n 为序列长度。每个位置至多被遍历两次。
        空间复杂度：O(1)。只需要常数的空间存放若干变量。
        """
        n = len(nums)
        left = 0  # 左指针指向当前已经处理好的序列的尾部的下一位置，也就是待处理序列中下一个非零数字要插入的位置
        right = 0  # 右指针指向待处理序列的头部
        i = 0  # 记录交换次数
        while right < n:
            if nums[right] != 0:
                if nums[left] == 0:
                    i += 1
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        print(f"交换次数 = {i}")


if __name__ == '__main__':
    # nums = [0, 1, 0, 3, 12]
    # nums = [1, 2, 0, 3, 12]
    nums = [1, 2, 3, 4, 0, 0, 5, 0, 12]

    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)
