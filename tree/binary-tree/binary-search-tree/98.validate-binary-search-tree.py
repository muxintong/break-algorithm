# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    BST树：【左 < 根  < 右】，root的整个左子树都要小于root.val，整个右子树都要大于root.val。
    keyponit：对于某一节点root，其只能约束自己的左右子节点，如何让root的约束力传递给整棵左右子树？
              通过使用辅助方法，增加入参列表携带额外约束信息，将上述约束传递给子树的所有节点。
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(root: Optional[TreeNode], min: Optional[TreeNode], max: Optional[TreeNode]) -> bool:
            if root is None: return True
            if min is not None and root.val <= min.val: return False
            if max is not None and root.val >= max.val: return False

            return is_valid_bst(root.left, min, root) and is_valid_bst(root.right, root, max)

        return is_valid_bst(root, None, None)
