from typing import Optional

from BinaryTree.structure.TreeNode import TreeNode


def max_depth(root: Optional[TreeNode]):
    if root is None:
        return 0

    queue = [root]
    depth = 0
    temp = []

    while queue:
        for node in queue:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        queue = temp
        temp = []
        depth += 1

    return depth