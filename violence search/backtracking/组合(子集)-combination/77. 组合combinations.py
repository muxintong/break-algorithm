from typing import List


class Solution:
    '''
    【组合（元素无重不可复选）】
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 结果集res:List[List[int]],存储各个track
        res = []
        # 符合题意的选择集
        track = []

        # 元素顺序保证start
        def backtrack(start):
            # 递归出口
            if len(track) == k:
                res.append(track.copy())
                return

            # NOTE:指针变量i每次从start位开始递归
            for i in range(start, n + 1, 1):
                track.append(i)
                backtrack(i + 1)
                track.remove(i)

        backtrack(1)
        return res


def main():
    # Input: n = 4, k = 2
    # Output:
    # [
    #   [2,4],
    #   [3,4],
    #   [2,3],
    #   [1,2],
    #   [1,3],
    #   [1,4],
    # ]
    solution1 = Solution()
    print(solution1.combine(n=4, k=2))

    print('---')

    # Input: n = 1, k = 1
    # Output: [[1]]
    solution2 = Solution()
    print(solution2.combine(n=1, k=1))


if __name__ == '__main__':
    main()
