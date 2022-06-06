# -*- coding:utf-8 -*-
"""
344. 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

难度：简单
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]

示例 2：
输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
1 <= s.length <= 10^5
s[i] 都是 ASCII 码表中的可打印字符
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string
"""
from typing import List


class Solution:
    """我的解法，O(n)"""

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        left = 0
        right = n - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    # s = ["H", "a", "n", "n", "a", "h"]

    solution = Solution()
    solution.reverseString(s)
    print(s)
