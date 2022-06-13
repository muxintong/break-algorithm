"""
https://labuladong.github.io/algo/2/18/23/
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            val = numbers[left] + numbers[right]
            if val == target:
                break
            elif val > target:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]


def main():
    # Input: numbers = [2,7,11,15], target = 9
    # Output: [1,2]
    # Explanation: The sum of 2 and 7 is 9.
    # Therefore, index1 = 1, index2 = 2. We return [1, 2].
    soluiton1 = Solution()
    print(soluiton1.twoSum([2,7,11,15], target = 9))

    # Input: numbers = [2,3,4], target = 6
    # Output: [1,3]
    # Explanation: The sum of 2 and 4 is 6.
    # Therefore index1 = 1, index2 = 3. We return [1, 3].
    soluiton1 = Solution()
    print(soluiton1.twoSum(numbers = [2,3,4], target = 6))

    # Input: numbers = [-1,0], target = -1
    # Output: [1,2]
    # Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
    soluiton1 = Solution()
    print(soluiton1.twoSum(numbers = [-1,0], target = -1))

if __name__ == '__main__':
    main()
