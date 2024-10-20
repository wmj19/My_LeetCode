from tempfile import template
from typing import Optional

from BinaryTree.structure.TreeNode import TreeNode

# 使用颜色标记法
# 访问过的用灰色，没访问的白色
def mark_inorder_traversal(root:Optional[TreeNode]):
    res = []
    WHITE, GRAY = 0, 1
    stack = [(WHITE, root)]

    while stack:
        color, node = stack.pop()
        # 因为会把叶子节点看成有子节点的分支
        if node is None: continue
        # 由于出栈和入栈顺序刚好是反正来的，因此对于中序遍历入栈要用"右中左"
        if color == 0:
            stack.append((WHITE, node.right))
            stack.append((GRAY, node))
            stack.append((WHITE, node.left))
        else:
            res.append(node.val)

    return res

def mark_preorder_traversal(root:Optional[TreeNode]):
    res = []
    WHITE, GRAY = 0, 1
    stack = [(WHITE, root)]

    while stack:
        color, node = stack.pop()
        # 因为会把叶子节点看成有子节点的分支
        if node is None: continue
        # 由于出栈和入栈顺序刚好是反正来的，因此对于中序遍历入栈要用"右左中"
        if color == 0:
            stack.append((WHITE, node.right))
            stack.append((WHITE, node.left))
            stack.append((GRAY, node))
        else:
            res.append(node.val)

    return res

def mark_postorder_traversal(root:Optional[TreeNode]):
    res = []
    WHITE, GRAY = 0, 1
    stack = [(WHITE, root)]

    while stack:
        color, node = stack.pop()
        # 因为会把叶子节点看成有子节点的分支
        if node is None: continue
        # 由于出栈和入栈顺序刚好是反正来的，因此对于中序遍历入栈要用"中右左"
        if color == 0:
            stack.append((GRAY, node))
            stack.append((WHITE, node.right))
            stack.append((WHITE, node.left))
        else:
            res.append(node.val)

    return res

def level_traversal(root:Optional[TreeNode]):
    queue = [root]
    temp = []
    res = []

    while queue:
        for node in queue:
            res.append(node.val)
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
        queue = temp
        temp =[]

    return res