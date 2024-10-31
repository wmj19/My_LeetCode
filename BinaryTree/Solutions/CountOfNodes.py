import collections
from typing import Optional
from BinaryTree.structure.TreeNode import TreeNode

def count_nodes(root: Optional[TreeNode]) -> int:
    queue = collections.deque()
    queue.append(root)
    count = 0

    while queue:
        node = queue.pop()
        count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return count