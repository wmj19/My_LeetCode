import structure.BinaryTree
from BinaryTree.structure.BinaryTree import *
from Solutions.MergeTrees import *

# tree1 = BinaryTree()
# tree1.root = TreeNode(1)
#
# tree1.left_insert(tree1.root, 3)
# tree1.right_insert(tree1.root, 2)
# tree1.left_insert(tree1.root.left, 5)
#
# tree2 = BinaryTree()
# tree2.root = TreeNode(2)
#
# tree1.left_insert(tree2.root, 1)
# tree1.right_insert(tree2.root, 3)
# tree1.right_insert(tree2.root.left, 4)
# tree1.right_insert(tree2.root.right, 7)
# # # 前序遍历
# print("Preorder traversal:")
# preorder_traversal(tree1.root)
# print()
# preorder_traversal(tree2.root)
# print()

tree1 = BinaryTree()
tree1.root = TreeNode(1)

tree1.left_insert(tree1.root, 2)
tree1.left_insert(tree1.root.left, 3)

tree2 = BinaryTree()
tree2.root = TreeNode(1)

tree1.right_insert(tree2.root, 2)
tree1.right_insert(tree2.root.right, 3)

# ans = mergeTrees_official(tree1.root, tree2.root)
print("not recursion".center(40, '='))
ans1 = mergeTrees_bfs(tree1.root, tree2.root)
preorder_traversal(ans1)
print()
print("recursion".center(40, '='))
ans2 = mergeTrees_official_recursion(tree1.root, tree2.root)
preorder_traversal(ans2)