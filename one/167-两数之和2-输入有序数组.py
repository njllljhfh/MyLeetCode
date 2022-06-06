# -*- coding:utf-8 -*-
"""
167. 两数之和 II - 输入有序数组
给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列，
请你从数组中找出满足相加之和等于目标数 target 的两个数。
如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。
难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。

示例 2：
输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。

示例 3：
输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers 按 非递减顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
"""
from typing import List


class MySolution:
    """我的解法，速度有点慢，O(nlog n)"""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        # 3个指针,列表中的索引
        start = 1
        end = n - 1

        p1 = 0
        while p1 < n - 1:
            num = target - numbers[p1]
            p2 = self.binary_search(numbers, num, start, end)
            if p2 != -1:
                return [p1 + 1, p2 + 1]
            start += 1
            p1 += 1

        return []

    def binary_search(self, numbers: List[int], target: int, start: int, end: int) -> int:
        # 二分查找
        while start <= end:
            middle = (start + end) // 2
            if target < numbers[middle]:
                end = middle - 1
            elif target > numbers[middle]:
                start = middle + 1
            else:
                return middle
        return -1


class Solution:
    """
    官方解法：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/solution/suan-fa-si-wei-yang-cheng-ji-shuang-zhi-rqju0/
    # 双指针
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left = left + 1
            else:
                right = right - 1
        return []


if __name__ == '__main__':
    # numbers = [2, 7, 11, 15]
    # target = 9
    # numbers = [2, 3, 4]
    # target = 6
    # numbers = [-1, 0]
    # target = -1
    numbers = [5, 25, 75]
    target = 100

    solution = Solution()
    res = solution.twoSum(numbers, target)
    print(res)
