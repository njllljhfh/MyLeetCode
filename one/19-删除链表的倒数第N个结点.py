# -*- coding:utf-8 -*-
"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

进阶：你能尝试使用一趟扫描实现吗？
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    官方解法：
    复杂度分析
    时间复杂度：O(n)，其中 n 是链表的长度。
    空间复杂度：O(1))。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/
    来源：力扣（LeetCode）
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 使用快慢指针
        dummy = ListNode(0, head)
        first = head  # 快指针
        second = dummy  # 慢指针

        # 先移动快指针
        for i in range(n):
            first = first.next

        # 同时移动快指针和慢指针
        while first:
            first = first.next
            second = second.next
        # while结束时：second 指向要删除的节点的上一个节点

        second.next = second.next.next
        return dummy.next
