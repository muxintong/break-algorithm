# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    二叉搜索树BST特性：left<root<right
    中序遍历【left-root-right】BST树可得有序递增序列
    本例欲得有序递减序列：递归遍历中逆向中序即可【right-root-left】
    """

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0

        def traverse(root: Optional[TreeNode]):
            if root is None: return

            traverse(root.right)
            self.sum += root.val
            root.val = self.sum
            traverse(root.left)

        traverse(root)
        return root

    def convertBST2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        nonlocal关键字使用方法
        """

        def traverse(root: Optional[TreeNode]):
            nonlocal sum
            if root:
                traverse(root.right)
                sum += root.val
                root.val = sum
                traverse(root.left)

        sum = 0
        traverse(root)
        return root
