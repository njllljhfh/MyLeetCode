# -*- coding:utf-8 -*-
"""
给定一棵二叉树的前序遍历 preorder 和中序遍历 inorder ，请从中构建二叉树，返回二叉树的根节点。假设二叉树中没有值重复的节点。

https://www.hello-algo.com/chapter_divide_and_conquer/build_binary_tree_problem/
"""


class TreeNode:
    """二叉树节点类"""

    def __init__(self, val: int = 0):
        self.val: int = val  # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用


def dfs(
        preorder: list[int],
        inorder_map: dict[int, int],
        i: int,
        l: int,
        r: int,
) -> TreeNode | None:
    """
    构建二叉树：分治
    :param i: 当前树的根节点在 preorder 中的索引记为
    :param l: 当前树在 inorder 中的索引区间的左边界
    :param r: 当前树在 inorder 中的索引区间的右边界
    """
    # 子树区间为空时终止
    if r - l < 0:
        return None

    # 初始化根节点
    root = TreeNode(preorder[i])

    # 查询 m ，从而划分左右子树（当前树的根节点在 inorder 中的索引记为 m）
    m = inorder_map[preorder[i]]

    # 子问题：构建左子树
    root.left = dfs(preorder, inorder_map, i + 1, l, m - 1)

    # 子问题：构建右子树
    # 右子树根节点索引中的 (m - l) 的含义是"左子树的节点数量"
    root.right = dfs(preorder, inorder_map, i + 1 + m - l, m + 1, r)

    # 返回根节点
    return root


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """构建二叉树"""
    # 初始化哈希表，存储 inorder 元素到索引的映射
    inorder_map = {val: i for i, val in enumerate(inorder)}
    root = dfs(preorder, inorder_map, 0, 0, len(inorder) - 1)
    return root


"""Driver Code"""
if __name__ == "__main__":
    preorder = [3, 9, 2, 1, 7]
    inorder = [9, 3, 1, 2, 7]
    print(f"前序遍历 = {preorder}")
    print(f"中序遍历 = {inorder}")
    root = build_tree(preorder, inorder)
