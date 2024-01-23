# -*- coding:utf-8 -*-


"""
148. 排序链表

难度：中等

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表。
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
    @classmethod
    def addTwoNumbers(cls, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode(0)
        q = p  # p的第一个节点0在最终返回时被去掉了。q 是指向 p中第一个节点的指针。
        tmp = 0

        while l1 or l2 or tmp:
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next

            p.next = ListNode(tmp % 10)

            p = p.next  # p在循环中不断地重新指向结果数字的更高位节点
            tmp = tmp // 10

        return q.next


if __name__ == '__main__':
    list_node1 = newList([4, 2, 1, 3])
    print(f"list_node1 = {list_node1}")
