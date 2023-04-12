"""
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash={}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=i
            else:
                if i-hash[nums[i]]<=k:
                    return True
                else:
                    hash[nums[i]]=i
        return False
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0
        while j < len(nums) - 1:
            j += 1
            if nums[i] == nums[j] and abs(i - j) <= k: return True

            while j - i >= k and i < j:
                i += 1
                if nums[i] == nums[j] and i != j and abs(i - j) <= k: return True

        return False


def main():
    # 输入：nums = [1,2,3,1], k = 3
    # 输出：true
    solution1 = Solution()
    print(solution1.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))

    # 输入：nums = [1,0,1,1], k = 1
    # 输出：true
    solution2 = Solution()
    print(solution2.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))

    # 输入：nums = [1,2,3,1,2,3], k = 2
    # 输出：false
    solution3 = Solution()
    print(solution3.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))

    # 输入： [1,2,1], 0
    # 输出： true
    # 预期结果： false
    solution4 = Solution()
    print(solution4.containsNearbyDuplicate([1, 2, 1], 0))

    # 输入： [0,1,2,3,2,5], 3
    # 输出： false
    # 预期结果： true
    solution5 = Solution()
    print(solution5.containsNearbyDuplicate([0, 1, 2, 3, 2, 5], 3))


if __name__ == '__main__':
    main()
