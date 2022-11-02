# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L + 1], post[:L])
        root.right = self.constructFromPrePost(pre[L + 1:], post[L:-1])
        return root


class Solution2:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(preorder: List[int], pre_start: int, pre_end: int,
                  postorder: List[int], post_start: int, post_end: int) -> Optional[TreeNode]:
            if pre_start > pre_end or post_start > post_end: return None
            if pre_start == pre_end: return TreeNode(preorder[pre_start])

            root_val = preorder[pre_start]
            pre_left_val = preorder[pre_start + 1]
            post_right_val = postorder[post_end - 1]
            pre_left_index_at_post = postorder.index(pre_left_val)
            post_right_index_at_pre = preorder.index(post_right_val)

            root = TreeNode(root_val)
            root.left = build(preorder, pre_start + 1, post_right_index_at_pre - 1,
                              postorder, post_start, pre_left_index_at_post)
            root.right = build(preorder, post_right_index_at_pre, pre_end,
                               postorder, pre_left_index_at_post + 1, post_end - 1)

            return root

        return build(preorder, 0, len(preorder) - 1,
                     postorder, 0, len(postorder) - 1)


def main():
    # 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
    # 输出：[1,2,3,4,5,6,7]
    solution1 = Solution()
    print(solution1.constructFromPrePost(preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1]))


if __name__ == '__main__':
    main()
