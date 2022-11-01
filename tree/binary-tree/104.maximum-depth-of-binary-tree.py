from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        depth = max(left, right) + 1
        return depth


def list_to_binarytree(nums: List[int]):
    def level(index):
        if index >= len(nums):
            return None

        root = TreeNode(nums[index])
        # print(root.val)
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root

    return level(0)


def main():
    # in:[3,9,20,None,None,15,7]
    # out:3
    root = [3, 9, 20, None, None, 15, 7]
    solution1 = Solution()
    print(solution1.maxDepth(list_to_binarytree(root)))


if __name__ == '__main__':
    main()
