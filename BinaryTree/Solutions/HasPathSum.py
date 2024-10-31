import collections
from typing import Optional
from BinaryTree.structure.TreeNode import TreeNode

def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if root is None:
        return False

    queue = collections.deque()
    queue.append((root, root.val))
    while queue:
        node, path_sum = queue.pop()
        if node.left is None and node.right is None and path_sum == target_sum:
            return True
        if node.left:
            queue.append((node.left, path_sum + node.left.val))
        if node.right:
            queue.append((node.right, path_sum + node.right.val))
    return False