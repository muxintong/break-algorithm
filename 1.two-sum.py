"""
https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 1.sort：由于外层传入时已经排好序,若无外层，此时需先排序
        nums.sort()

        # 2.left-right pointer
        left = 0
        right = len(nums) - 1
        res = []
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
            elif sum < target:
                left += 1
            else:
                right -= 1

        # 对结果集res：二维list去重
        unique_ress = list(set([tuple(t) for t in res]))
        # >>> lists1
        # [(1, 8), (2, 7)]
        # >>> lists1=[list(list1) for list1 in lists1]
        # >>> lists1
        # [[1, 8], [2, 7]]
        #
        # NOTE：转换后为list[(tuple), ...]形式，还需将内层tuple在转为list
        unique_res = [list(member) for member in unique_ress]

        return unique_res


def main():
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    # [(1, 8), (2, 7)]
    solution1 = Solution()
    print(solution1.twoSum(nums=[2, 7, 11, 15, 1, 8], target=9))

    # Input: nums = [3,2,4], target = 6
    # Output: [1,2]
    solution2 = Solution()
    print(solution2.twoSum(nums=[3, 2, 4], target=6))

    # Input [3,3] 6
    # Output [0,0]
    # Expected [0,1]
    solution3 = Solution()
    print(solution3.twoSum(nums=[3, 3, 3], target=6))


if __name__ == '__main__':
    main()
