from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(root: Optional[TreeNode]) -> List[int]:
            if root is None: return

            res.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return res


def list_to_binarytree(nums: List[int]):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None

        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root

    return level(0)


def main():
    # 输入：root = [1,None,2,3]
    # 输出：[1,2,3]
    root = [1,None,2,3]
    list_to_binarytree(root)
    solution1 = Solution()
    print(solution1.preorderTraversal(list_to_binarytree(root)))

    # 输入：root = []
    # 输出：[]
    root = []
    list_to_binarytree(root)
    solution2 = Solution()
    print(solution2.preorderTraversal(list_to_binarytree(root)))

    # 输入：root = [1]
    # 输出：[1]
    root = [1]
    list_to_binarytree(root)
    solution3 = Solution()
    print(solution3.preorderTraversal(list_to_binarytree(root)))

    # 输入：root = [1,null,2]
    # 输出：[1,2]
    root = [1, None, 2]
    list_to_binarytree(root)
    solution4 = Solution()
    print(solution4.preorderTraversal(list_to_binarytree(root)))


if __name__ == '__main__':
    main()
