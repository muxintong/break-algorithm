from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        perms = []
        track = []

        used = [False for i in range(n + 1)]

        def backtrack(used: List[bool]) -> None:
            if len(track) == n:
                perms.append(track.copy())

            for i in range(1, n + 1):
                if used[i]:
                    continue

                elif not used[i]:
                    used[i] = True
                    track.append(i)

                    backtrack(used)

                    track.remove(i)
                    used[i] = False

        backtrack(used)

        res = []
        for perm in perms:
            flag = 0
            for i in range(1, len(perm) + 1):
                if perm[i - 1] % i != 0 and i % perm[i - 1] != 0:
                    flag = 1
                    break
            if flag == 0: res.append(perm)

        return len(res)


def main():
    # 输入：n = 2
    # 输出：2
    # 解释：
    # 第 1 个优美的排列是 [1,2]：
    #     - perm[1] = 1 能被 i = 1 整除
    #     - perm[2] = 2 能被 i = 2 整除
    # 第 2 个优美的排列是 [2,1]:
    #     - perm[1] = 2 能被 i = 1 整除
    #     - i = 2 能被 perm[2] = 1 整除
    solution1 = Solution()
    print(solution1.countArrangement(n=2))

    # 输入：n = 1
    # 输出：1
    solution2 = Solution()
    print(solution2.countArrangement(n=1))

    # 输入：n = 3
    solution3 = Solution()
    print(solution3.countArrangement(n=3))


if __name__ == '__main__':
    main()
