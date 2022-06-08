# -*- coding:utf-8 -*-
"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
- 每行中的整数从左到右按升序排列。
- 每行的第一个整数大于前一行的最后一个整数。

难读：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

链接：https://leetcode.cn/problems/search-a-2d-matrix
"""
from typing import List

# import time

"""
二分查找
"""


# class Solution:
#     """我的解法"""
#
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])
#         print(f"m={m}, n={n}")
#
#         start = (0, 0)
#         end = (m - 1, n - 1)
#
#         # 二分查找
#         while self._position_to_order(start, n) <= self._position_to_order(end, n):
#             mid_order = (self._position_to_order(start, n) + self._position_to_order(end, n) + 1) // 2
#             mid = self._order_to_position(mid_order, n)
#             if target < matrix[mid[0]][mid[1]]:
#                 end = self._order_to_position(mid_order - 1, n)
#             elif target > matrix[mid[0]][mid[1]]:
#                 start = self._order_to_position(mid_order + 1, n)
#             else:
#                 return True
#
#             # print(f"mid_order={mid_order}")
#             # print(f"mid={mid}")
#             # print(f"start={start}")
#             # print(f"end={end}")
#             # print("- " * 10)
#             # time.sleep(0.5)
#
#         return False
#
#     @classmethod
#     def _position_to_order(cls, position: tuple, n: int) -> int:
#         """
#         计算该位置在升序矩阵中序号
#         :param position: 位置(行号, 列号)
#         :param n: 列数
#         :return:
#         """
#         return position[0] * n + position[1]
#
#     @classmethod
#     def _order_to_position(cls, order: int, n: int) -> tuple:
#         """
#         根据升序矩阵中序号，计算该序号在矩阵中的位置
#         :param order:
#         :param n: 列数
#         :return: (行号, 列号)
#         """
#         return order // n, order % n


class Solution:
    """
    官方解法
    复杂度分析
    时间复杂度：O(log mn)，其中 m 和 n 分别是矩阵的行数和列数。
    空间复杂度：O(1)。
    连接：https://leetcode.cn/problems/search-a-2d-matrix/solution/sou-suo-er-wei-ju-zhen-by-leetcode-solut-vxui/
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1
        while low <= high:
            mid = (high + low) // 2
            x = matrix[mid // n][mid % n]
            if x < target:
                low = mid + 1
            elif x > target:
                high = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':
    # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # target = 3
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    # matrix = [[1]]
    # target = 1

    solution = Solution()
    result = solution.searchMatrix(matrix, target)
    print(result)
