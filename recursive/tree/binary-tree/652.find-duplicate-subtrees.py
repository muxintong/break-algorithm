# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        给你一棵二叉树的根节点 root ，返回所有 重复的子树 。
        对于同一类的重复子树，你只需要返回其中任意 一棵 的根结点即可。
        如果两棵树具有 相同的结构 和 相同的结点值 ，则认为二者是 重复 的。
        """
        res = []
        memory = {}

        def traverse(root: Optional[TreeNode]):
            if root is None: return

            left = traverse(root.left)
            right = traverse(root.right)

            # postorder
            if left is not None and right is not None:
                subtree = left.val + ',' + right.val + ',' + root.val
            elif left is not None:
                subtree = left.val + ',' + root.val
            elif right is not None:
                subtree = right.val + ',' + root.val
            else:
                subtree = root.val
            memory.setdefault(subtree, 0)
            if memory[subtree] == 1: res.append([subtree])
            memory[subtree] += 1

        traverse(root)
        return res

    def findDuplicateSubtrees2(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        memory = {}

        def traverse(root: TreeNode):
            if root is None: return '#'

            left_val = traverse(root.left)
            right_val = traverse(root.right)

            # postorder
            subtree = left_val + ',' + right_val + ',' + root.val
            memory.setdefault(subtree, 0)
            if memory[subtree] == 1: res.append(subtree)
            memory[subtree] += 1

            return subtree

        traverse(root)
        return res


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
    # 输入：root = [1,2,3,4,None,2,4,None,None,4]
    # 输出：[[2,4],[4]]
    root = list_to_binarytree([1, 2, 3, 4, None, 2, 4, None, None, 4])
    solution1 = Solution()
    print(solution1.findDuplicateSubtrees(root))

    # 输入：root = [2,1,1]
    # 输出：[[1]]
    root = list_to_binarytree([2, 1, 1])
    solution1 = Solution()
    print(solution1.findDuplicateSubtrees(root))

    # 输入：root = [2,2,2,3,None,3,None]
    # 输出：[[2,3],[3]]
    root = list_to_binarytree([2, 2, 2, 3, None, 3, None])
    solution1 = Solution()
    print(solution1.findDuplicateSubtrees(root))


if __name__ == '__main__':
    main()
