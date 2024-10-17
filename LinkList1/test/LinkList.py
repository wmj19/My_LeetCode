from ListNode import ListNode
from LinkList1.Solutions.deleteDuplicates import deleteDuplicates
from LinkList1.Solutions.deleteDuplicatesSave import deleteDuplicatesSave

class LinkList:
    def __init__(self):
        self.head = None  # 链表头节点

    # 在链表末尾插入节点
    def insert(self, value):
        new_node = ListNode(value)
        if self.head is None:  # 如果链表为空，直接将新节点设为头节点
            self.head = new_node
        else:
            current = self.head
            while current.next:  # 遍历到链表的末尾
                current = current.next
            current.next = new_node  # 在末尾插入新节点

    # 删除节点（按值删除第一个匹配的节点）
    def delete(self, value):
        current = self.head
        if current is None:
            return  # 链表为空，直接返回
        if current.val == value:  # 如果头节点就是要删除的节点
            self.head = current.next
            current = None
            return
        previous = None
        while current and current.val != value:  # 遍历链表查找要删除的节点
            previous = current
            current = current.next
        if current is None:  # 未找到节点
            return
        previous.next = current.next  # 将当前节点从链表中移除
        current = None

    # 查找节点
    def search(self, value):
        current = self.head
        while current:
            if current.val == value:
                return current  # 返回找到的节点
            current = current.next
        return None  # 如果未找到，返回None

# 遍历链表
def traverse(head):
    current = head
    while current:  # 直到遍历到末尾
        print(current.val, end=" -> ")
        current = current.next
    print("None")



if __name__ == "__main__":
    link_list = LinkList()

    # 插入节点
    link_list.insert(1)
    link_list.insert(1)
    link_list.insert(2)
    link_list.insert(3)
    link_list.insert(3)
    link_list.insert(4)
    link_list.insert(5)
    link_list.insert(5)
    link_list.insert(6)

    # 遍历链表
    print("Linked List:")
    traverse(link_list.head)

    # 删除节点
    link_list.delete(2)
    print("\nAfter deleting 2:")
    traverse(link_list.head)

    # 查找节点
    search_result = link_list.search(3)
    if search_result:
        print(f"\nValue {search_result.val} found in the list.")
    else:
        print("\nValue not found in the list.")
    print()

    res1 = deleteDuplicates(link_list.head)
    res2 = deleteDuplicatesSave(link_list.head)
    traverse(res1)
    traverse(res2)
