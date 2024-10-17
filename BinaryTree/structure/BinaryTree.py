from TreeNode import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def left_insert(self, current_node, value):
        if current_node.left is None:
            current_node.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def right_insert(self, current_node, value):
        if current_node.right is None:
            current_node.right = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right = current_node.right
            current_node.right = new_node

# 前序遍历（根 -> 左 -> 右）
def preorder_traversal(node):
    if node:
        print(node.val, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# 中序遍历（左 -> 根 -> 右）
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

# 后序遍历（左 -> 右 -> 根）
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.val, end=" ")

if __name__ == "__main__":
    # 创建一个二叉树
    tree = BinaryTree()
    tree.root = TreeNode(1)

    # 手动插入左右节点
    tree.left_insert(tree.root, 2)
    tree.right_insert(tree.root, 3)
    tree.left_insert(tree.root.left, 4)
    tree.right_insert(tree.root.left, 5)

    # 前序遍历
    print("Preorder traversal:")
    preorder_traversal(tree.root)
    print()

    # 中序遍历
    print("Inorder traversal:")
    inorder_traversal(tree.root)
    print()

    # 后序遍历
    print("Postorder traversal:")
    postorder_traversal(tree.root)
    print()