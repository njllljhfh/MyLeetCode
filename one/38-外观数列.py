# -*- coding:utf-8 -*-
"""
难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/count-and-say/description/
"""


# class Solution:
#     """我的解法"""
#
#     def countAndSay(self, n: int) -> str:
#         r = "1"
#         for i in range(2, n + 1):
#             r = self.describe(f"{r}")
#         return r
#
#     def describe(self, s: str):
#         result = []
#
#         left = 0
#         right = 0
#         length = len(s)
#
#         while right < length:
#             if s[left] == s[right]:
#                 right += 1
#             else:
#                 result.append(f"{right - left}{s[left]}")
#                 left = right
#
#             if right == length:
#                 result.append(f"{right - left}{s[left]}")
#
#         return "".join(result)

class Solution:
    """
    官方解法
    njl做了优化，去掉了切片，改用索引
    """

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        res = ["1", "1"]

        for i in range(3, n + 1):
            new_res = []
            length = len(res)
            left = 0
            right = 0

            while right < length:
                if res[left] == res[right]:
                    right += 1
                else:
                    new_res.append(f"{right - left}")
                    new_res.append(f"{res[left]}")
                    left = right

                # 尾部的数
                if right == length:
                    new_res.append(f"{right - left}")
                    new_res.append(f"{res[left]}")

            res = new_res

        return "".join(res)


if __name__ == '__main__':
    # print(Solution().describe('1'))

    print(Solution().countAndSay(1))
    print(Solution().countAndSay(2))
    print(Solution().countAndSay(3))
    print(Solution().countAndSay(4))
    print(Solution().countAndSay(5))
    print(Solution().countAndSay(6))
