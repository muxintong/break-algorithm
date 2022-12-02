from typing import List


"""
给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。
设计一个算法使得这 m 个子数组各自和的最大值最小。
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:


def main():
    # 输入：nums = [7,2,5,10,8], m = 2
    # 输出：18
    # 解释：
    # 一共有四种方法将 nums 分割为 2 个子数组。
    # 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
    # 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
    solution1 = Solution()
    print(solution1.splitArray(nums = [7,2,5,10,8], m = 2))

    # 输入：nums = [1,2,3,4,5], m = 2
    # 输出：9
    solution2 = Solution()
    print(solution2.splitArray(nums = [1,2,3,4,5], m = 2))

    # 输入：nums = [1,4,4], m = 3
    # 输出：4
    solution3 = Solution()
    print(solution3.splitArray(nums = [1,4,4], m = 3))

if __name__ == '__main__':
    main()