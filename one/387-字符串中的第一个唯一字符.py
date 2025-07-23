# -*- coding:utf-8 -*-

"""
387-字符串中的第一个唯一字符.py

难度：简单

示例 1：
输入: s = "leetcode"
输出: 0

示例 2:
输入: s = "loveleetcode"
输出: 2

示例 3:
输入: s = "aabb"
输出: -1


提示:
1 <= s.length <= 10^5
s 只包含小写字母

https://leetcode.cn/problems/first-unique-character-in-a-string/
"""


# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         """
#         没有利用到 s只包含小写字母 的条件
#         :param s:
#         :return:
#         """
#         sToNum = {}
#         for item in s:
#             sToNum.setdefault(item, 0)
#             sToNum[item] += 1
#
#         for i in range(len(s)):
#             if sToNum[s[i]] == 1:
#                 return i
#
#         return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        min_unique_char_index = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":  # 利用到了，s只包含小写字母的条件
            i = s.find(c)
            if i != -1 and i == s.rfind(c):
                min_unique_char_index = min(min_unique_char_index, i)
        return min_unique_char_index if min_unique_char_index != len(s) else -1


if __name__ == '__main__':
    # s = "leetcode"  # 0
    s = "loveleetcode"  # 2
    # s = "aabb"  # -1

    print(Solution().firstUniqChar(s))
