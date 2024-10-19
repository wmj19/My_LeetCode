from typing import Optional

from LinkList1.test import ListNode

# 单项链表的结构决定了，如果有环一定是最后一个节点不会指向None
# 如果是中间某个节点是环，那么这个链表都不完整

# T141
# 快慢指针, 龟兔赛跑算法

def has_cycle(head: Optional[ListNode]):

    if head is None or head.next is None:
        return False

    slow, fast = head, head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next

    return True