from typing import Optional

from tomlkit import value

from LinkList1.structure.ListNode import ListNode

class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre, cur, temp = None, head, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre

    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        value = []
        cur = head
        while cur:
            value.append(cur.val)
            cur = cur.next

        # mid = len(value) // 2
        #
        # for i in range(0, mid):
        #     if value[i] != value[len(value)-1-i]:
        #         return False
        # return True

        return value == value[::-1]