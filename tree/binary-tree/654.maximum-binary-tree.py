# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) <= 0: return

        max_val = 0
        max_index = 0
        for i, val in enumerate(nums):
            if val > max_val:
                max_val = val
                max_index = i

        root = TreeNode(max_val)

        root.left = self.constructMaximumBinaryTree(nums[0:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:len(nums)])

        return root
