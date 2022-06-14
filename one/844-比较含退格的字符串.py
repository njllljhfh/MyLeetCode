# -*- coding:utf-8 -*-
"""
844. 比较含退格的字符串
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。
难度：简单
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。

示例 2：
输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。

示例 3：
输入：s = "a#c", t = "b"
输出：false
解释：s 会变成 "c"，但 t 仍然是 "b"。
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
1 <= s.length, t.length <= 200
s 和 t 只含有小写字母以及字符 '#'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

进阶：
你可以用 O(n) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

链接：https://leetcode.cn/problems/backspace-string-compare
"""


class Solution:
    """
    官方解法
    时间复杂度：O(n+m)，其中 n 和 m 分别为字符串 s 和 t 的长度。我们需要遍历两字符串各一次。
    空间复杂度：O(1)。对于每个字符串，我们只需要定义一个指针和一个计数器即可。
    链接：https://leetcode.cn/problems/backspace-string-compare/solution/bi-jiao-han-tui-ge-de-zi-fu-chuan-by-leetcode-solu/
    """

    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        skipS = 0  # s中待删除的字符的个数
        skipT = 0  # t中待删除的字符的个数

        while i >= 0 or j >= 0:
            while i >= 0:
                # 从右向左遍历s
                if s[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                # 从右向左遍历t
                if t[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    # s 和 t 中当前指向的要保留的字符 不相同
                    return False
                else:
                    # s 和 t 中当前指向的要保留的字符 相同
                    i -= 1
                    j -= 1
            elif i >= 0 or j >= 0:
                # i 和 j 其中一个 小于 0，另一个大于等于0（即，一个已经没有要保留的字符了，而另一个还有要保留的字符，所以 s 和 t 的文本结果一定定不相同）
                return False

        return True


if __name__ == '__main__':
    # s = "ab#c"
    # t = "ad#c"
    # s = "ab##"
    # t = "c#d#"
    s = "a#c"
    t = "b"

    res = Solution().backspaceCompare(s, t)
    print(res)
