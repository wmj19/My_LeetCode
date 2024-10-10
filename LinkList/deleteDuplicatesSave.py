# 83.删除列表重复元素
# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from ListNode import ListNode

class Solution:
    def deleteDuplicatesSave(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = cur = head

        while num and num.next:
            while cur and cur.val == num.val:
                cur = cur.next
            num.next = cur
            if not num.next:
                break
            num = num.next

        return head