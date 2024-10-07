from ListNode import *
from mergeTwoLists import *

if __name__ == "__main__":

    def print_link(head):
        cur = head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next

    print_link(list1)
    print()
    print_link(list2)
    print()

    solution = Solution()
    res = solution.mergeTwoLists(list1, list2)
    print(type(res))
    print_link(res)