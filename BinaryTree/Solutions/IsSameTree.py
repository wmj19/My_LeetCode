from typing import Optional

from BinaryTree.structure.TreeNode import TreeNode

# 100. 相同的树
# 给你两棵二叉树的根节点 p 和 q, 编写一个函数来检验这两棵树是否相同.
#
# 如果两个树在结构上相同，并且节点具有相同的值, 则认为它们是相同的.

# 用的广度优先搜索算法
def is_same_tree(p:Optional[TreeNode], q:Optional[TreeNode]):

    # 非递归
    stack_p = [p]
    stack_q = [q]

    while stack_p and stack_q:
        node1 = stack_p.pop()
        node2 = stack_q.pop()

        if node1 is None and node2 is None:
            continue
        if node1 is None and node2:
            return False
        if node1 and node2 is None:
            return False

        if node1.val == node2.val:
            stack_p.append(node1.right)
            stack_p.append(node1.left)
            stack_q.append(node2.right)
            stack_q.append(node2.left)
        else:
            return False

    return True