import collections
from typing import Optional, List


from BinaryTree.structure.TreeNode import TreeNode

class Solutions:
    # T257二叉树的所有路径
    # 前序遍历
    def preorder_traversal(self, root, path, res):
        if root is None:
            return
        path += f'{root.val}'
        if root.right is None and root.left is None:
            res.append(path)
        else:
            path += '->'
            self.preorder_traversal(root.left, path, res)
            self.preorder_traversal(root.right, path, res)

    def binary_tree_paths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.preorder_traversal(root, '', res)
        return res
