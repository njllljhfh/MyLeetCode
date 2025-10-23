# -*- coding:utf-8 -*-

"""
记忆化搜索是一种“从顶至底”的方法：
    我们从原问题（根节点）开始，递归地将较大子问题分解为较小子问题，直至解已知的最小子问题（叶节点）。
    之后，通过回溯逐层收集子问题的解，构建出原问题的解。
"""


def dfs(i: int, mem: list[int]) -> int:
    """记忆化搜索"""
    # 已知 dp[1] 和 dp[2] ，返回之
    if i == 1 or i == 2:
        mem[i] = i
        return i

    # 若存在记录 dp[i] ，则直接返回之
    if mem[i] != -1:
        return mem[i]

    # dp[i] = dp[i-1] + dp[i-2]
    count = dfs(i - 1, mem) + dfs(i - 2, mem)

    # 记录 dp[i]
    mem[i] = count
    return count


def climbing_stairs_dfs_mem(n: int) -> int:
    """爬楼梯：记忆化搜索"""
    # mem[i] 记录爬到第 i 阶的方案总数，-1 代表无记录
    mem = [-1] * (n + 1)
    res = dfs(n, mem)
    print(f'mem = {mem}')
    return res


if __name__ == "__main__":
    res = climbing_stairs_dfs_mem(3)
    # res = climbing_stairs_dfs_mem(50)
    print(f'res = {res}')
