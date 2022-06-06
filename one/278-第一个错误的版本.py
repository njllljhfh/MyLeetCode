# -*- coding:utf-8 -*-
"""
278. 第一个错误的版本 (解题思路:二分查找 交互)
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。
由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

难度：简单
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：n = 5, bad = 4
输出：4
解释：
调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。


示例 2：
输入：n = 1, bad = 1
输出：1
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-bad-version
"""

bad = 1


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version >= bad:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n):
        """我的解法"""
        if n <= 1:
            return 1

        start = 1
        end = n

        # 二分查找
        while start <= end:
            middle = (start + end) // 2
            if isBadVersion(middle):
                if end - start <= 1:
                    print(f"start={start},end={end},middle={middle}")
                    return middle
                end = middle
            else:
                if end - start <= 1:
                    print(f"start={start},end={end},middle={middle}")
                    return end
                start = middle


class Solution2:
    def firstBadVersion(self, n):
        """
        力扣官方题解
        https://leetcode-cn.com/problems/first-bad-version/solution/di-yi-ge-cuo-wu-de-ban-ben-by-leetcode-s-pf8h/

        复杂度分析
        时间复杂度：O(log n)，其中 nn 是给定版本的数量。
        空间复杂度：O(1)，我们只需要常数的空间保存若干变量。
        """
        left = 1
        right = n

        # 二分查找
        while left < right:  # 循环直至区间左右端点相同
            # mid = left + (right - left) // 2  # 防止计算时溢出
            mid = (left + right) // 2  # 防止计算时溢出
            if isBadVersion(mid):
                right = mid  # 答案在区间 [left, mid] 中
            else:
                left = mid + 1  # 答案在区间 [mid+1, right] 中

        # 此时有 left == right，区间缩为一个点，即为答案
        return left


if __name__ == '__main__':
    # n = 5
    # bad = 4
    # n = 1
    # bad = 1
    # n = 5
    # bad = 1
    n = 2
    bad = 2

    solution = Solution2()
    res = solution.firstBadVersion(n)
    print(res)
