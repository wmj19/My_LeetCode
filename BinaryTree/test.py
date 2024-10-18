import structure.BinaryTree
from BinaryTree.structure.BinaryTree import *
from BinaryTree.utils import *
from Solutions.MergeTrees import *
from Solutions.Traversal import *

# 构造树
tree1 = BinaryTree()
tree1.root = TreeNode(4)
tree1.left_insert(tree1.root, 14)
tree1.right_insert(tree1.root, 3)
tree1.left_insert(tree1.root.left, 1)
tree1.right_insert(tree1.root.left, 2)

tree2 = BinaryTree()
tree2.root = TreeNode(2)
tree2.left_insert(tree2.root, 4)
tree2.right_insert(tree2.root, 1)
tree2.left_insert(tree2.root.right, 9)

print("mergeTrees_bfs".center(40, '='))
ans1 = mergeTrees_bfs(tree1.root, tree2.root)
preorder_traversal(ans1)
print()
print("mergeTrees_official_recursion".center(40, '='))
ans2 = mergeTrees_official_recursion(tree1.root, tree2.root)
preorder_traversal(ans2)
print()

print("mark_inorder_traversal".center(40, '='))
res_inorder = mark_inorder_traversal(tree1.root)
print_list(res_inorder)
print("mark_preorder_traversal".center(40, '='))
res_preorder = mark_preorder_traversal(tree1.root)
print_list(res_preorder)
print("mark_postorder_traversal".center(40, '='))
res_postorder = mark_postorder_traversal(tree1.root)
print_list(res_postorder)
