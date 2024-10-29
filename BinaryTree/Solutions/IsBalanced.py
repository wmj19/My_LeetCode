from typing import Optional

from BinaryTree.Solutions.MaxDepth import max_depth
from BinaryTree.structure.TreeNode import TreeNode



def is_balanced(root: Optional[TreeNode]) -> bool:
    if root:
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)
        if abs(left_depth - right_depth) >= 2:
            return False
        return is_balanced(root.left) and is_balanced(root.right)