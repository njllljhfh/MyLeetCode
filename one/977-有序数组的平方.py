# -*- coding:utf-8 -*-
"""
977. 有序数组的平方
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

难度：简单
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums 已按 非递减顺序 排序
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

进阶：
请你设计时间复杂度为 O(n) 的算法解决本问题
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
"""
from typing import List


class MySolution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        我的解法
        复杂度分析
        时间复杂度：O(n*log n)，其中 nn 是数组 \textit{nums}nums 的长度。
        空间复杂度：O(log n)。除了存储答案的数组以外，我们需要 O(log n) 的栈空间进行排序。
        """
        answer = [num * num for num in nums]
        answer.sort()
        return answer


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        官方解法：https://leetcode-cn.com/problems/squares-of-a-sorted-array/solution/you-xu-shu-zu-de-ping-fang-by-leetcode-solution/

        复杂度分析
        时间复杂度：O(n)，其中 n 是数组 nums 的长度。
        空间复杂度：O(1)，除了存储答案的数组以外，我们只需要维护常量空间。
        """
        n = len(nums)
        answer = [0] * n

        i = 0
        j = n - 1
        pos = n - 1
        # 每次遍历取出当前剩余的数字中，平方最大的数，并将其倒序放到结果数组中
        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                answer[pos] = nums[i] * nums[i]
                i += 1
            else:
                answer[pos] = nums[j] * nums[j]
                j -= 1
            pos -= 1

        return answer


if __name__ == '__main__':
    # nums = [-4, -1, 0, 3, 10]
    nums = [-7, -3, 2, 3, 11]

    res = Solution().sortedSquares(nums)
    print(res)
