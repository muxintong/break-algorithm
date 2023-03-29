# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 找到空位置扎入新节点
        if root is None:
            root = TreeNode(val)
            return root

        if val < root.val: root.left = self.insertIntoBST(root.left, val)
        if val > root.val: root.right = self.insertIntoBST(root.right, val)

        return root
