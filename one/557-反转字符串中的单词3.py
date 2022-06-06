# -*- coding:utf-8 -*-
"""
557. 反转字符串中的单词 III
给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

难度：简单
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：s = "Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

示例 2:
输入： s = "God Ding"
输出："doG gniD"
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
1 <= s.length <= 5 * 10^4
s 包含可打印的 ASCII 字符。
s 不包含任何开头或结尾空格。
s 里 至少 有一个词。
s 中的所有单词都用一个空格隔开。
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
"""


class Solution:
    """我的解法，O(n)"""

    def reverseWords(self, s: str) -> str:
        n = len(s)
        left = 0

        res = ''
        while left < n:
            temp = ''
            for letter in s[left:]:
                left += 1
                if letter != ' ':
                    temp = letter + temp
                else:
                    temp = temp + letter
                    break
            res = res + temp

        return res


if __name__ == '__main__':
    s = "Let's take LeetCode contes"
    # s = "Let's"

    solution = Solution()
    res = solution.reverseWords(s)
    print(res)
