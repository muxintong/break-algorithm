# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inorder: List[int], in_start: int, in_end: int,
                  postorder: List[int], post_start: int, post_end: int) -> Optional[TreeNode]:
            if in_start > in_end: return None

            root_val_postorder = postorder[post_end]
            root_index_inorder = inorder.index(root_val_postorder)
            left_size = root_index_inorder - in_start

            root = TreeNode(root_val_postorder)
            root.left = build(inorder, in_start, root_index_inorder - 1,
                              postorder, post_start, post_start + left_size - 1)
            root.right = build(inorder, root_index_inorder + 1, in_end,
                               postorder, post_start + left_size, post_end - 1)

            return root

        return build(inorder, 0, len(inorder) - 1,
                     postorder, 0, len(postorder) - 1)
