# -*- coding:utf-8 -*-
"""
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

难度：困难
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

中位数定义：https://baike.baidu.com/item/%E4%B8%AD%E4%BD%8D%E6%95%B0/3087401
"""
from typing import List

# class Solution:
#     @classmethod
#     def findMedianSortedArrays(cls, nums1: List[int], nums2: List[int]) -> float:
#         """时间复杂度：O(m + n)"""
#         len1 = len(nums1)
#         len2 = len(nums2)
#         total_len = len1 + len2
#         if total_len == 0:
#             return -1.0
#
#         left = -1  # 两个连续数中的上一个数
#         right = -1  # 两个连续数中的下一个数
#         index1 = 0
#         index2 = 0
#
#         # 总长度为奇数时：循环次数为总长度的一半向上取整
#         # 总长度为偶数时：循环次数为总长度的一半加1
#         for _ in range(total_len // 2 + 1):
#             left = right
#             if index1 < len1 and (index2 >= len2 or nums1[index1] < nums2[index2]):
#                 # 先用index1取值, 用完再将其加1
#                 right = nums1[index1]
#                 index1 += 1
#             else:
#                 # 先用index2取值, 用完再将其加1
#                 right = nums2[index2]
#                 index2 += 1
#         if (total_len & 1) == 0:  # 按位与
#             # 总长度为偶数
#             return (left + right) / 2.0
#         else:
#             # 总长度为奇数
#             return right

INT_MAX = 1000001


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        思路：找第k小数
        时间复杂度：O(long(m + n))
        """
        m = len(nums1)  # 取原始数组长度
        n = len(nums2)
        nums1.append(INT_MAX)  # 追加哨兵位, 解决索引越界
        nums2.append(INT_MAX)
        k = (m + n + 1) // 2  # 获取中间数是第几个数（偶数取前一个数）
        idx1 = 0  # 遍历指针，指向当前取得数组的元素
        idx2 = 0
        flag = False  # 标记中间数取的是否为nums1的元素
        while True:
            # 数组1元素全部取完，剩下的元素由数组2提供
            if idx1 == m:
                # [idx2, ?]提供k个元素，即?-idx2+1=k => ? = idx2+k-1
                idx2 += k - 1
                break
            # 数组2元素全部取完，剩下的元素由数组1提供
            if idx2 == n:
                idx1 += k - 1
                flag = True
                break
            # 为了使指针停在中间数的位置，最后一个数单独处理
            if k == 1:
                flag = nums1[idx1] < nums2[idx2]  # 指针无需移动，只需要判断取哪个数组的元素
                break

            # 每次两个数组各出k/2的元素，然后取数字更小的那一组
            half = k // 2
            mid1 = min(idx1 + half, m) - 1  # [idx1, mid1] 范围元素，确保mid1不越界
            mid2 = min(idx2 + half, n) - 1
            # mid1更小，那么mid1一定不会是第k个数，因此淘汰[idx1, mid1]往后找；否则淘汰[idx2, mid2]往后找
            # k减少对应区间的元素个数 idx-mid + 1
            if nums1[mid1] < nums2[mid2]:
                k -= mid1 - idx1 + 1
                idx1 = mid1 + 1
            else:
                k -= mid2 - idx2 + 1
                idx2 = mid2 + 1

        # 总元素个数为奇数，直接返回中间数，根据flag判断中间数是在nums1还是在nums2
        if (m + n) & 1:
            return nums1[idx1] if flag else nums2[idx2]

        # 总元素个数为偶数，不仅要取中间数，还要取中间数的后一位取平均
        # 根据flag判断中间数是在nums1还是在nums2，中间数的下一个数要么是中间数同数组的后一位，要么是另一个数组的当前指向元素
        if flag:
            return (nums1[idx1] + min(nums1[idx1 + 1], nums2[idx2])) / 2
        else:
            return (nums2[idx2] + min(nums2[idx2 + 1], nums1[idx1])) / 2


if __name__ == '__main__':
    num_ls1 = [1, 2]
    num_ls2 = [3, 4]

    # num_ls1 = [1, 2]
    # num_ls2 = [3, 4, 4]

    # num_ls1 = []
    # num_ls2 = []

    res = Solution().findMedianSortedArrays(num_ls1, num_ls2)
    print(res)
