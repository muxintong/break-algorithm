# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        将以root为根的二叉树翻转，返回翻转后的根
        """
        if root is None: return

        # 递归翻转左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # 后序重构该树
        root.left = right
        root.right = left

        # 返回翻转后的新根
        return root


def list_to_binarytree(nums: List[int]):
    def level(index: int):
        if index >= len(nums): return None

        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)

        return root

    return level(0)


def print_binarytree_preorder(root: TreeNode) -> None:
    if root is None: return

    print(root.val)
    print_binarytree_preorder(root.left)
    print_binarytree_preorder(root.right)


def main():
    # 输入：root = [4,2,7,1,3,6,9]
    # 输出：[4,7,2,9,6,3,1]
    solution1 = Solution()
    r1=list_to_binarytree([4, 2, 7, 1, 3, 6, 9])
    print_binarytree_preorder(r1)
    print('---')
    print_binarytree_preorder(solution1.invertTree(r1))
    print('---')


if __name__ == '__main__':
    main()
