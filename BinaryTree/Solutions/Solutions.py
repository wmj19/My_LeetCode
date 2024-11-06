import collections
from typing import Optional, List

from BinaryTree.structure.BinaryTree import inorder_traversal
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


    def sum_of_left_leaves(self, root: Optional[TreeNode]) -> int:
        LEFT, RIGHT, ROOT = 0, 1, 2
        queue = collections.deque()
        queue.append((root, ROOT))

        sum = 0

        while queue:
            node, pos = queue.pop()
            if pos == LEFT and node.left is None and node.right is None:
                sum += node.val
            if node.left:
                queue.append((node.left, LEFT))
            if node.right:
                queue.append((node.right, RIGHT))

        return sum

    def inorder_traversal(self, root: TreeNode, inorder_list):
        if root:
            self.inorder_traversal(root.left, inorder_list)
            inorder_list.append(root.val)
            self.inorder_traversal(root.right, inorder_list)

    def find_mode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.inorder_traversal(root, lst)
        pre = lst[0]
        mode = [lst[0]]
        max_count = 1
        count = 1
        for i in range(1, len(lst)):
            if pre == lst[i]:
                count += 1
            else:
                count = 1

            if count == max_count:
                mode.append(pre)
            if count >= max_count:
                max_count = count
                mode = [lst[i]]
            pre = lst[i]
        return mode


