# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    二叉搜索树BST特性：left<root<right
    中序遍历【left-root-right】BST树可得有序递增序列
    本例欲得有序递减序列：递归遍历中逆向中序即可【right-root-left】,在中序代码处理过程中进行累加
    """

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def traverse(root: TreeNode):
            if root is None: return

            traverse(root.right)

            # inorder
            self.sum += root.val
            root.val = self.sum

            traverse(root.left)

        traverse(root)
        return root
