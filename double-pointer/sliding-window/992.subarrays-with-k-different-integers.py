from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:


def main():
    # 输入：nums = [1,2,1,2,3], k = 2
    # 输出：7
    # 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
    solution1 = Solution()
    print(solution1.subarraysWithKDistinct())

    # 输入：nums = [1,2,1,3,4], k = 3
    # 输出：3
    # 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
    solution2 = Solution()
    print(solution2.subarraysWithKDistinct())


if __name__ == '__main__':
    main()
