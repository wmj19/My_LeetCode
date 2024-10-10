from all_package import *

# 使用两个指针，pre指向前驱，cur指向当前节点
# cur指向的节点如果和后续值相同，则往后遍历
# 直到找到val相同的结点的最后一个，然后让pre.next = cur.next cur = cur.next

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

