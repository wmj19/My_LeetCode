from typing import Optional

from BinaryTree.structure.TreeNode import TreeNode

# 101.判断一颗树是否对称
# 和100题几乎一样，把根的左右子树分别看成两颗树就和100题一样了
# 唯一不同的就是入栈顺序，因为是对称的，
# 所以左边的子树的左节点相当于是右边子树的右节点因此入栈顺序会相反
def is_symmetric(root: Optional[TreeNode]):
    root_left = root.left
    root_right = root.right
    stack_left = [root_left]
    stack_right = [root_right]

    while stack_left and stack_right:
        node_left = stack_left.pop()
        node_right = stack_right.pop()

        if node_left is None and node_right is None:
            continue
        if node_left is None and node_right:
            return False
        if node_left and node_right is None:
            return False

        if node_left.val == node_right.val:
            stack_left.append(node_left.right)
            stack_left.append(node_left.left)
            stack_right.append(node_right.left)
            stack_right.append(node_right.right)
        else:
            return False

    return True