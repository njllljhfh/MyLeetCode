# -*- coding:utf-8 -*-
"""
给定 n 种硬币，第 i 种硬币的面值为 coins[i-1]，目标金额为 amt ，每种硬币可以重复选取，
问能够凑出目标金额的最少硬币数量。如果无法凑出目标金额，则返回 -1 。


对于零钱兑换问题，贪心算法无法保证找到全局最优解，并且有可能找到非常差的解。它更适合用动态规划解决。
一般情况下，贪心算法的适用情况分以下两种。
    1.可以保证找到最优解：贪心算法在这种情况下往往是最优选择，因为它往往比回溯、动态规划更高效。
    2.可以找到近似最优解：贪心算法在这种情况下也是可用的。对于很多复杂问题来说，寻找全局最优解非常困难，能以较高效率找到次优解也是非常不错的。
"""


def coin_change_greedy(coins: list[int], amt: int) -> int:
    """零钱兑换：贪心"""
    # 假设 coins 列表有序
    i = len(coins) - 1
    count = 0

    # 循环进行贪心选择，直到无剩余金额
    while amt > 0:
        # 找到小于且最接近剩余金额的硬币
        while i > 0 and coins[i] > amt:
            i -= 1
        # 选择 coins[i]
        amt -= coins[i]
        count += 1

    # 若未找到可行方案，则返回 -1
    return count if amt == 0 else -1


if __name__ == "__main__":
    # 贪心：能够保证找到全局最优解
    coins = [1, 5, 10, 20, 50, 100]
    amt = 186
    res = coin_change_greedy(coins, amt)
    print(f"\ncoins = {coins}, amt = {amt}")
    print(f"凑到 {amt} 所需的最少硬币数量为 {res}")

    # 贪心：无法保证找到全局最优解
    coins = [1, 20, 50]
    amt = 60
    res = coin_change_greedy(coins, amt)
    print(f"\ncoins = {coins}, amt = {amt}")
    print(f"凑到 {amt} 所需的最少硬币数量为 {res}，即 50 + 1*10")
    print(f"实际上需要的最少数量为 3 ，即 20 + 20 + 20")

    # 贪心：无法保证找到全局最优解
    coins = [1, 49, 50]
    amt = 98
    res = coin_change_greedy(coins, amt)
    print(f"\ncoins = {coins}, amt = {amt}")
    print(f"凑到 {amt} 所需的最少硬币数量为 {res}，即 50 + 1*48")
    print(f"实际上需要的最少数量为 2 ，即 49 + 49")
