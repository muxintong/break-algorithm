# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        kthSmallest：查找并返回BST树中第k个最小的元素
        BST树特性：【left < root < right】，中序遍历BST树可得一有序递增序列
        """
        self.rank = 0  # 当前元素排名
        self.res = 0

        def traverse(root: Optional[TreeNode]):
            if root is None: return

            traverse(root.left)
            # inorder
            self.rank += 1
            if self.rank == k:
                self.res = root.val
                return
            traverse(root.right)

        traverse(root)
        return self.res
