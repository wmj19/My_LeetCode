# 83.删除列表重复元素
# 给定一个已排序的链表的头 head ，
# 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
from typing import Optional
from LinkList1.test import ListNode


def deleteDuplicatesSave(head: Optional[ListNode]) -> Optional[ListNode]:
    num = cur = head

    while num and num.next:
        while cur and cur.val == num.val:
            cur = cur.next
        num.next = cur
        if not num.next:
            break
        num = num.next

    return head