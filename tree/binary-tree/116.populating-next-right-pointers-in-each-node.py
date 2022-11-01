from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None: return None

        # 跨越不同父节点连接相邻节点
        def traverse(node1: Node, node2: Node) -> None:
            if node1 is None or node2 is None: return None

            # preorder:将node1的next域指向node2完成连接
            node1.next = node2

            # recursive
            # 相同节点内连
            traverse(node1.left, node1.right)
            traverse(node2.left, node2.right)
            # 不同节点外连
            traverse(node1.right, node2.left)

        traverse(root.left, root.right)
        return root
