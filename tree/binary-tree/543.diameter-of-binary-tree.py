from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if root is None: return

        def maxDepth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            left = maxDepth(root.left)
            right = maxDepth(root.right)
            depth = max(left, right) + 1
            return depth

        left = maxDepth(root.left)
        right = maxDepth(root.right)
        diameter = left + right
        res = max(diameter, res)

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return res


def list_to_binarytree(nums: List[int]):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None

        root = TreeNode(nums[index])
        # print(root.val)
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root

    return level(0)


def main():
    # 输入：root = [1,2,3,4,5]
    # 输出：3
    root = root = [1, 2, 3, 4, 5]
    list_to_binarytree(root)
    solution1 = Solution()
    print(solution1.diameterOfBinaryTree(list_to_binarytree(root)))


if __name__ == '__main__':
    main()
