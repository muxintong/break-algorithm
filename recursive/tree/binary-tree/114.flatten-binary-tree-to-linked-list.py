# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        给你二叉树的根结点 root ，请你将它展开为一个单链表：
        
        展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
        展开后的单链表应该与二叉树 先序遍历 顺序相同。
        """
        if root is None: return

        # 递归拉平左右子树
        self.flatten(root.left)
        self.flatten(root.right)

        # postorder：
        left = root.left
        right = root.right
        # 左空
        root.left = None
        # 右接左
        root.right = left
        # 接上原右子树
        p = root
        while p.right is not None:
            p = p.right
        p.right = right
