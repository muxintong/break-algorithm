# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memory = {}

        def dp(root: TreeNode) -> int:
            if root is None: return 0

            if memory.get(root): return memory[root]

            # 不抢root.val，去下家
            not_rob = dp(root.left) + dp(root.right)
            # 抢root.val，去下下家
            rob = root.val \
                  + (dp(root.left.left) + dp(root.left.right)) if root.left is not None else 0 \
                  + (dp(root.right.left) + dp(root.right.right)) if root.right is not None else 0

            memory[root] = max(rob, not_rob)

            return memory[root]

        return dp(root)


def list_to_binarytree(nums: List[int]):
    def level(index):
        # if index >= len(nums) or nums[index] is None:
        #     return None
        if index >= len(nums):
            return None

        root = TreeNode(nums[index])
        # print(root.val)
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root

    return level(0)


def main():
    # 输入: root = [3,2,3,null,3,null,1]
    # 输出: 7
    # 解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
    solution1 = Solution()
    print(solution1.rob(list_to_binarytree([3, 2, 3, None, 3, None, 1])))

    # 输入: root = [3,4,5,1,3,null,1]
    # 输出: 9
    # 解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
    solution2 = Solution()
    print(solution2.rob(list_to_binarytree([3, 4, 5, 1, 3, None, 1])))


if __name__ == '__main__':
    main()
