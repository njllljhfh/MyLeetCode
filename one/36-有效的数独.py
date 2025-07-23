# -*- coding:utf-8 -*-
"""
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

1.数字 1-9 在每一行只能出现一次。
2.数字 1-9 在每一列只能出现一次。
3.数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-sudoku/
"""
from pprint import pprint
import numpy as np
from typing import List


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         """
#         我的解法: 需要便利 3 次
#         :param board:
#         :return:
#         """
#         row_count = len(board)
#         column_count = len(board[0])
#
#         # 行
#         for row in board:
#             value_set = set()
#             for value in row:
#                 if value != '.':
#                     if value in value_set:
#                         return False
#                     else:
#                         value_set.add(value)
#
#         # 列
#         for col in range(column_count):
#             value_set = set()
#             for row in range(row_count):
#                 value = board[row][col]
#                 if value != '.':
#                     if value in value_set:
#                         return False
#                     else:
#                         value_set.add(value)
#
#         # 3*3块
#         step = row_count // 3
#         for row in range(0, row_count, step):
#             for col in range(0, column_count, step):
#                 value_set = set()
#                 for r in range(row, row + step):
#                     for c in range(col, col + step):
#                         value = board[r][c]
#                         if value != '.':
#                             if value in value_set:
#                                 return False
#                             else:
#                                 value_set.add(value)
#
#         return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        官方解法：只遍历了一次
        :param board:
        :return:
        """
        # rows[i][index]: i 表示行， index 表示数字 index+1(即 index=0 表示数字1)，对应的值表示 该数字在该行出现的次数
        rows = [[0] * 9 for _ in range(9)]

        # 同rows，表示列的数字次数
        columns = [[0] * 9 for _ in range(9)]

        # 表示每个3*3格子内，数字的出现次数
        subboxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v != '.':
                    num = int(v)
                    index = num - 1
                    rows[i][index] += 1
                    columns[j][index] += 1
                    subboxes[i // 3][j // 3][index] += 1
                    if rows[i][index] > 1 or columns[j][index] > 1 or subboxes[i // 3][j // 3][index] > 1:
                        # print(f"i={i},j={j},index={index}")
                        # pprint(rows)
                        # pprint(columns)
                        # pprint(subboxes)
                        return False
        return True


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         """
#         numpy 版
#         官方解法：只遍历了一次
#         :param board:
#         :return:
#         """
#         # rows[i][index]: i 表示行， index 表示数字 index+1(即 index=0 表示数字1)，对应的值表示 该数字在该行出现的次数
#         rows = np.zeros(shape=(9, 9), dtype=np.int8)
#
#         # 同rows，表示列的数字次数
#         columns = np.zeros(shape=(9, 9), dtype=np.int8)
#
#         # 表示每个3*3格子内，数字的出现次数
#         subboxes = np.zeros(shape=(3, 3, 9), dtype=np.int8)
#
#         for i in range(9):
#             for j in range(9):
#                 v = board[i][j]
#                 if v != '.':
#                     num = int(v)
#                     index = num - 1
#                     rows[i][index] += 1
#                     columns[j][index] += 1
#                     subboxes[i // 3][j // 3][index] += 1
#                     if rows[i][index] > 1 or columns[j][index] > 1 or subboxes[i // 3][j // 3][index] > 1:
#                         return False
#         return True


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]  # True

    # board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
    #          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #          [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #          [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]  # False

    print(Solution().isValidSudoku(board))
