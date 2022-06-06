# -*- coding:utf-8 -*-
class Solution:
    """
    官方解法(优化后的滑动窗口)：https://leetcode.cn/problems/permutation-in-string/solution/zi-fu-chuan-de-pai-lie-by-leetcode-solut-7k7u/
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False

        # cnt[x] 是 s2中字符出现的次数 - s1中字符出现的次数
        cnt = [0] * 26  # 记录26个字母在s2和s1中出现的次数的差
        for i in range(n):
            cnt[ord(s1[i]) - ord('a')] -= 1
            cnt[ord(s2[i]) - ord('a')] += 1

        diff = 0
        for c in cnt:
            if c != 0:
                diff += 1

        if diff == 0:
            return True

        for i in range(n, m):
            x = ord(s2[i]) - ord('a')  # 右侧进入窗口的字符
            y = ord(s2[i - n]) - ord('a')  # 左侧移除窗口的字符

            # 若 x=y 则对cnt无影响，可以直接跳过
            if x == y:
                continue

            # 在修改 cnt 之前，cnt[x]=0,则将 diff 加 1
            if cnt[x] == 0:
                diff += 1

            cnt[x] += 1

            # 在修改 cnt 之后，cnt[x]=0,则将 diff 减 1
            if cnt[x] == 0:
                diff -= 1

            # 在修改 cnt 之前，cnt[y]=0,则将 diff 加 1
            if cnt[y] == 0:
                diff += 1

            cnt[y] -= 1

            # 在修改 cnt 之后，cnt[y]=0,则将 diff 减 1
            if cnt[y] == 0:
                diff -= 1

            if diff == 0:
                return True

        return False
