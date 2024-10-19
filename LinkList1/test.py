from LinkList1.Solutions import deleteDuplicates
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

