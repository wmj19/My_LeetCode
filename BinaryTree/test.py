from PyQt5.QtCore import center

import structure.BinaryTree
from BinaryTree.Solutions.CountOfNodes import count_nodes
from BinaryTree.Solutions.HasPathSum import has_path_sum
from BinaryTree.Solutions.IsBalanced import is_balanced
from BinaryTree.Solutions.IsSameTree import is_same_tree
from BinaryTree.Solutions.IsSymmetric import is_symmetric
from BinaryTree.Solutions.MaxDepth import max_depth
from BinaryTree.Solutions.MinDepth import min_depth
from BinaryTree.Solutions.sorted_array_to_BST import sorted_array_to_BST
from BinaryTree.structure.BinaryTree import *
from BinaryTree.utils import *
from LinkList1.structure.LinkList import traverse
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
print("level_traversal".center(40, '='))
res_level = level_traversal(tree1.root)
print_list(res_level)

print("is_same_tree".center(40, '='))
same_tree1 = BinaryTree()
same_tree1.root = TreeNode(1)
same_tree1.left_insert(same_tree1.root, 2)
# same_tree1.right_insert(same_tree1.root, 3)
same_tree2 = BinaryTree()
same_tree2.root = TreeNode(1)
#same_tree1.left_insert(same_tree2.root, 2)
#same_tree1.right_insert(same_tree2.root, 3)
same_tree1.right_insert(same_tree2.root, 2)

res = is_same_tree(same_tree1.root, same_tree2.root)
if res:
    print("tree1 and tree2 is same tree")
else:
    print("tree1 and tree2 is different")

print("is_symmetric".center(40, '='))
tree_symmetric = BinaryTree()
tree_symmetric.root = TreeNode(1)
tree_symmetric.left_insert(tree_symmetric.root, 2)
tree_symmetric.left_insert(tree_symmetric.root.left, 3)
tree_symmetric.right_insert(tree_symmetric.root.left, 4)
tree_symmetric.right_insert(tree_symmetric.root, 2)
tree_symmetric.right_insert(tree_symmetric.root.right, 3)
tree_symmetric.left_insert(tree_symmetric.root.right, 4)
if is_symmetric(tree_symmetric.root):
    print("symmetric")
else:
    print("not symmetric")


print("max_depth".center(40, '='))
tree_max_depth = BinaryTree()
tree_max_depth.root = TreeNode(1)
tree_max_depth.left_insert(tree_max_depth.root, 2)
tree_max_depth.left_insert(tree_max_depth.root.left, 4)
tree_max_depth.right_insert(tree_max_depth.root.left, 5)
tree_max_depth.right_insert(tree_max_depth.root, 3)
tree_max_depth.left_insert(tree_max_depth.root.right, 6)
tree_max_depth.right_insert(tree_max_depth.root.right, 7)
tree_max_depth.left_insert(tree_max_depth.root.right.left, 8)
max_depth = max_depth(tree_max_depth.root)
print(f"max_depth = {max_depth}")

print("sorted_array_to_BST".center(40, '='))
# bst_tree = sorted_array_to_BST([-2, -1, 0, 1, 2])
# inorder_res = mark_inorder_traversal(bst_tree)
# print_list(inorder_res)
bst_tree = sorted_array_to_BST([-10, -3, 0, 5, 9])
inorder_res = level_traversal(bst_tree)
print_list(inorder_res)

print("is_balanced".center(40, '='))
# tree_is_balanced = BinaryTree()
# tree_is_balanced.root = TreeNode(1)
# tree_is_balanced.left_insert(tree_is_balanced.root, 2)
# tree_is_balanced.left_insert(tree_is_balanced.root.left, 2)
# tree_is_balanced.left_insert(tree_is_balanced.root.left.left, 2)
# tree_is_balanced.right_insert(tree_is_balanced.root, 3)
# tree_is_balanced = BinaryTree()
# tree_is_balanced.root = TreeNode(3)
# tree_is_balanced.left_insert(tree_is_balanced.root, 9)
# tree_is_balanced.right_insert(tree_is_balanced.root, 20)
# tree_is_balanced.left_insert(tree_is_balanced.root.right, 15)
# tree_is_balanced.right_insert(tree_is_balanced.root.right, 7)
tree_is_balanced = BinaryTree()
tree_is_balanced.root = TreeNode(3)
tree_is_balanced.left_insert(tree_is_balanced.root, 9)
tree_is_balanced.right_insert(tree_is_balanced.root, 20)
tree_is_balanced.left_insert(tree_is_balanced.root.left, 15)
tree_is_balanced.left_insert(tree_is_balanced.root.left.left, 15)
tree_is_balanced.right_insert(tree_is_balanced.root.left, 7)
tree_is_balanced.right_insert(tree_is_balanced.root.left.left, 7)
res = is_balanced(tree_is_balanced.root)
if res:
    print("true")
else:
    print("false")

print("min_depth".center(40, '='))
tree_min_depth = BinaryTree()
tree_min_depth.root = TreeNode(2)
tree_min_depth.right_insert(tree_min_depth.root, 3)
tree_min_depth.right_insert(tree_min_depth.root.right, 4)
tree_min_depth.right_insert(tree_min_depth.root.right.right, 5)
min_depth = min_depth(tree_min_depth.root)
print(f"tree_min_depth's depth = {min_depth}")

print("has_path_sum".center(40, '='))
tree_has_path_sum = BinaryTree()
tree_has_path_sum.root = TreeNode(1)
tree_has_path_sum.left_insert(tree_has_path_sum.root, 2)
tree_has_path_sum.right_insert(tree_has_path_sum.root, 3)
res = has_path_sum(tree_has_path_sum.root, 3)
print(res)

print("count_of_node".center(40, '='))
res = count_nodes(tree_has_path_sum.root)
print(res)