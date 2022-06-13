from typing import List
from bisect import *


class SolutionTimeLimitExceeded:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        w = len(envelopes)
        # 按宽度w升序排列，若宽度一样，则按高度h降序排列：把排序后的h作为一个数组，在这个数组上计算LIS的长度就是最终答案。
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # 对高度数组寻找LIS
        height = [0] * w
        for i in range(w):
            height[i] = envelopes[i][1]

        return self.lengthOfLIS(height)

    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]:其值为以nums[i]结尾的LIS值
        # 求出数组中以每个数字结尾的LIS，最终答案为其中最大的
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        res = 1
        for i in range(len(nums)):
            res = max(res, dp[i])

        return res


class Solution:
    def maxEnvelopes(self, E: List[List[int]]) -> int:
        E.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, height in E:
            left = bisect_left(dp, height)
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
        return len(dp)


def main():
    # Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    # Output: 3
    # Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
    solution1 = Solution()
    print(solution1.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))

    # Input: envelopes = [[1,1],[1,1],[1,1]]
    # Output: 1
    solution2 = Solution()
    print(solution2.maxEnvelopes([[1, 1], [1, 1], [1, 1]]))

    # Input: [[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]
    # Output: 6
    # Expected: 3
    solution3 = Solution()
    print(solution3.maxEnvelopes(
        [[1, 15], [7, 18], [7, 6], [7, 100], [2, 200], [17, 30], [17, 45], [3, 5], [7, 8], [3, 6], [3, 10], [7, 20],
         [17, 3], [17, 45]]))


if __name__ == '__main__':
    main()
