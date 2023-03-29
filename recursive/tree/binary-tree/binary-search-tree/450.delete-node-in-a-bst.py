# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
            successor = root.right
            while successor.left:
                successor = successor.left
            successor.right = self.deleteNode(root.right, successor.val)
            successor.left = root.left
            return successor
        return root


class Solution:
    def get_min(self, root: TreeNode) -> TreeNode:
        # BST树最左边的元素即为最小元素
        p = root
        while p.left is not None: p = p.left
        return p

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None: return None

        if key == root.val:
            if root.left is None: return root.right
            if root.right is None: return root.left
            if root.left is not None and root.right is not None:
                # 左右子树都不空：新根则可为左子树的最大节点或右子树的最小节点
                # 1.找右最小节点
                right_min = self.get_min(root.right)
                # 2.删右最小节点
                root.right = self.deleteNode(root.right, right_min)
                # 3.将右最小节点作为新根
                right_min.left = root.left
                right_min.right = root.right
                root = right_min
                return root

        if key < root.val: root.left = self.deleteNode(root.left, key)
        if key > root.val: root.right = self.deleteNode(root.right, key)

        return root
