# -*- coding:utf-8 -*-
"""
876. 链表的中间结点
给定一个头结点为 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。

难度：简单
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

示例 1：
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.

示例 2：
输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

提示：
给定链表的结点数介于 1 和 100 之间。
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/middle-of-the-linked-list
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MySolution:
    """我的解法，时间复杂度O(n)"""

    def middleNode(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = head

        i = 1  # 当前遍历的是第几个节点
        j = 1  # 以当前的 i 为最后一个节点，那么第 j 个节点是中间节点
        while p1:
            mid = i // 2 + 1
            if mid > j:
                p2 = p2.next
                j = mid
            i += 1
            p1 = p1.next

        return p2


class Solution:
    """
    方法三：快慢指针法
    思路和算法
    用两个指针 slow 与 fast 一起遍历链表。slow 一次走一步，fast 一次走两步。那么当 fast 到达链表的末尾时，slow 必然位于中间。

    复杂度分析
    时间复杂度：O(n)，其中 n 是给定链表的结点数目。
    空间复杂度：O(1)，只需要常数空间存放 slow 和 fast 两个指针。


    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/middle-of-the-linked-list/solution/lian-biao-de-zhong-jian-jie-dian-by-leetcode-solut/
    来源：力扣（LeetCode）
    """

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
