# -*- coding:utf-8 -*-
"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
只会存在一个有效答案
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
"""


class Solution(object):
    def twoSum(self, nums: [int, ...], target: int) -> [int, int]:
        """时间复杂度：O(n)"""
        # 生成 value 到 index 的映射
        hash_map = {}
        for ind, num in enumerate(nums):
            hash_map[num] = ind

        # 通过hash表的key来查找，时间复杂度为 O(1)
        for ind, num in enumerate(nums):
            j = hash_map.get(target - num)
            if j is not None and j != ind:
                return [ind, j]


class Solution2(object):
    def twoSum(self, nums, target):
        """时间复杂度：O(n)"""
        hashmap = {}
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None:
                return [j, i]
            hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


if __name__ == '__main__':
    # s = Solution()
    s = Solution2()
    nums = [2, 7, 11, 15]
    target = 9
    result = s.twoSum(nums, target)
    print(result)
