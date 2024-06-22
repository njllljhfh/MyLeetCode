# -*- coding:utf-8 -*-
"""
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

难度：中等
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例1：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
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
            return f'{self.next}{self.val}'


class Solution:
    @classmethod
    def addTwoNumbers(cls, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode(0)  # 哨兵节点
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


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         """这个算法修改了入参，个人认为不太好"""
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#         # 如果l1是短链表则交换l1和l2
#         cur1, cur2 = l1, l2
#         while cur1 and cur2:
#             cur1 = cur1.next
#             cur2 = cur2.next
#         if cur2:
#             l1, l2 = l2, l1
#         head1, head2 = l1, l2
#         temp = 0
#         # 记录l1的尾节点
#         tail = head1
#         while head1 or head2:
#             val2 = head2.val if head2 else 0
#             if head1.val + val2 + temp < 10:
#                 head1.val += (val2 + temp)
#                 temp = 0
#             else:
#                 head1.val = head1.val + val2 + temp - 10
#                 temp = 1
#             tail = head1
#             head1 = head1.next
#             head2 = head2.next if head2 else None
#         if temp:
#             tail.next = ListNode(1)
#         return l1


if __name__ == '__main__':
    # 测试数据1
    # ls1 = ListNode(2)
    # ls1.next = ListNode(4)
    # ls1.next.next = ListNode(3)
    # ls2 = ListNode(5)
    # ls2.next = ListNode(6)
    # ls2.next.next = ListNode(4)
    # ------------
    # 测试数据2
    # ls1 = ListNode(0)
    # ls2 = ListNode(0)
    # ------------
    # 测试数据3
    ls1 = ListNode(9)
    ls1.next = ListNode(9)
    ls1.next.next = ListNode(9)
    ls1.next.next.next = ListNode(9)
    ls2 = ListNode(8)
    ls2.next = ListNode(8)
    ls2.next.next = ListNode(8)
    # ------------
    print(f'ls1={ls1}')
    print(f'ls2={ls2}')

    ls_res = Solution().addTwoNumbers(ls1, ls2)
    print(f'ls_res={ls_res}')
