class Solution:
    def numTrees(self, n: int) -> int:
        """
        numTrees:计算闭区间 [1, n] 组成的 BST 个数.
        1. 首先，这棵 BST 的根节点总共有几种情况？ 因为每个数字都可以作为根节点：故有n种情况。
        2. 固定 i 作为根节点，这个前提下能有几种不同的 BST 呢？
           根据 BST 的特性，根节点的左子树都比根节点的值小，右子树的值都比根节点的值大。
           所以如果固定 i 作为根节点，左子树节点就是 {1,i-1} 的组合，右子树就是 {i+1,n} 的组合。
           左子树的组合数和右子树的组合数乘积就是 i 作为根节点时的 BST 个数。
        """

        self.memory = [[0 for col in range(n + 1)] for row in range(n + 1)]

        def bst_counts(l: int, r: int) -> int:
            if l > r: return 1

            # before: findout in memory
            if self.memory[l][r] != 0: return self.memory[l][r]
            # recursive
            res = 0
            for i in range(l, r + 1):
                l_nums = bst_counts(l, i - 1)
                r_nums = bst_counts(i + 1, r)
                res += l_nums * r_nums
            # after: write in memory
            self.memory[l][r] = res

            return res

        return bst_counts(1, n)
