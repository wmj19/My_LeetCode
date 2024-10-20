# 这里其实题目已经告诉我们数组是升序排序，这有什么暗示呢？
# 为了让左右子树的高度差不超过1，我们可以直接选择最中间的数字作为根节点。
#
# 为了能够更好的思考递归，请大家先跟我假设只有三个数字，比如[1, 2, 3],现在我们需要构建一个二叉排序树。
#
# 首先我们选择最中间的数字2作为根节点
# 然后构建数字1对应的节点left和数字3对应的节点right
# 最后我们直接拼接他们，TreeNode(2, left, right)。
# ok，现在我们思路放宽一点，假设数组是[-1, 0, 1, 2, 3, 4, 5]
#
# 我们依旧是一样的思路.
#
# 先选中间节点2。把整个数组拆分成为[-1, 0, 1]、[2]、[3, 4, 5]。(记得把这三个数字看成一个整体)
# 现在问题就转化成为[-1, 0, 1]这样的left左子树如何求？[3, 4, 5]这样的右子树如何求？（这里大家仔细想想，是不是跟原问题是一致的啊，我们只需要继续这样递归下去，便可以求得结果）
# 递归边界
#
# 既然都想到了递归，那么递归边界是什么呢？
# 这里比较容易想到，假如我们传进来一个空数组，是不是就会返回一个空节点啊！
# 所以我们的边界条件，就是当我们的数组长度为0的时候，返回None。
#
# 作者：长衫难脱
# 链接：https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/solutions/2876821/hen-hao-de-di-gui-si-kao-wen-ti-by-tshng-khc5/
# 来源：力扣（LeetCode）
from BinaryTree.structure.TreeNode import TreeNode


def sorted_array_to_BST(nums:list[int]):

    if len(nums) == 0:
        return None

    n = len(nums) // 2
    left = sorted_array_to_BST(nums[:n])
    right = sorted_array_to_BST(nums[n+1:])

    return TreeNode(nums[n], left, right)
