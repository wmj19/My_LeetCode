from typing import Optional
from ListNode import ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = cur = ListNode(next=head)
        cur = cur.next

        while cur and cur.next:
            if cur.next.val != cur.val:
                pre = cur
                cur = cur.next
            else:
                while True:
                    if cur.next and cur.next.val == cur.val:
                        cur = cur.next
                    else:
                        break
                pre.next = cur.next
                cur = cur.next
        return dummy.next

