from typing import Optional
from BinaryTree.structure.TreeNode import TreeNode


def min_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    queue = [root]
    temp = []
    min_depth = 1

    while queue:
        for node in queue:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if node.left is None and node.right is None:
                return min_depth
        queue = temp
        temp = []
        min_depth += 1

    return min_depth