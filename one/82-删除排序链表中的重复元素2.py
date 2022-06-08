# -*- coding:utf-8 -*-
"""
82. 删除排序链表中的重复元素 II
给定一个 已排序的 链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字。返回 已排序的链表 。

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2
输入：head = [1,1,1,2,3]
输出：[2,3]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

链接:https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        官方解法
        复杂度分析
        时间复杂度：O(n)，其中 n 是链表的长度。
        空间复杂度：O(1)。
        链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/solution/shan-chu-pai-xu-lian-biao-zhong-de-zhong-oayn/
        :param head:
        :return:
        """
        dummyNode = ListNode(val=0, next=head)  # dummyNode 傀儡节点
        cur = dummyNode  # cur 指向到目前为止，要保留的节点
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    # 去掉值为x的所有节点
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummyNode.next
