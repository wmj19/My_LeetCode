# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from all_package import *

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        pre = dummy_1 = ListNode(next=head)
        bigger_or_equal = dummy_2 = ListNode()
        cur = head

        while cur:
            if cur.val >= x:
                bigger_or_equal.next = cur
                bigger_or_equal = bigger_or_equal.next
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next

        # 如果不设置，bigger_or_equal的最后一个结点如果在原先的链表里不是最后一个结点，
        # 则会连到原先的下一个结点上去，形成一个环
        bigger_or_equal.next = None

        if dummy_2.next:
            pre.next = dummy_2.next

        return dummy_1.next