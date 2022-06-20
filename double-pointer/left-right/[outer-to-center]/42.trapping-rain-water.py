"""
link:
https://labuladong.github.io/algo/4/31/129/
https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        对于柱i，其所能容纳的最大雨水量为：
        min(l_max[0-i], r_max[i,n]) - height[i]
        """
        n = len(height)
        l_max_memo = [0] * n
        r_max_memo = [0] * n

        l_max = height[0]
        r_max = height[n - 1]

        for i in range(1, n - 1, 1):
            l_max = max(l_max, height[i - 1])
            l_max_memo[i] = l_max

        for i in range(n - 2, 0, -1):
            r_max = max(r_max, height[i + 1])
            r_max_memo[i] = r_max

        res = 0
        for i in range(1, n - 1):
            # NOTE:所接雨水量不能为负值，只有当其大于0时才将其计入答案中
            temp = min(l_max_memo[i], r_max_memo[i]) - height[i]
            if temp > 0:
                res += temp

        return res

    # 备忘录解法
    def trap2(self, height: List[int]) -> int:
        """
        对于柱i，其所能容纳的最大雨水量为：
        min(l_max[0-i], r_max[i,n] - height[i]
        """
        n = len(height)
        # 使用数组作为备忘录
        l_max_memo = [0] * n
        r_max_memo = [0] * n

        # base case
        l_max_memo[0] = height[0]
        r_max_memo[n - 1] = height[n - 1]

        # l_max：左至右
        for i in range(1, n - 1, 1):
            l_max_memo[i] = max(height[i], l_max_memo[i - 1])

        # r_max：右至左
        for i in range(n - 2, 0, -1):
            r_max_memo[i] = max(height[i], r_max_memo[i + 1])

        res = 0
        for i in range(1, n - 1):
            # NOTE:所接雨水量不能为负值，只有当其大于0时才将其计入答案中
            temp = min(l_max_memo[i], r_max_memo[i]) - height[i]
            if temp > 0:
                res += temp

        return res

    
def main():
    # Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # Output: 6
    # Explanation: The above elevation map (black section) is represented by
    # array [0,1,0,2,1,0,1,3,2,1,2,1].
    # In this case, 6 units of rain water (blue section) are being trapped.
    solution1 = Solution()
    print(solution1.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    # Input: height = [4,2,0,3,2,5]
    # Output: 9
    solution2 = Solution()
    print(solution2.trap2([4, 2, 0, 3, 2, 5]))


if __name__ == '__main__':
    main()
