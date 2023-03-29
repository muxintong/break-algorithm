from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def maxDepth(node):
            if not node: return 0

            L = maxDepth(node.left)
            R = maxDepth(node.right)

            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        maxDepth(root)
        return self.ans - 1


class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if root is None: return 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            if root is None: return 0

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
        if index >= len(nums):
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

    # in：[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
    # out：8
    root = root = [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None,
                   None, -1, -4, None, None, None, -2]
    list_to_binarytree(root)
    solution2 = Solution()
    print(solution2.diameterOfBinaryTree(list_to_binarytree(root)))


if __name__ == '__main__':
    main()
