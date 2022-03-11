# -*- coding:utf-8 -*-
"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"wke" 是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
"""


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         """dragon自己实现的，此算法时间复杂度较高"""
#         len_s = len(s)
#         max_len = 0
#
#         for i in range(len_s):
#             sub_str = set()
#             for j in range(i, len_s):
#                 if s[j] not in sub_str:
#                     sub_str.add(s[j])
#                 else:
#                     break
#             new_len = len(sub_str)
#             max_len = new_len if new_len > max_len else max_len
#
#         return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        思路：
            这道题主要用到思路是：【滑动窗口】

        什么是滑动窗口？
            其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，
            当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

        如何移动？
            我们只要把队列的左边的元素移出就行了，直到满足题目要求！
            一直维持这样的队列，找出队列出现最长的长度时候，求出解！

        时间复杂度：O(n)

        作者：powcai
        链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
        来源：力扣（LeetCode）
        """
        if not s:
            return 0
        left = 0  # 【滑动窗口】最左边的元素的索引
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0

        for i in range(n):
            cur_len += 1

            while s[i] in lookup:  # 对 set类型 进行 in 操作的时间复杂度是 O(1)
                lookup.remove(s[left])
                left += 1
                cur_len -= 1

            if cur_len > max_len:
                max_len = cur_len

            lookup.add(s[i])
        return max_len


if __name__ == '__main__':
    s1 = 'pwwkew'
    # s1 = 'bbbbb'
    # s1 = " "
    print(Solution().lengthOfLongestSubstring(s1))
