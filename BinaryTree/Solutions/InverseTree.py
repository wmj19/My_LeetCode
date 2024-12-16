import collections
from typing import Optional
from BinaryTree.structure.TreeNode import TreeNode
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.pop()
        if node.left or node.right:
            temp = node.right
            node.right = node.left
            node.left = temp
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root