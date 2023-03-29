# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            print(root.val)
            self.inorderTraversal(root.right)


def list_to_tree(l: list) -> TreeNode:
    if len(l) == 0: return None
    head = TreeNode(l[0])
    p = head
    for i in range(len(l)):
        p = TreeNode(l[i])
        p.left = list_to_tree(l[i + 1])
        p.right = list_to_tree(l[i + 2])
    return head


def list_to_binarytree(nums: List[int]):
    def level(index):
        # if index >= len(nums) or nums[index] is None:
        #     return None
        if index >= len(nums):
            return None

        root = TreeNode(nums[index])
        print(root.val)
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root

    return level(0)


def list2BinaryTree(root, nums: list, i):
    if i < len(nums):
        if nums[i] == None:
            return None
        else:
            root = TreeNode(nums[i])
            root.left = list2BinaryTree(root.left, nums, i * 2 + 1)
            root.right = list2BinaryTree(root.right, nums, i * 2 + 2)
        return root
    return root


def main():
    # 输入：root = [1,null,2,3]
    # 输出：[1,3,2]
    solution1 = Solution()
    root = [1, None, 2, 3]
    print(list2BinaryTree(None, root, 0))
    # print(solution1.inorderTraversal(root=[1, None, 2, 3]))


if __name__ == '__main__':
    main()
