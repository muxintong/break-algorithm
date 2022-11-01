# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder: List[int], pre_start: int, pre_end: int,
                  inorder: List[int], in_start: int, in_end: int
                  ) -> Optional[TreeNode]:
            # base case：递归出口
            if pre_start > pre_end: return None

            # 1.前序定位root，对应第一个元素
            root_val = preorder[pre_start]
            # 2.inorder找到root位置，进行左右子树划分
            index = inorder.index(root_val)

            root = TreeNode(root_val)

            left_size = index - in_start
            root.left = build(preorder, pre_start + 1, pre_start + left_size,
                              inorder, in_start, index - 1)
            root.right = build(preorder, pre_start + left_size + 1, pre_end,
                               inorder, index + 1, in_end)

            return root

        return build(preorder, 0, len(preorder) - 1,
                     inorder, 0, len(inorder) - 1)
