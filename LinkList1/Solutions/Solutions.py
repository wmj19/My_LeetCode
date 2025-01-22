from typing import Optional

from tomlkit import value

from LinkList1.structure.ListNode import ListNode
from LinkList1.structure.LinkList import LinkList,traverse

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

    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        quick, slow = ListNode(), ListNode()
        quick.next, slow.next = head, head
        while quick:
            slow = slow.next
            quick = quick.next
            if quick:
                quick = quick.next
        return  slow

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # leet code的链表是不带头节点的！！！
        # 经典快慢指针的应用，快的先走N步，
        # 快指针走到最后一个节点时，慢指针就刚好指向要删除的倒数第N个结点的前一个
        pre = cur = dummy = ListNode(next=head)
        for _ in range(n):
            pre = pre.next

        while pre.next:
            pre = pre.next
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next


if __name__ == "__main__":
    linklist = LinkList()
    linklist.insert(1)
    traverse(linklist.head)
    traverse(Solution().removeNthFromEnd(linklist.head, n=1))