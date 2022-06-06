# -*- coding:utf-8 -*-
"""
1305. 两棵二叉搜索树中的所有元素
给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：

每棵树的节点数在 [0, 5000] 范围内
-105 <= Node.val <= 105
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        方法一：中序遍历 + 归并
        来源：https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/solution/liang-ke-er-cha-sou-suo-shu-zhong-de-suo-you-yua-3/
        时间复杂度：O(n+m)O(n+m)，其中 nn 和 mm 分别为两棵二叉搜索树的节点个数。
        空间复杂度：O(n+m)O(n+m)。存储数组以及递归时的栈空间均为 O(n+m)O(n+m)。
        :param root1:
        :param root2:
        :return:
        """

        def inorder(node: TreeNode, res: List[int]):
            """二叉树的中序遍历"""
            if node:
                inorder(node.left, res)
                res.append(node.val)
                inorder(node.right, res)

        # 中序遍历
        nums1, nums2 = [], []
        inorder(root1, nums1)
        inorder(root2, nums2)

        # 归并排序
        merged = []
        p1, n1 = 0, len(nums1)
        p2, n2 = 0, len(nums2)
        while True:
            if p1 == n1:
                merged.extend(nums2[p2:])
                break
            if p2 == n2:
                merged.extend(nums1[p1:])
                break
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        return merged
