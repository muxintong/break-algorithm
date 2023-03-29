from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        track = []
        used = [False for i in range(n + 1)]

        def backtrack(used: List[bool]) -> None:
            if len(track) == n:
                res.append(track.copy())

            for i in range(1, n + 1):
                if used[i]: continue
                used[i] = True
                track.append(i)

                backtrack(used)

                track.remove(i)
                used[i] = False

        backtrack(used)
        s = ''
        for j in res[k - 1]:
            s = s + str(j)
        return s


def main():
    """
    给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

    按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    给定 n 和 k，返回第 k 个排列。
    """
    # 输入：n = 3, k = 3
    # 输出："213"
    solution1 = Solution()
    print(solution1.getPermutation(n=3, k=3))

    # 输入：n = 4, k = 9
    # 输出："2314"
    solution2 = Solution()
    print(solution2.getPermutation(n=4, k=9))

    # 输入：n = 3, k = 1
    # 输出："123"
    solution3 = Solution()
    print(solution3.getPermutation(n=3, k=1))


if __name__ == '__main__':
    main()
