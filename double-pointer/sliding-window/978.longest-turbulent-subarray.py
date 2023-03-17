from typing import List

"""
core mind:
滑动窗口问题：
(a1 < a2 > a3) or (a1 > a2 < a3)
使用乘积和小于0的形式转化该问题
不满足上述条件的即：(a2-a1)*(a3-a2)>=0
"""


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        if len(arr) == 2:
            if arr[0] == arr[1]:
                return 1
            else:
                return 2

        left = 0
        right = 0
        res = 0

        for right in range(2, len(arr), 1):
            if arr[right - 1] == arr[right]:
                left = right
            elif (arr[right - 1] - arr[right - 2]) * (arr[right] - arr[right - 1]) >= 0:
                left = right - 1
            res = max(res, right - left + 1)

        return res


def main():
    # 输入：arr = [9,4,2,10,7,8,8,1,9]
    # 输出：5
    # 解释：arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
    solution1 = Solution()
    print(solution1.maxTurbulenceSize(arr=[9, 4, 2, 10, 7, 8, 8, 1, 9]))

    # 输入：arr = [4,8,12,16]
    # 输出：2
    solution2 = Solution()
    print(solution2.maxTurbulenceSize(arr=[4, 8, 12, 16]))

    # 输入：arr = [100]
    # 输出：1
    solution3 = Solution()
    print(solution3.maxTurbulenceSize(arr=[100]))


if __name__ == '__main__':
    main()
