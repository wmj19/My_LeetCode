from BinaryTree.utils import print_list
from LinkList1.Solutions import deleteDuplicates
from LinkList1.Solutions.Solutions import Solution
from LinkList1.structure.LinkList import LinkList, traverse


print("delete duplicates".center(50, '='))
link_list_delete_duplicates = LinkList()
link_list_delete_duplicates.insert(1)
link_list_delete_duplicates.insert(1)
link_list_delete_duplicates.insert(2)
link_list_delete_duplicates.insert(3)
link_list_delete_duplicates.insert(3)
link_list_delete_duplicates.insert(4)
link_list_delete_duplicates.insert(5)
link_list_delete_duplicates.insert(5)
link_list_delete_duplicates.insert(6)
print("link_list_delete_duplicates:")
traverse(link_list_delete_duplicates.head)
print("after delete duplicates")
res = deleteDuplicates(link_list_delete_duplicates.head)
traverse(res)

print("reverse list".center(40, "="))
link_reverse_list = LinkList()
link_reverse_list.insert(1)
link_reverse_list.insert(2)
link_reverse_list.insert(3)
link_reverse_list.insert(4)
link_reverse_list.insert(5)
link_reverse_list.insert(6)
res = Solution().reverse_list(link_reverse_list.head)
traverse(res)

print("is plain drome".center(40, '='))
link_plain_drome = LinkList()
link_plain_drome.insert(1)
link_plain_drome.insert(2)
link_plain_drome.insert(3)
link_plain_drome.insert(2)
link_plain_drome.insert(1)
res = Solution().is_palindrome(link_plain_drome.head)
print(res)

print("My Hash Map".center(40, "="))
test = [[1, 11], [2, 22], [3, 33]]
for key, val in test:
    print(f"key = {key}")
    print(f"val = {val}")

print("middle node".center(40, "="))
link_middle_node = LinkList()
link_middle_node.insert(1)
link_middle_node.insert(2)
link_middle_node.insert(3)
link_middle_node.insert(4)
link_middle_node.insert(5)
link_middle_node.insert(6)
res = Solution().middle_node(link_middle_node.head)
traverse(res)