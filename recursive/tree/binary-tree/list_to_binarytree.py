from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def preorder(root: Optional[TreeNode]):
    if root is None: return

    print(root.val)
    preorder(root.left)
    preorder(root.right)


def main():
    l1 = [3, 9, 20, None, None, 15, 7]
    print(list_to_binarytree(l1))

    print('---')

    l2 = [1, 2, 3, 4, 5]
    print(list_to_binarytree(l2))

    print('---')

    l3 = [1, None, 2, 3]
    r3 = list_to_binarytree(l3)
    print('---')
    preorder(r3)

    print('---')

    # l4 = [1, None, 2, 3, 4, None, None, 5, 6]
    # root4 = list_to_binarytree(l4)
    # preorder(root4)
    # print('---')
    # print(root4)


if __name__ == '__main__':
    main()
