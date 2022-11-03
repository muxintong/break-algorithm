# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        coremind:
        1、穷举root节点的所有可能。
        2、递归构造出左右子树的所有合法 BST。
        3、给root节点穷举所有左右子树的组合。
        """
        if n == 0: return []

        def bst_build(l: int, r: int):
            """"
            bst_build：构造闭区间[l,r]内所有的合法BST
            """
            if l > r: return [None, ]

            res = []
            # 1.穷举根节点root的所有可能情况
            for i in range(l, r + 1):
                # 2.递归构造左右子树的所有合法BST
                left_tree = bst_build(l, i - 1)
                right_tree = bst_build(i + 1, r)
                # 3.穷举root节点所有左右子树的组合
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)

            return res

        return bst_build(1, n)

    def generateTrees_TimeLimitError(self, n: int) -> List[Optional[TreeNode]]:
        """
        TimeLimitError Reason：全局变量外置发生上下文切换
        """
        if n == 0: return []
        self.res = []

        def bst_build(l: int, r: int):
            if l > r: return [None, ]

            # 1.穷举根节点root的所有可能情况
            for i in range(l, r + 1):
                # 2.递归构造左右子树的所有合法BST
                left_tree = bst_build(l, i - 1)
                right_tree = bst_build(i + 1, r)
                # 3.穷举root节点所有左右子树的组合
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        self.res.append(root)

            return self.res

        return bst_build(1, n)


class Solution_Authority:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end: return [None, ]

            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)
                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)

                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []
