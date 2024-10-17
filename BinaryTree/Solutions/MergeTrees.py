import collections
from typing import Optional
import sys
sys.path.append('mergeTrees.py')
from BinaryTree.structure.TreeNode import TreeNode

# T617: 合并二叉树
# 给你两棵二叉树： root1 和 root2 。
#
# 想象一下，当你将其中一棵覆盖到另一棵之上时,
# 两棵树上的一些节点将会重叠（而另一些不会).
# 你需要将这两棵树合并成一棵新二叉树
#
# 合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；
#            否则，不为 null 的节点将直接作为新二叉树的节点。
#
# 返回合并后的二叉树。
#
# 注意: 合并过程必须从两个树的根节点开始

# LeetCode官方bfs题解
def mergeTrees_bfs(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if root1 is None:
        return root2

    if root2 is None:
        return root1

    merged = TreeNode(root1.val+root2.val)
    queue =collections.deque([merged])
    queue1 = collections.deque([root1])
    queue2 = collections.deque([root2])

    while queue1 or queue2:
        node = queue.popleft()
        node1 = queue1.popleft()
        node2 = queue2.popleft()

        left1, right1 = node1.left, node1.right
        left2, right2 = node2.left, node2.right
        if left1 or left2:
            if left1 and left2:
                left = TreeNode(left1.val + left2.val)
                node.left = left
                queue.append(left)
                queue1.append(left1)
                queue2.append(left2)
            elif left1:
                node.left = left1
            elif left2:
                node.left = left2


        if right1 or right2:
            if right1 and right2:
                right = TreeNode(right1.val+right2.val)
                node.right = right
                queue.append(right)
                queue1.append(right1)
                queue2.append(right2)
            elif right1:
                node.right = right1
            elif right2:
                node.right = right2

    return merged

def build(binary_tree_list):
    for i in range(1,(len(binary_tree_list)-1)//2+1):
        if isinstance(binary_tree_list[2*i], TreeNode):
            binary_tree_list[i].left = binary_tree_list[2*i]
        if isinstance(binary_tree_list[2*i+1], TreeNode):
            binary_tree_list[i].right = binary_tree_list[2*i+1]
    return binary_tree_list[1]

# LeetCode官方递归题解
def mergeTrees_official_recursion(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1:
        return t2
    if not t2:
        return t1

    merged = TreeNode(t1.val + t2.val)
    merged.left = mergeTrees_official_recursion(t1.left, t2.left)
    merged.right = mergeTrees_official_recursion(t1.right, t2.right)
    return merged


