# -*- coding:utf-8 -*-


"""
148. 排序链表

难度：中等

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sort-list/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode

    def __repr__(self):
        return self._show_str()

    def _show_str(self):
        """把这个节点当做个位显示完整的数值"""
        if self.next is None:
            return f'{self.val}'
        else:
            # f'{self.next}' 会执行 next 节点的 __repr__ 方法
            return f'{self.val}{self.next}'


def newList(ls: list):
    list_node = None
    p = list_node
    for i in ls:
        if list_node is not None:
            p.next = ListNode(i)
            p = p.next
        else:
            list_node = ListNode(i)
            p = list_node
    return list_node


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        return sortFunc(head, None)


if __name__ == '__main__':
    list_node1 = newList([4, 2, 1, 3])
    print(f"list_node1 = {list_node1}")

    s = Solution()
    res = s.sortList(list_node1)
    print(f"res = {res}")
