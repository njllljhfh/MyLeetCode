# -*- coding:utf-8 -*-
"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

链接：https://leetcode.cn/problems/3sum
"""
from typing import List


class Solution:
    """
    官方解法
    时间复杂度：O(n^2) 其中 n 是数组 nums 的长度。
    空间复杂度：O(log n)。我们忽略存储答案的空间，额外的排序的空间复杂度为 O(log n)。然而我们修改了输入的数组 nums，
             在实际情况下不一定允许，因此也可以看成使用了一个额外的数组存储了 nums 的副本并进行排序，空间复杂度为 O(n)。
    链接：https://leetcode.cn/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0]

    res = Solution().threeSum(nums)
    print(res)
