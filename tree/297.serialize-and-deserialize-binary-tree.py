# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def traverse(root: TreeNode):
            if root is None:
                res.append('x')
                return

                # preorder
            res.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return ','.join(str(i) for i in res)

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')

        def traverse(data_list: List):
            val = data_list.pop(0)
            if val == 'x': return

            # preorder
            root = TreeNode(int(val))
            root.left = traverse(data_list)
            root.right = traverse(data_list)

            return root

        return traverse(data_list)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
