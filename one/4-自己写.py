# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1 + len2
        p1 = 0
        p2 = 0

        if total == 0:
            return 0

        if total % 2 == 0:
            mid_index = [total // 2 - 1, total // 2]
        else:
            mid_index = [total // 2]

        mid = None
        for i in range(total):
            if p1 < len1:
                num1 = nums1[p1]
            else:
                num1 = None

            if p2 < len2:
                num2 = nums2[p2]
            else:
                num2 = None

            if num1 is None:
                mid = nums2[p2]
                p2 += 1
            elif num2 is None:
                mid = nums1[p1]
                p1 += 1
            else:
                if num1 < num2:
                    mid = nums1[p1]
                    p1 += 1
                else:
                    mid = nums2[p2]
                    p2 += 1

            if i == mid_index[0]:
                break

        if len(mid_index) == 1:
            return mid
        else:
            if p1 < len1:
                num1 = nums1[p1]
            else:
                num1 = None

            if p2 < len2:
                num2 = nums2[p2]
            else:
                num2 = None

            if num1 is None:
                mid2 = num2
            elif num2 is None:
                mid2 = num1
            else:
                mid2 = min(num1, num2)

            return (mid + mid2) / 2


if __name__ == '__main__':
    # num_ls1 = [1, 2]
    # num_ls2 = [3, 4]

    num_ls1 = [1, 2]
    num_ls2 = [3, 4, 4]

    # num_ls1 = []
    # num_ls2 = [1]

    res = Solution().findMedianSortedArrays(num_ls1, num_ls2)
    print(res)
