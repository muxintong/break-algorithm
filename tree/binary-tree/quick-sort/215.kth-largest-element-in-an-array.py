import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


def main():
    # 输入: [3,2,1,5,6,4], k = 2
    # 输出: 5
    solution1 = Solution()
    print(solution1.findKthLargest([3, 2, 1, 5, 6, 4], k=2))

    # 输入: [3,2,3,1,2,4,5,5,6], k = 4
    # 输出: 4
    solution1 = Solution()
    print(solution1.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))


if __name__ == '__main__':
    main()
